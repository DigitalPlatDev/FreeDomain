import os
import socket
import logging
import time
import collections


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Rate limiting: max 10 requests per 60 seconds per IP
RATE_LIMIT_MAX = 10
RATE_LIMIT_WINDOW = 60
_rate_limit_store = collections.defaultdict(list)

def is_rate_limited(ip):
    now = time.time()
    window_start = now - RATE_LIMIT_WINDOW
    _rate_limit_store[ip] = [t for t in _rate_limit_store[ip] if t > window_start]
    if len(_rate_limit_store[ip]) >= RATE_LIMIT_MAX:
        return True
    _rate_limit_store[ip].append(now)
    return False

def whois(query):
    try:
        response = get_whois(query).format(query)
        return response
    except Exception as e:
        logging.error(f"Error processing WHOIS query: {e}")
        return "Internal server error"

def main():
    host = os.getenv("WHOIS_BIND_ADDRESS", "127.0.0.1")
    port = 43

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    logging.info(f"WHOIS Server Started, port: {port}")

    while True:
        try:
            client_socket, addr = server_socket.accept()
            logging.info(f"Received connection from {addr}")
            client_ip = addr[0]

            if is_rate_limited(client_ip):
                logging.warning(f"Rate limit exceeded for {client_ip}")
                try:
                    client_socket.sendall("Rate limit exceeded. Try again later.\r\n".encode('utf-8'))
                finally:
                    client_socket.close()
                continue

            try:
                with client_socket:
                    client_socket.settimeout(10.0)
                    
                    try:
                        data = client_socket.recv(1024).strip()
                        try:
                            decoded_data = data.decode('utf-8')
                        except UnicodeDecodeError:
                            logging.warning(f"Received invalid UTF-8 data from {addr}: {data}")
                            client_socket.sendall("Invalid request encoding".encode('utf-8'))
                            continue

                        logging.info(f"Request inquiry: {decoded_data}")
                        
                        if not decoded_data:
                            logging.warning("Empty request received")
                            continue

                        response = whois(decoded_data)
                        client_socket.sendall(response.encode('utf-8'))

                    except socket.timeout:
                        logging.warning("Connection timed out")
                    except Exception as e:
                        logging.error(f"Unexpected error: {e}")
                        client_socket.sendall("Internal server error".encode('utf-8'))

            except Exception as e:
                logging.error(f"Error handling client socket: {e}")

        except Exception as e:
            logging.error(f"Error accepting connection: {e}")

if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as e:
            logging.critical(f"Critical error in main loop: {e}")
            import time
            time.sleep(1)
