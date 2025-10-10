# 0x13. Firewall

## Description
This project introduces firewall concepts and implementation using UFW (Uncomplicated Firewall) on Ubuntu. You'll learn how to configure firewall rules to protect your servers while allowing necessary traffic. Understanding firewalls is crucial for securing web infrastructure and preventing unauthorized access.

## Concepts
For this project, you should understand:
- **Network security**
- **Firewall fundamentals**
- **Port management**
- **TCP/IP protocols**
- **Web stack security**

## Background Context
### Warning!
Firewalls can be tricky. If you configure them incorrectly, you might block yourself from accessing your servers. Be very careful when working with firewalls on production servers.

**Important:** Always make sure you have multiple ways to access your server (like console access through your hosting provider) before making firewall changes.

Your servers are already behind a firewall provided by your hosting infrastructure, but you'll be adding an additional layer of security with a host-based firewall.

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash scripts must pass `Shellcheck` without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script does

## Your Servers

| Name | Username | IP | State |
|------|----------|-----|-------|
| [STUDENT_ID]-web-01 | ubuntu | XXX.XXX.XXX.XXX | running |
| [STUDENT_ID]-web-02 | ubuntu | XXX.XXX.XXX.XXX | running |
| [STUDENT_ID]-lb-01 | ubuntu | XXX.XXX.XXX.XXX | running |

## Tasks

### 0. Block all incoming traffic but
**File:** `0-block_all_incoming_traffic_but`

Let's install the `ufw` firewall and setup a few rules on `web-01`.

