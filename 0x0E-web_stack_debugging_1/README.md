# 0x0E. Web stack debugging #1

## Description
This is the second project in the Web Stack Debugging series. Building on the skills from debugging #0, you'll tackle more complex issues with Nginx configuration. The goal is to debug why Nginx isn't listening on port 80 and write scripts to automate the fix.

## Concepts
For this project, you should understand:
- **Network basics**
- **Web stack debugging**
- **Nginx configuration**
- **Port management**
- **Process management**

## Background Context
Debugging is a critical skill for any software engineer or system administrator. In this project, you're given a broken web stack and must diagnose and fix the issue. The challenge is not just fixing it manually, but creating an automated solution that can configure any Ubuntu container to meet the requirements.

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file at the root of the folder of the project is mandatory
- All your Bash script files must be executable
- Your Bash scripts must pass `Shellcheck` without any error
- Your Bash scripts must run without error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script does
- You are not allowed to use `wget`

## Tasks

### 0. Nginx likes port 80
**File:** `0-nginx_likes_port_80`

Using your debugging skills, find out what's keeping your Ubuntu container's Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.

**Requirements:**
- Nginx must be running, and listening on port 80 of all the server's active IPv4 IPs
- Write a Bash script that configures a server to the above requirements

**Example:**
```bash
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# ./0-nginx_likes_port_80 > /dev/null 2&>1
root@966c5664b21f:/#
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#
```

---

### 1. Make it sweet and short
**File:** `1-debugging_made_short`

Using what you did for task #0, make your fix short and sweet.

**Requirements:**
- Your Bash script must be 5 lines long or less
- There must be a new line at the end of the file
- You must respect usual Bash script requirements
- You cannot use `;`
- You cannot use `&&`
- You cannot use `wget`
- You cannot execute your previous answer file (Do not include the name of the previous script in this one)
- `service` (init) must say that nginx is not running... for real

**Example:**
```bash
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# cat -e 1-debugging_made_short | wc -l
5
root@966c5664b21f:/# ./1-debugging_made_short
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#
root@966c5664b21f:/# service nginx status
 * nginx is not running
root@966c5664b21f:/#
```

---

## Debugging Process

### Step 1: Access the Container
```bash
# Start the container
docker run -d -ti ubuntu:20.04

# Get container ID
docker ps

# Access the container
docker exec -it <container_id> /bin/bash
```

### Step 2: Install Nginx
```bash
apt-get update
apt-get install -y nginx
```

### Step 3: Diagnose the Problem

#### Check if Nginx is Running
```bash
service nginx status
# or
systemctl status nginx
# or
ps aux | grep nginx
```

#### Check What's Listening on Port 80
```bash
netstat -tuln | grep :80
# or
ss -tuln | grep :80
# or
lsof -i :80
```

#### Check Nginx Configuration
```bash
nginx -t
# or
cat /etc/nginx/sites-enabled/default
```

#### Check Nginx Error Logs
```bash
cat /var/log/nginx/error.log
tail -f /var/log/nginx/error.log
```

#### Check Which Port Nginx is Configured to Listen On
```bash
grep -r "listen" /etc/nginx/
cat /etc/nginx/sites-available/default | grep listen
```

### Step 4: Common Issues and Solutions

#### Issue 1: Nginx Not Running
**Symptom:** `service nginx status` shows nginx is not running

**Solution:**
```bash
service nginx start
# or
systemctl start nginx
```

#### Issue 2: Nginx Listening on Wrong Port
**Symptom:** Nginx is running but not on port 80

**Check Configuration:**
```bash
cat /etc/nginx/sites-enabled/default | grep listen
```

**Fix:**
Edit `/etc/nginx/sites-enabled/default` or `/etc/nginx/sites-available/default`:
```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    # ...
}
```

Then reload:
```bash
nginx -t  # Test configuration
service nginx reload
```

#### Issue 3: Port 80 Already in Use
**Symptom:** Nginx fails to start, logs show "Address already in use"

**Find what's using port 80:**
```bash
lsof -i :80
# or
netstat -tuln | grep :80
```

**Kill the process:**
```bash
kill <PID>
# or forcefully
kill -9 <PID>
```

#### Issue 4: Nginx Site Not Enabled
**Symptom:** Configuration exists but isn't active

**Solution:**
```bash
ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
service nginx reload
```

#### Issue 5: Firewall Blocking Port 80
**Check firewall:**
```bash
ufw status
iptables -L
```

**Allow port 80:**
```bash
ufw allow 80
# or
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

---

## Nginx Basics

### Nginx Configuration Structure

```
/etc/nginx/
├── nginx.conf                 # Main configuration file
├── sites-available/           # Available site configurations
│   └── default
├── sites-enabled/             # Enabled site configurations (symlinks)
│   └── default -> ../sites-available/default
├── conf.d/                    # Additional configuration files
└── modules-enabled/           # Enabled modules
```

### Important Nginx Commands

```bash
# Start Nginx
service nginx start
systemctl start nginx

# Stop Nginx
service nginx stop
systemctl stop nginx

# Restart Nginx
service nginx restart
systemctl restart nginx

# Reload Configuration (no downtime)
service nginx reload
systemctl reload nginx
nginx -s reload

# Test Configuration Syntax
nginx -t

