# 0x10. HTTPS SSL

## Description
This project introduces SSL/TLS certificates and HTTPS configuration. You'll learn about the importance of HTTPS for securing web traffic, how to configure SSL termination on HAProxy, and how to audit your DNS configuration. Understanding HTTPS is crucial for securing modern web applications and protecting user data.

## Concepts
For this project, you should understand:
- **DNS**
- **Web stack debugging**
- **HTTPS/SSL**
- **SSL termination**
- **SSL certificates**

## Background Context
### What happens when you don't secure your website traffic?

![HTTP vs HTTPS](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/FlhGPEK.png)

HTTPS (HyperText Transfer Protocol Secure) is a protocol for secure communication over a computer network. It's the secure version of HTTP, where all communications between your browser and the website are encrypted.

## Learning Objectives
At the end of this project, you should be able to explain:

### General
- What is HTTPS SSL 2 main roles
- What is the purpose encrypting traffic
- What SSL termination means

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script does

## Your Servers

| Name | Username | IP | State |
|------|----------|-----|-------|
| [STUDENT_ID]-web-01 | ubuntu | XXX.XXX.XXX.XXX | running |
| [STUDENT_ID]-web-02 | ubuntu | XXX.XXX.XXX.XXX | running |
| [STUDENT_ID]-lb-01 | ubuntu | XXX.XXX.XXX.XXX | running |

## Tasks

### 0. World wide web
**File:** `0-world_wide_web`

Configure your domain zone so that the subdomain `www` points to your load-balancer IP (`lb-01`). Let's also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

**Requirements:**
- Add the subdomain `www` to your domain, point it to your `lb-01` IP (your domain name might be configured with default subdomains, feel free to remove them)
- Add the subdomain `lb-01` to your domain, point it to your `lb-01` IP
- Add the subdomain `web-01` to your domain, point it to your `web-01` IP
- Add the subdomain `web-02` to your domain, point it to your `web-02` IP
- Your Bash script must accept 2 arguments:
  1. `domain`:
     - type: string
     - what: domain name to audit
     - mandatory: yes
  2. `subdomain`:
     - type: string
     - what: specific subdomain to audit
     - mandatory: no
- Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
- When only the parameter `domain` is provided, display information for its subdomains `www`, `lb-01`, `web-01` and `web-02` - in this specific order
- When passing `domain` and `subdomain` parameters, display information for the specified subdomain
- Ignore `shellcheck` case `SC2086`
- Must use:
  - `awk`
  - at least one Bash function
- You do not need to handle edge cases such as:
  - Empty parameters
  - Nonexistent domain names
  - Nonexistent subdomains

**Example:**
```bash
$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100

$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
```

---

### 1. HAproxy SSL termination
**File:** `1-haproxy_ssl_termination`

"Terminating SSL on HAproxy" means that HAProxy is configured to handle encrypted traffic, unencrypt it and pass it to its destination.

Create a certificate using `certbot` and configure HAproxy to accept encrypted traffic for your subdomain `www.`.

**Requirements:**
- HAProxy must be listening on port TCP 443
- HAProxy must be accepting SSL traffic
- HAProxy must serve encrypted traffic that will return the `/` of your web server
- When querying the root of your domain name, the page returned must contain `Holberton School`
- Share your HAProxy config as an answer file (`/etc/haproxy/haproxy.cfg`)

The file `1-haproxy_ssl_termination` must be your HAProxy configuration file

Make sure to install HAProxy 1.5 or higher, SSL termination is not available before v1.5.

**Example:**
```bash
$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

$ curl https://www.holberton.online
Holberton School for the win!
```

---

### 2. No loophole in your website traffic
**File:** `100-redirect_http_to_https`

A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAProxy to automatically redirect HTTP traffic to HTTPS.

**Requirements:**
- This should be transparent to the user
- HAProxy should return a 301 (Moved Permanently)
- HAProxy should redirect HTTP traffic to HTTPS
- Share your HAProxy config as an answer file (`/etc/haproxy/haproxy.cfg`)

The file `100-redirect_http_to_https` must be your HAProxy configuration file

**Example:**
```bash
$ curl -sIL http://www.holberton.online
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://www.holberton.online/
Connection: close

HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 02:19:18 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
```

---

## HTTPS/SSL Concepts

### What is HTTPS?
HTTPS (HyperText Transfer Protocol Secure) is an extension of HTTP that uses encryption to secure communications between a client and server. It uses SSL/TLS protocols to encrypt data.

### Two Main Roles of HTTPS SSL