**Requirements:**
- The requirements below must be applied to `web-01` (feel free to do it on `lb-01` and `web-02`, but it won't be checked)
- Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
  - `22` (SSH)
  - `443` (HTTPS SSL)
  - `80` (HTTP)
- Share the `ufw` commands that you used in your answer file

**Example:**
```bash
root@03-web-01:~# ufw status
Status: active

To                         Action      From
--                         ------      ----
22                         ALLOW       Anywhere
80                         ALLOW       Anywhere
443                        ALLOW       Anywhere
22 (v6)                    ALLOW       Anywhere (v6)
80 (v6)                    ALLOW       Anywhere (v6)
443 (v6)                   ALLOW       Anywhere (v6)
```

---

### 1. Port forwarding
**File:** `100-port_forwarding`

Firewalls can not only filter requests, they can also forward them.

**Requirements:**
- Configure `web-01` so that its firewall redirects port `8080/TCP` to port `80/TCP`
- Your answer file should be a copy of the `ufw` configuration file that you modified to make this happen

**Terminal in web-01:**
```bash
root@03-web-01:~# netstat -lpn
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      2473/nginx
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      978/sshd
tcp6       0      0 :::80                   :::*                    LISTEN      2473/nginx
tcp6       0      0 :::22                   :::*                    LISTEN      978/sshd
udp        0      0 0.0.0.0:68              0.0.0.0:*                           594/dhclient
udp6       0      0 :::33099                :::*                                594/dhclient
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ACC ]     STREAM     LISTENING     7724     1/init              @/com/ubuntu/upstart
unix  2      [ ACC ]     STREAM     LISTENING     6525     1/init              /var/run/dbus/system_bus_socket
```

**My machine:**
```bash
vagrant@03:~$ curl -sI web-01.holberton.online:80
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 07 Mar 2017 02:14:41 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes

vagrant@03:~$ curl -sI web-01.holberton.online:8080
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 07 Mar 2017 02:14:43 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes
```

---

## Firewall Fundamentals

### What is a Firewall?
A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It acts as a barrier between a trusted internal network and untrusted external networks.

### Types of Firewalls

#### 1. Network Firewall (External)
- Hardware or software-based
- Sits at the network perimeter
- Protects entire networks
- Examples: Cisco ASA, Palo Alto Networks

#### 2. Host-based Firewall (Internal)
- Software running on individual servers
- Protects specific hosts
- Examples: UFW, iptables, Windows Firewall
- **This project focuses on host-based firewalls**

### Firewall Policies

#### Default Deny (Recommended)
- Block all traffic by default
- Explicitly allow only necessary traffic
- More secure approach
- Used in this project

#### Default Allow
- Allow all traffic by default
- Explicitly block unwanted traffic
- Less secure
- Not recommended for production

---

## UFW (Uncomplicated Firewall)

### What is UFW?
UFW is a user-friendly frontend for managing iptables firewall rules on Ubuntu and Debian systems. It simplifies the process of configuring a firewall.

### Installing UFW
```bash
# Update package list
sudo apt-get update

# Install UFW
sudo apt-get install ufw

# Check UFW status
sudo ufw status
```

### Basic UFW Commands

#### Enable/Disable UFW
```bash
# Enable firewall
sudo ufw enable

# Disable firewall
sudo ufw disable

# Check status
sudo ufw status
sudo ufw status verbose
sudo ufw status numbered
```

#### Default Policies
```bash
# Deny all incoming traffic
sudo ufw default deny incoming

# Allow all outgoing traffic
sudo ufw default allow outgoing

# Check defaults
sudo ufw status verbose
```

#### Allow Rules
```bash
# Allow specific port
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443

# Allow specific port with protocol
sudo ufw allow 22/tcp
sudo ufw allow 53/udp

# Allow port range
sudo ufw allow 6000:6007/tcp

# Allow from specific IP
sudo ufw allow from 192.168.1.100

# Allow from specific IP to specific port
sudo ufw allow from 192.168.1.100 to any port 22

# Allow subnet
sudo ufw allow from 192.168.1.0/24
```

#### Deny Rules
```bash
# Deny specific port
sudo ufw deny 23

# Deny from specific IP
sudo ufw deny from 192.168.1.100
```

#### Delete Rules
```bash
# Delete by rule specification
sudo ufw delete allow 80

# Delete by rule number (use 'status numbered' first)
sudo ufw status numbered
sudo ufw delete 2
```

#### Reset UFW
```bash
# Reset all rules to default
sudo ufw reset
```

---

## Common Port Numbers

### Well-Known Ports (0-1023)

| Port | Protocol | Service |
|------|----------|---------|
| 20 | TCP | FTP Data Transfer |
| 21 | TCP | FTP Control |
| 22 | TCP | SSH (Secure Shell) |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP (Email) |
| 53 | TCP/UDP | DNS |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 (Email) |
| 143 | TCP | IMAP (Email) |
| 443 | TCP | HTTPS |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 8080 | TCP | HTTP Alternate |

### Ports for This Project
- **22**: SSH (remote access)
- **80**: HTTP (web traffic)
- **443**: HTTPS (secure web traffic)

---

## Port Forwarding

### What is Port Forwarding?
Port forwarding (or port redirection) redirects a communication request from one address and port number combination to another while packets are traversing a network gateway, such as a firewall.

### Use Cases
- Redirect HTTP traffic from port 8080 to port 80
- Run multiple services on different internal ports
- Hide actual service ports from external users
- Load balancing and proxying

### UFW Port Forwarding Configuration

Port forwarding in UFW requires editing configuration files because it's not available through the command-line interface.

#### Location
```bash
/etc/ufw/before.rules
```

#### Add NAT Rules
Edit `/etc/ufw/before.rules` and add before the `*filter` section:

```bash
# NAT table rules
*nat
:PREROUTING ACCEPT [0:0]

# Port forward 8080 to 80
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80

# Commit the changes
COMMIT
```

#### Enable Forwarding
Edit `/etc/ufw/sysctl.conf` or `/etc/sysctl.conf`:

```bash
# Uncomment this line:
net/ipv4/ip_forward=1
```

#### Apply Changes
```bash
# Reload UFW
sudo ufw disable
sudo ufw enable

# Or reload sysctl
sudo sysctl -p
```

---

## Security Best Practices

### 1. Principle of Least Privilege
Only open ports that are absolutely necessary for your services.

```bash
# Bad: Allow all ports
sudo ufw allow 1:65535/tcp

# Good: Only allow necessary ports
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

### 2. Use Specific Rules
Be as specific as possible with your rules.

```bash
# Better: Allow SSH only from specific IP
sudo ufw allow from 192.168.1.100 to any port 22

# Even better: Allow SSH from specific subnet
sudo ufw allow from 192.168.1.0/24 to any port 22
```

### 3. Rate Limiting
Protect against brute force attacks.

```bash
# Limit SSH connections (6 attempts per 30 seconds)
sudo ufw limit 22/tcp
```

### 4. Log Everything
Enable logging to monitor firewall activity.

```bash
# Enable logging
sudo ufw logging on

# Set log level (low, medium, high, full)
sudo ufw logging medium

# View logs
sudo tail -f /var/log/ufw.log
```

### 5. Regular Audits
Regularly review your firewall rules.

```bash
# List all rules
sudo ufw status numbered

# Remove unnecessary rules
sudo ufw delete [rule-number]
```

### 6. Test Before Production
Always test firewall changes on a non-production system first.

### 7. Have a Backup Access Method
Before enabling a firewall on a remote server, ensure you have:
- Console access through your hosting provider
- Another SSH key or login method
- Recovery mode access

---

## Testing Your Firewall

### Test Port Accessibility

#### From Another Machine
```bash
# Test if port is open
telnet your-server-ip 80
nc -zv your-server-ip 80

# Test HTTP
curl http://your-server-ip

# Test HTTPS
curl https://your-server-ip

# Scan ports (use responsibly)
nmap your-server-ip
```

#### From the Server Itself
```bash
# Check listening ports
sudo netstat -tuln
sudo ss -tuln

# Check UFW status
sudo ufw status verbose
sudo ufw status numbered

# Test locally
curl localhost:80
curl localhost:443
```

### Test Port Forwarding
```bash
# Test from another machine
curl http://your-server-ip:8080

# Should return the same as
curl http://your-server-ip:80

# Check with netstat (should NOT show 8080 listening)
netstat -tuln | grep 8080
```

---

## Troubleshooting

### Issue: Locked Out of Server
**Prevention:**
```bash
# Always allow SSH before enabling firewall
sudo ufw allow 22/tcp
sudo ufw enable
```

**Solution:**
- Use console access from your hosting provider
- Disable UFW: `sudo ufw disable`
- Fix rules, then re-enable

### Issue: Firewall Not Blocking Traffic
**Check:**
```bash
# Is UFW enabled?
sudo ufw status

# Are rules correct?
sudo ufw status numbered

# Check iptables rules
sudo iptables -L -v -n
```

**Solution:**
```bash
# Reload UFW
sudo ufw reload

# Or restart
sudo ufw disable
sudo ufw enable
```

### Issue: Port Forwarding Not Working
**Check:**
```bash
# Is IP forwarding enabled?
cat /proc/sys/net/ipv4/ip_forward
# Should output: 1

# Check NAT rules
sudo iptables -t nat -L -v -n

# Check before.rules syntax
sudo ufw reload
```

**Solution:**
```bash
# Enable IP forwarding
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

# Make permanent in /etc/sysctl.conf
net.ipv4.ip_forward=1

# Reload
sudo sysctl -p
sudo ufw disable && sudo ufw enable
```

### Issue: Service Not Accessible After Firewall Setup
**Check:**
```bash
# Is the service running?
sudo systemctl status nginx
sudo systemctl status apache2

# Is it listening on the right port?
sudo netstat -tuln | grep :80

# Is the firewall allowing it?
sudo ufw status | grep 80
```

### Issue: UFW Rules Not Persisting
**Solution:**
```bash
# UFW rules should persist automatically
# If not, ensure UFW is enabled on boot
sudo systemctl enable ufw

# Check if UFW is enabled
sudo ufw status
```

---

## Common UFW Commands Reference

```bash
# Installation
sudo apt-get install ufw

# Status
sudo ufw status
sudo ufw status verbose
sudo ufw status numbered

# Enable/Disable
sudo ufw enable
sudo ufw disable

# Default Policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow Rules
sudo ufw allow 22
sudo ufw allow 80/tcp
sudo ufw allow from 192.168.1.100

# Deny Rules
sudo ufw deny 23
sudo ufw deny from 192.168.1.100

# Delete Rules
sudo ufw delete allow 80
sudo ufw delete 2  # by number

# Rate Limiting
sudo ufw limit 22/tcp

# Logging
sudo ufw logging on
sudo ufw logging medium

# Reset
sudo ufw reset

# Reload
sudo ufw reload

# Show listening ports
sudo ufw show listening

# Show raw rules
sudo ufw show raw
```

---

## iptables vs UFW

### iptables (Low-level)
```bash
# iptables syntax (complex)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -j DROP
```

### UFW (High-level)
```bash
# UFW syntax (simple)
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw default deny incoming
```

**Note:** UFW is a frontend for iptables. All UFW rules are translated to iptables rules behind the scenes.

---

## Advanced Configuration

### Application Profiles
```bash
# List available profiles
sudo ufw app list

# Allow by profile
sudo ufw allow 'Nginx Full'
sudo ufw allow 'OpenSSH'

# View profile details
sudo ufw app info 'Nginx Full'
```

### Custom Application Profile
Create `/etc/ufw/applications.d/myapp`:
```ini
[MyApp]
title=My Application
description=My custom application
ports=8000,8001,8002/tcp
```

Then:
```bash
sudo ufw app update MyApp
sudo ufw allow 'MyApp'
```

### IPv6 Support
Edit `/etc/default/ufw`:
```bash
IPV6=yes
```

### Logging Levels
```bash
sudo ufw logging off      # Disable logging
sudo ufw logging low      # Log blocked packets
sudo ufw logging medium   # Log blocked + allowed packets
sudo ufw logging high     # Log all packets + rate limiting
sudo ufw logging full     # Maximum logging
```

---

## Security Checklist

- [ ] UFW is installed and enabled
- [ ] Default policy is deny incoming
- [ ] SSH (22) is allowed
- [ ] HTTP (80) is allowed (if running web server)
- [ ] HTTPS (443) is allowed (if running web server)
- [ ] All unnecessary ports are blocked
- [ ] Rate limiting is enabled on SSH
- [ ] Logging is enabled
- [ ] Rules are documented
- [ ] Backup access method exists
- [ ] Rules tested before production
- [ ] IP forwarding configured (if needed)
- [ ] Rules reviewed regularly

---

## Resources

- [UFW Documentation](https://help.ubuntu.com/community/UFW)
- [UFW Essentials](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)
- [How To Set Up a Firewall with UFW on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04)
- [iptables Tutorial](https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands)
- [Port Forwarding with UFW](https://serverfault.com/questions/238964/can-i-use-ufw-to-setup-a-port-forward)

## Author
This project is part of the ALX Software Engineering Program.

## License
This project is licensed under the terms of the ALX Software Engineering Program.
