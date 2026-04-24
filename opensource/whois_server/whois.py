import socket
import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Resource management constants
MAX_WORKERS = 50          # Maximum concurrent client threads
MAX_RECV_SIZE = 1024      # Maximum input payload size in bytes
CONN_TIMEOUT = 10.0       # Per-connection socket timeout in seconds
RATE_LIMIT_WINDOW = 60    # Sliding window duration in seconds for rate limiting
RATE_LIMIT_MAX = 10       # Maximum connections allowed per IP per window

# Per-IP rate limiting state (thread-safe)
_rate_limit_lock = threading.Lock()
_ip_connection_times: dict = {}


def _is_rate_limited(addr) -> bool:
    """Return True if the connecting IP has exceeded the rate limit."""
    ip = addr[0]
    now = time.monotonic()
    with _rate_limit_lock:
        times = _ip_connection_times.get(ip, [])
        # Discard timestamps outside the current window
        times = [t for t in times if now - t < RATE_LIMIT_WINDOW]
        if len(times) >= RATE_LIMIT_MAX:
            _ip_connection_times[ip] = times
            return True
        times.append(now)
        _ip_connection_times[ip] = times
        return False


def whois(query):
    try:
        response = get_whois(query).format(query)
        return response
    except Exception as e:
        logging.error(f"Error processing WHOIS query: {e}")
        return "Internal server error"


def handle_client(client_socket, addr):
    """Handle a single client connection inside a bounded thread pool."""
    try:
        with client_socket:
            client_socket.settimeout(CONN_TIMEOUT)

            try:
                data = client_socket.recv(MAX_RECV_SIZE).strip()
                try:
                    decoded_data = data.decode('utf-8')
                except UnicodeDecodeError:
                    logging.warning(f"Received invalid UTF-8 data from {addr}: {data}")
                    client_socket.sendall("Invalid request encoding".encode('utf-8'))
                    return

                logging.info(f"Request inquiry: {decoded_data}")

                if not decoded_data:
                    logging.warning("Empty request received")
                    return

                response = whois(decoded_data)
                client_socket.sendall(response.encode('utf-8'))

            except socket.timeout:
                logging.warning(f"Connection timed out from {addr}")
            except Exception as e:
                logging.error(f"Unexpected error from {addr}: {e}")
                try:
                    client_socket.sendall("Internal server error".encode('utf-8'))
                except Exception:
                    pass
    except Exception as e:
        logging.error(f"Error handling client socket from {addr}: {e}")


def main():
    host = '0.0.0.0'
    port = 43

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    logging.info(f"WHOIS Server Started, port: {port}")

    # Bounded thread pool prevents unbounded thread creation (resource exhaustion)
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        while True:
            try:
                client_socket, addr = server_socket.accept()
                logging.info(f"Received connection from {addr}")

                # Per-IP rate limiting to block connection-flood attacks
                if _is_rate_limited(addr):
                    logging.warning(f"Rate limit exceeded for {addr}, dropping connection")
                    try:
                        client_socket.sendall(
                            "Rate limit exceeded. Please try again later.\r\n".encode('utf-8')
                        )
                    except Exception:
                        pass
                    client_socket.close()
                    continue

                executor.submit(handle_client, client_socket, addr)

            except Exception as e:
                logging.error(f"Error accepting connection: {e}")

if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as e:
            logging.critical(f"Critical error in main loop: {e}")
            time.sleep(1)