# Check Nginx Version
nginx -v
nginx -V  # Verbose with compile options

# Check Status
service nginx status
systemctl status nginx
```

### Basic Nginx Configuration

```nginx
server {
    # Listen on port 80 for IPv4
    listen 80 default_server;
    
    # Listen on port 80 for IPv6
    listen [::]:80 default_server;
    
    # Server name
    server_name _;
    
    # Document root
    root /var/www/html;
    
    # Default index files
    index index.html index.htm index.nginx-debian.html;
    
    # Location block
    location / {
        try_files $uri $uri/ =404;
    }
}
```

---

## Port Management

### Understanding Ports

**Well-known ports (0-1023):**
- Port 80: HTTP
- Port 443: HTTPS
- Port 22: SSH
- Port 21: FTP

**Registered ports (1024-49151):**
- Used by applications

**Dynamic/Private ports (49152-65535):**
- Temporary ports for client connections

### Checking Port Usage

```bash
# Show all listening ports
netstat -tuln
ss -tuln

# Check specific port
netstat -tuln | grep :80
lsof -i :80

# Show process using port
lsof -i :80 -t  # Shows PID only
ps aux | grep $(lsof -i :80 -t)  # Show full process info
```

### Freeing a Port

```bash
# Find process
lsof -i :80

# Kill gracefully
kill <PID>

# Force kill
kill -9 <PID>

# Kill by name
pkill nginx
killall nginx
```

---

## Script Writing Tips

### For Task 0: Full Solution
Your script should:
1. Install necessary tools if needed
2. Stop any conflicting services
3. Fix Nginx configuration
4. Start Nginx
5. Verify it's listening on port 80

### For Task 1: Minimal Solution (≤5 lines)
Focus on:
1. The absolute minimum commands needed
2. Combining operations where possible
3. No semicolons or `&&` operators
4. Must leave nginx "not running" according to `service nginx status`

**Hint for Task 1:**
The trick is to start nginx directly (not via service) so that `service nginx status` doesn't recognize it as running through the init system.

---

## Testing Your Solution

### Test Inside Container
```bash
# Test with curl
curl localhost:80
curl 0:80
curl 127.0.0.1:80

# Test with telnet
telnet localhost 80

# Check listening ports
netstat -tuln | grep :80
```

### Test from Host Machine
```bash
# Get container IP
docker inspect <container_id> | grep IPAddress

# Test from host
curl <container_ip>:80
```

### Verify Nginx Status
```bash
service nginx status
ps aux | grep nginx
netstat -tuln | grep :80
```

---

## Common Pitfalls

### 1. Not Testing Configuration
Always run `nginx -t` before reloading:
```bash
nginx -t && service nginx reload
```

### 2. Using Wrong Paths
Configuration location varies:
- Ubuntu/Debian: `/etc/nginx/sites-available/`
- CentOS/RHEL: `/etc/nginx/conf.d/`

### 3. Forgetting to Reload
After changing configuration:
```bash
service nginx reload  # Apply changes without downtime
```

### 4. Permission Issues
Nginx needs permission to bind to port 80 (privileged port):
```bash
# Run as root or with sudo
sudo service nginx start
```

### 5. Syntax Errors in Configuration
Always check syntax:
```bash
nginx -t
```

---

## Advanced Debugging

### Enable Debug Logging
Edit `/etc/nginx/nginx.conf`:
```nginx
error_log /var/log/nginx/error.log debug;
```

### Monitor Logs in Real-Time
```bash
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

### Check System Logs
```bash
journalctl -u nginx
journalctl -xe
dmesg | grep nginx
```

### Strace Nginx
```bash
strace -p $(pidof nginx | cut -d' ' -f1)
```

---

## Docker Commands for Testing

```bash
# Start Ubuntu container
docker run -d -it ubuntu:20.04

# List running containers
docker ps

# Execute command in container
docker exec -it <container_id> bash

# Copy script to container
docker cp 0-nginx_likes_port_80 <container_id>:/

# Stop container
docker stop <container_id>

# Remove container
docker rm <container_id>

# Start fresh container
docker run -p 8080:80 -d -it ubuntu:20.04
```

---

## Resources

- [Nginx Documentation](https://nginx.org/en/docs/)
- [Nginx Beginner's Guide](https://nginx.org/en/docs/beginners_guide.html)
- [Debugging Nginx](https://www.nginx.com/blog/debugging-nginx/)
- [Linux Port Management](https://www.cyberciti.biz/faq/unix-linux-check-if-port-is-in-use-command/)
- [Netstat Command](https://www.computerhope.com/unix/unetstat.htm)
- [Systemctl vs Service](https://askubuntu.com/questions/903354/difference-between-systemctl-and-service-commands)

## Tips for Success

1. **Understand the problem first** - Don't just copy solutions
2. **Test incrementally** - Verify each step works
3. **Read error messages** - They usually tell you what's wrong
4. **Use logs** - They contain valuable debugging information
5. **Keep it simple** - The best solution is often the simplest
6. **Automate carefully** - Test your script multiple times
7. **Consider edge cases** - What if nginx is already running?

## Author
This project is part of the ALX Software Engineering Program.

## License
This project is licensed under the terms of the ALX Software Engineering Program.