#### 1. Privacy/Encryption
- Encrypts data transmitted between client and server
- Prevents eavesdropping and man-in-the-middle attacks
- Protects sensitive information (passwords, credit cards, personal data)

#### 2. Authentication
- Verifies the identity of the website
- Ensures you're communicating with the legitimate server
- Prevents phishing and impersonation attacks

### What is SSL Termination?
SSL termination is the process of decrypting SSL/TLS traffic at the load balancer level, then forwarding unencrypted traffic to backend servers.

**Benefits:**
- Reduces CPU load on backend servers
- Centralizes certificate management
- Simplifies backend server configuration
- Enables inspection and caching of traffic

**How it works:**
```
Client (HTTPS) → Load Balancer (Decrypts) → Backend Server (HTTP)
```

## SSL/TLS Certificates

### What is an SSL Certificate?
An SSL certificate is a digital certificate that authenticates a website's identity and enables an encrypted connection. It contains:
- Domain name
- Certificate authority
- Certificate's issuance and expiration dates
- Public key
- Digital signature

### Types of SSL Certificates

#### 1. Domain Validated (DV)
- Basic level of validation
- Verifies domain ownership only
- Quick to obtain (minutes)
- Free options available (Let's Encrypt)

#### 2. Organization Validated (OV)
- Validates organization identity
- More thorough vetting process
- Takes days to obtain
- Shows organization name

#### 3. Extended Validation (EV)
- Highest level of validation
- Extensive vetting process
- Takes weeks to obtain
- Shows green address bar (in older browsers)

### Let's Encrypt
Let's Encrypt is a free, automated, and open Certificate Authority. It provides free SSL/TLS certificates that are trusted by all major browsers.

## Obtaining SSL Certificates with Certbot

### Installing Certbot
```bash
# Ubuntu 16.04
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install certbot
```

### Obtaining a Certificate (Standalone)
```bash
# Stop your web server first
sudo service nginx stop
sudo service haproxy stop

# Obtain certificate
sudo certbot certonly --standalone -d www.yourdomain.com

# Certificates will be saved to:
# /etc/letsencrypt/live/www.yourdomain.com/fullchain.pem
# /etc/letsencrypt/live/www.yourdomain.com/privkey.pem
```

### Combining Certificate and Key for HAProxy
HAProxy requires the certificate and private key in a single file:

```bash
sudo mkdir -p /etc/haproxy/certs
sudo cat /etc/letsencrypt/live/www.yourdomain.com/fullchain.pem \
    /etc/letsencrypt/live/www.yourdomain.com/privkey.pem \
    | sudo tee /etc/haproxy/certs/www.yourdomain.com.pem
sudo chmod 600 /etc/haproxy/certs/www.yourdomain.com.pem
```

### Certificate Renewal
Let's Encrypt certificates expire after 90 days. Set up automatic renewal:

```bash
# Test renewal
sudo certbot renew --dry-run

# Add to crontab for automatic renewal
sudo crontab -e
# Add this line:
0 0 * * * certbot renew --post-hook "cat /etc/letsencrypt/live/www.yourdomain.com/fullchain.pem /etc/letsencrypt/live/www.yourdomain.com/privkey.pem > /etc/haproxy/certs/www.yourdomain.com.pem && service haproxy reload"
```

## HAProxy SSL Configuration

### Basic SSL Termination Configuration

```bash
global
    log /dev/log local0
    log /dev/log local1 notice
    chroot /var/lib/haproxy
    stats socket /run/haproxy/admin.sock mode 660 level admin
    stats timeout 30s
    user haproxy
    group haproxy
    daemon

    # Default SSL material locations
    ca-base /etc/ssl/certs
    crt-base /etc/ssl/private

    # SSL configuration
    ssl-default-bind-ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384
    ssl-default-bind-options no-sslv3 no-tlsv10 no-tlsv11
    tune.ssl.default-dh-param 2048

defaults
    log     global
    mode    http
    option  httplog
    option  dontlognull
    option  forwardfor
    option  http-server-close
    timeout connect 5000
    timeout client  50000
    timeout server  50000
    errorfile 400 /etc/haproxy/errors/400.http
    errorfile 403 /etc/haproxy/errors/403.http
    errorfile 408 /etc/haproxy/errors/408.http
    errorfile 500 /etc/haproxy/errors/500.http
    errorfile 502 /etc/haproxy/errors/502.http
    errorfile 503 /etc/haproxy/errors/503.http
    errorfile 504 /etc/haproxy/errors/504.http

frontend www-https
    bind *:443 ssl crt /etc/haproxy/certs/www.yourdomain.com.pem
    http-request set-header X-Forwarded-Proto https
    default_backend www-backend

backend www-backend
    balance roundrobin
    server web-01 [WEB-01-IP]:80 check
    server web-02 [WEB-02-IP]:80 check
```

### HTTP to HTTPS Redirect Configuration

```bash
frontend www-http
    bind *:80
    # Redirect all HTTP traffic to HTTPS
    redirect scheme https code 301 if !{ ssl_fc }

frontend www-https
    bind *:443 ssl crt /etc/haproxy/certs/www.yourdomain.com.pem
    http-request set-header X-Forwarded-Proto https
    default_backend www-backend

backend www-backend
    balance roundrobin
    server web-01 [WEB-01-IP]:80 check
    server web-02 [WEB-02-IP]:80 check
```

## DNS Configuration

### A Records
An A record (Address Record) maps a domain name to an IPv4 address.

**Example:**
```
www.yourdomain.com    IN    A    54.210.47.110
lb-01.yourdomain.com  IN    A    54.210.47.110
web-01.yourdomain.com IN    A    34.198.248.145
web-02.yourdomain.com IN    A    54.89.38.100
```

### Checking DNS Records
```bash
# Using dig
dig www.yourdomain.com

# Using nslookup
nslookup www.yourdomain.com

# Check specific record type
dig www.yourdomain.com A
```

### DNS Propagation
After changing DNS records, it can take time for changes to propagate:
- Local DNS cache: seconds to minutes
- ISP DNS cache: minutes to hours
- Global propagation: up to 48 hours (usually much faster)

## Testing Your HTTPS Configuration

### Test SSL Certificate
```bash
# Check certificate details
openssl s_client -connect www.yourdomain.com:443

# Test HTTPS connection
curl -I https://www.yourdomain.com

# Test with verbose output
curl -v https://www.yourdomain.com
```

### Test HTTP to HTTPS Redirect
```bash
# Should show 301 redirect
curl -sIL http://www.yourdomain.com

# Check redirect location
curl -I http://www.yourdomain.com | grep Location
```

### SSL Labs Test
Use [SSL Labs](https://www.ssllabs.com/ssltest/) to test your SSL configuration and get a security grade.

### Test HAProxy Configuration
```bash
# Check configuration syntax
sudo haproxy -c -f /etc/haproxy/haproxy.cfg

# Restart HAProxy
sudo service haproxy restart

# Check HAProxy status
sudo service haproxy status
```

## Security Best Practices

### 1. Use Strong Cipher Suites
```bash
ssl-default-bind-ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384
```

### 2. Disable Old SSL/TLS Versions
```bash
ssl-default-bind-options no-sslv3 no-tlsv10 no-tlsv11
```

### 3. Use HSTS (HTTP Strict Transport Security)
```bash
http-response set-header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
```

### 4. Keep Certificates Up to Date
- Monitor expiration dates
- Automate renewal process
- Test renewal before expiration

### 5. Use Strong DH Parameters
```bash
tune.ssl.default-dh-param 2048
```

## Common Issues and Solutions

### Issue: Certificate Not Trusted
**Solution:** Ensure using fullchain.pem (includes intermediate certificates)

### Issue: Mixed Content Warnings
**Solution:** Ensure all resources (images, CSS, JS) use HTTPS

### Issue: HAProxy Won't Start
**Solution:** Check certificate file permissions (should be 600)

### Issue: Certificate Expired
**Solution:** Renew certificate and reload HAProxy

### Issue: DNS Not Resolving
**Solution:** Wait for DNS propagation, check DNS configuration

## Debugging Commands

```bash
# Check certificate expiration
openssl x509 -in /etc/haproxy/certs/www.yourdomain.com.pem -noout -dates

# View certificate details
openssl x509 -in /etc/haproxy/certs/www.yourdomain.com.pem -text -noout

# Check HAProxy logs
sudo tail -f /var/log/haproxy.log

# Test SSL handshake
openssl s_client -connect www.yourdomain.com:443 -servername www.yourdomain.com

# Check listening ports
sudo netstat -tuln | grep -E ':80|:443'
```

## Resources

- [What is HTTPS?](https://www.instantssl.com/http-vs-https)
- [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
- [HAProxy SSL termination on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-implement-ssl-termination-with-haproxy-on-ubuntu-14-04)
- [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
- [Bash function](https://tldp.org/LDP/abs/html/functions.html)
- [Let's Encrypt](https://letsencrypt.org/)
- [Certbot Documentation](https://certbot.eff.org/)
- [SSL Labs](https://www.ssllabs.com/ssltest/)

## Author
This project is part of the ALX Software Engineering Program.

## License
This project is licensed under the terms of the ALX Software Engineering Program.
