# 🌐 DigitalPlat FreeDomain - Complete Registration Guide

Welcome to **DigitalPlat FreeDomain**! Get your free domain name in minutes. This guide will walk you through the entire process from registration to getting your domain online.

## 📋 Table of Contents
- [Why Free Domains?](#-why-free-domains)
- [Available Domain Extensions](#-available-domain-extensions)
- [Quick Start Guide](#-quick-start-guide)
- [Step 1: Create Your Account](#step-1-create-your-account)
- [Step 2: Register Your Domain](#step-2-register-your-domain)
- [Step 3: Setup Free DNS (Nameservers)](#step-3-setup-free-dns-nameservers)
- [Step 4: Configure Your Domain](#step-4-configure-your-domain)
- [Domain Limits & Rules](#-domain-limits--rules)
- [FAQ](#-faq)
- [Community & Support](#-community--support)

---

## ✔️ Why Free Domains?

At **DigitalPlat FreeDomain**, we're on a mission to make the web more accessible. We believe that the cost of a domain shouldn't hold anyone back from creating a website. Our goal is to make the internet an open space where everyone can have their own place online, regardless of budget.

**🌟 Trusted by Thousands** - Over 350,000 domains already registered!

---

## 🌍 Available Domain Extensions

- **.DPDNS.ORG**
- **.US.KG**
- **.QZZ.IO**
- **.XX.KG**

_(More extensions coming soon!)_

---

## 🚀 Quick Start Guide

**Total Time**: ~15 minutes  
**Cost**: $0 (Completely Free)

1. Create account → 2. Register domain → 3. Setup DNS → 4. Go live!

---

## Step 1: Create Your Account

### 1.1 Visit Registration Page
Go to: **https://dash.domain.digitalplat.org/auth/register**

### 1.2 Fill in Required Information

#### Basic Information:
- **Username**: 5-50 characters, no spaces (e.g., `johnsmith123`)
- **Legal Full Name**: Your real name with space (e.g., `John Smith`)
  - ⚠️ **Important**: Cannot be changed after registration
  - Must match KYC documents if required later
- **Email Address**: Use these providers for GitHub KYC option:
  - `gmail.com`, `outlook.com`, `yahoo.com`, `hotmail.com`
  - `zoho.com`, `yandex.com`, `icloud.com`
  - `163.com`, `126.com`, `qq.com`
- **Phone Number**: Format: `+1-3100000000`
  - Include country code
  - Used for account recovery
- **Full Address**: Complete address (e.g., `1000 Santa Monica Blvd, Santa Monica, CA 90401, United States`)

#### Password Requirements:
- Minimum 8 characters
- Must include uppercase letters
- Must include lowercase letters
- Must include numbers
- Cannot contain: `& * ' " < > \ / spaces`

### 1.3 Accept Terms
Read and agree to:
- [Terms of Service](https://nic.us.kg/terms-of-service/)
- [Privacy Policy](https://nic.us.kg/privacy-policy/)
- [Acceptable Use Policy](https://nic.us.kg/acceptable-use-policy/)

### 1.4 Complete CAPTCHA & Register
- Solve the CAPTCHA
- Click **"Register!"**
- Check your email for confirmation

---

## Step 2: Register Your Domain

### 2.1 Login to Dashboard
Go to: **https://dash.domain.digitalplat.org/auth/login**

### 2.2 Check Domain Availability
1. Click **"Domain Registration"** in the sidebar
2. Enter your desired domain name (without the extension)
3. Select your preferred extension (`.us.kg`, `.qzz.io`, etc.)
4. Click **"Check"**

### 2.3 Domain Checkout
If available, you'll see:
```
✅ Congratulations! This domain name is now available

Your domain information:
Name: yourdomain.us.kg
Administrator: YourUsername
Price: Always free, with a default registration period of one year (365 days)
```

**🎯 Now you need to configure nameservers** → Continue to Step 3

---

## Step 3: Setup Free DNS (Nameservers)

**What are Nameservers?** They tell the internet where to find your website when someone visits your domain.

### Option A: Cloudflare (⭐ Recommended)

**Why Cloudflare?**
- ✅ Free forever
- ✅ Fast global network (CDN)
- ✅ Free SSL certificates
- ✅ DDoS protection
- ✅ Easy to use dashboard

#### Setup Steps:

**1. Create Cloudflare Account**
- Go to: https://dash.cloudflare.com/sign-up
- Sign up with your email
- Verify your email

**2. Add Your Domain**
- Click **"Add Site"**
- Enter your full domain (e.g., `yourdomain.us.kg`)
- Select **Free Plan** → Click **Continue**

**3. Get Your Nameservers**
Cloudflare will display something like:
```
kip.ns.cloudflare.com
uma.ns.cloudflare.com
```
*(Your nameservers will be different)*

**4. Copy Nameservers**
- Copy both nameserver addresses
- Keep this tab open

**5. Return to DigitalPlat**
- Go back to your domain checkout page
- Enter nameservers:
  - **Name Server 1**: `kip.ns.cloudflare.com` (use your own)
  - **Name Server 2**: `uma.ns.cloudflare.com` (use your own)
  - Leave 3-6 empty
- Click **"Submit"** or **"Register"**

**6. Complete Setup**
- Return to Cloudflare dashboard
- Click **"Done, check nameservers"**
- Wait 24-48 hours for DNS propagation

---

### Option B: FreeDNS (Afraid.org)

**Free, simple DNS hosting**

#### Setup Steps:

**1. Create Account**
- Go to: https://freedns.afraid.org/signup/
- Create free account

**2. Add Domain**
- Login to FreeDNS
- Go to **"Add a domain"**
- Enter your domain (e.g., `yourdomain.us.kg`)

**3. Get Nameservers**
FreeDNS uses:
```
ns1.afraid.org
ns2.afraid.org
ns3.afraid.org (optional)
ns4.afraid.org (optional)
```

**4. Enter in DigitalPlat**
- **Name Server 1**: `ns1.afraid.org`
- **Name Server 2**: `ns2.afraid.org`
- **Name Server 3**: `ns3.afraid.org` (optional)
- **Name Server 4**: `ns4.afraid.org` (optional)

---

### Option C: Hostry

**Professional DNS hosting**

**Nameservers:**
```
ns1.hostry.com
ns2.hostry.com
```

**Setup:**
1. Visit: https://hostry.com
2. Create account and add your domain
3. Use the nameservers above in DigitalPlat

---

### Option D: Other DNS Providers

You can use any DNS provider:
- **Hurricane Electric**: `ns1.he.net`, `ns2.he.net`
- **ClouDNS**: Custom nameservers
- **Your Own Server**: Run PowerDNS or BIND

---

## Step 4: Configure Your Domain

### After Nameserver Configuration:

**1. Wait for DNS Propagation**
- Usually takes 1-24 hours
- Can take up to 48 hours
- Check status: https://www.whatsmydns.net/

**2. Add DNS Records (in your DNS provider)**

Once propagation is complete, go to your DNS provider (e.g., Cloudflare):

#### For a Website:
```
Type: A
Name: @ (or yourdomain.us.kg)
Content: Your server IP address (e.g., 192.0.2.1)
TTL: Auto
```

#### For WWW subdomain:
```
Type: CNAME
Name: www
Content: yourdomain.us.kg
TTL: Auto
```

#### For Email (MX Record):
```
Type: MX
Name: @
Content: mail.yourprovider.com
Priority: 10
TTL: Auto
```

**3. Test Your Domain**
- Visit `http://yourdomain.us.kg` in a browser
- It should now point to your website!

---

## 📊 Domain Limits & Rules

| Item | Limit |
|------|-------|
| **Domains per account** | 3 maximum |
| **Registration period** | 365 days (1 year) |
| **Renewal** | Available when <180 days remaining |
| **Cost** | Always FREE |
| **Subdomains** | Unlimited (via DNS panel) |
| **WHOIS privacy** | Available |

### ⚠️ Important Rules:
- ✅ **One account per person/organization**
- ✅ **Genuine information required**
- ❌ **No spam, malware, or abuse**
- ❌ **No reselling domains**
- ❌ **No illegal content**

---

## ❔ FAQ

### How many free domain names can I register?
Currently limited to **3 domains per account** due to abuse prevention.

### Which DNS platforms can I use?
Any DNS management system! Popular choices:
- Cloudflare (recommended)
- FreeDNS (Afraid.org)
- Hostry
- Hurricane Electric
- Your own DNS server (PowerDNS, BIND)

### Do I need to star this project?
No, but we'd be deeply grateful! It helps more people discover free domains. ⭐

### Does Cloudflare work?
Yes! Full support for:
- DNS management
- CDN (Content Delivery Network)
- DDoS protection
- Free SSL certificates
- Page rules and caching

### Can I create subdomains?
Yes! Create unlimited subdomains via your DNS panel:
- `blog.yourdomain.us.kg`
- `shop.yourdomain.us.kg`
- `api.yourdomain.us.kg`

### What if my domain is taken?
Try variations or use a different extension (`.us.kg`, `.qzz.io`, `.dpdns.org`, `.xx.kg`)

### How do I renew my domain?
Renewal option appears in your dashboard when less than 180 days remain.

### Is KYC required?
Only for certain cases. If using approved email providers (Gmail, Outlook, etc.), you can use GitHub's free KYC option.

---

## 🤝 Community & Support

### Get Help & Connect:

📱 **Telegram**: https://t.me/digitalplatdomain  
💬 **Discord**: https://discord.gg/ma4RZzMmVW  
💻 **GitHub Discussions**: https://github.com/DigitalPlatDev/FreeDomain/discussions

### Report Issues:
🐛 **Bug Reports**: https://github.com/DigitalPlatDev/US.KG-Issues/issues/new/choose  
📧 **General Contact**: contact@nic.us.kg

---

## 🚨 Abuse Reporting

We take domain abuse seriously and maintain a safer internet.

**Report abuse:**
- 📧 **Email**: abusereport@digitalplat.org
- 📝 **Form**: [Abuse Report Form](https://docs.google.com/forms/d/e/1FAIpQLSdCuhUBFynK4d2YZXptEhV4QHei9-FAk2WhKovrnZRx01lSIQ/viewform)

Response time: Few hours to several days depending on complexity.

---

## ⏭️ What's Next

We're working on:
- 🌐 More domain extensions
- 🏠 Free hosting options
- 🛠️ Additional tools and features

**We can't wait to see what you build!**

---

## 📚 Additional Resources

- [Complete Tutorial](./documents/tutorial/getting-started/1-register-account.md)
- [FAQ Page](./documents/domains/faq.md)
- [Terms of Service](https://nic.us.kg/terms-of-service/)
- [Privacy Policy](https://nic.us.kg/privacy-policy/)
- [Acceptable Use Policy](https://nic.us.kg/acceptable-use-policy/)

---

**🎉 Ready to get started?**  
👉 [Register Your Free Domain Now](https://dash.domain.digitalplat.org/)

---

<div align="center">

Made with ❤️ by DigitalPlat  
*Making the internet accessible to everyone*

</div>
