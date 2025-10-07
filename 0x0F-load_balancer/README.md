# 0x0F. Load balancer

## Description
This project introduces the concept of load balancing and redundancy in web infrastructure. You'll learn how to configure HAProxy as a load balancer to distribute traffic across multiple web servers, improving the reliability and scalability of your web stack. Additionally, you'll configure custom HTTP headers to track which server handled a request.

## Concepts
For this project, you should understand:
- **Load balancing**
- **Web stack debugging**
- **HTTP headers**
- **Redundancy**
- **High availability**

## Background Context
You have been given 2 additional servers:
- `gc-[STUDENT_ID]-web-02-XXXXXXXXXX`
- `gc-[STUDENT_ID]-lb-01-XXXXXXXXXX`

Let's improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

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

### 0. Double the number of webservers
**File:** `0-custom_http_response_header`

In this first task you need to configure `web-02` to be identical to `web-01`. Fortunately, you built a Bash script during your web server project, and they'll now come in handy to easily configure `web-02`. Remember, always try to automate your work!

Since we're placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.

**Requirements:**
- Configure Nginx so that its HTTP response contains a custom header (on `web-01` and `web-02`)
  - The name of the custom HTTP header must be `X-Served-By`
  - The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write `0-custom_http_response_header` so that it configures a brand new Ubuntu machine to the requirements asked in this task
  - Ignore SC2154 for `shellcheck`

**Example:**
```bash
$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01

$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
```

If your server's hostnames are not properly configured (`[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`), follow this tutorial.

---

### 1. Install your load balancer
**File:** `1-install_load_balancer`

Install and configure HAProxy on your `lb-01` server.

**Requirements:**
- Configure HAProxy to send traffic to `web-01` and `web-02`
- Distribute requests using a roundrobin algorithm
- Make sure that HAProxy can be managed via an init script
- Make sure that your servers are configured with the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`. If not, follow this tutorial.
- For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements

**Example:**
```bash
$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:17 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:19 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
X-Served-By: 03-web-02
Accept-Ranges: bytes
```

---

## Load Balancing Concepts

### What is a Load Balancer?
A load balancer is a device or software that distributes network or application traffic across multiple servers. It acts as a reverse proxy and helps ensure no single server bears too much demand, improving:
- **Availability** - If one server fails, traffic is redirected to remaining servers
- **Scalability** - Easy to add more servers as demand increases
- **Performance** - Distributes load evenly across servers

### Load Balancing Algorithms

#### 1. Round Robin
- Distributes requests sequentially across all servers
- Simple and fair distribution
- Default algorithm used in this project

#### 2. Least Connections
- Sends requests to the server with fewest active connections
- Good for varying request processing times

#### 3. IP Hash
- Uses client's IP address to determine which server receives request
- Ensures same client always reaches same server

#### 4. Weighted Round Robin
- Assigns different weights to servers based on capacity
- More powerful servers receive more requests

### HAProxy
HAProxy (High Availability Proxy) is a free, open-source load balancer and proxy server for TCP and HTTP applications. It's known for:
- High performance
- Reliability
- Low resource usage
- Advanced load balancing algorithms

## HAProxy Configuration

### Basic HAProxy Configuration Structure

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

defaults
    log     global
    mode    http
    option  httplog
    option  dontlognull
    timeout connect 5000
    timeout client  50000
    timeout server  50000

frontend http_front
    bind *:80
    stats uri /haproxy?stats
    default_backend http_back

backend http_back
    balance roundrobin
    server web-01 [WEB-01-IP]:80 check
    server web-02 [WEB-02-IP]:80 check
```

### Key Configuration Sections

#### Global Section
- Sets process-wide parameters
- Logging configuration
- Security settings

#### Defaults Section
- Default settings for all sections
- Timeout values
- Logging options

#### Frontend Section
- Defines how requests are forwarded to backends
- Specifies listening port and IP
- Can define ACLs (Access Control Lists)

#### Backend Section
- Defines servers that handle requests
- Specifies load balancing algorithm
- Health check configuration

## Nginx Custom Header Configuration

To add a custom header in Nginx, modify your server block:

```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    add_header X-Served-By $hostname;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

The `add_header X-Served-By $hostname;` directive adds the custom header with the server's hostname.

## Installation and Configuration

### Installing HAProxy
```bash
sudo apt-get update
sudo apt-get install -y haproxy
```

### Enabling HAProxy Init Script
Edit `/etc/default/haproxy`:
```bash
ENABLED=1
```

### Configuring HAProxy
Edit `/etc/haproxy/haproxy.cfg`:
```bash
# Add frontend and backend configuration
```

### Starting HAProxy
```bash
sudo service haproxy start
# or
sudo systemctl start haproxy
```

### Checking HAProxy Status
```bash
sudo service haproxy status
```

### Restarting HAProxy
```bash
sudo service haproxy restart
```

## Testing Your Load Balancer

### Test Round Robin Distribution
```bash
# Multiple requests should alternate between servers
$ curl -sI http://[LB-IP] | grep X-Served-By
X-Served-By: 03-web-01

$ curl -sI http://[LB-IP] | grep X-Served-By
X-Served-By: 03-web-02

$ curl -sI http://[LB-IP] | grep X-Served-By
X-Served-By: 03-web-01
```

### Test with Multiple Requests
```bash
# Bash loop to send multiple requests
for i in {1..10}; do curl -sI http://[LB-IP] | grep X-Served-By; done
```

### Check HAProxy Stats Page
If you configured the stats page:
```bash
http://[LB-IP]/haproxy?stats
```

## Debugging Tips

### Check HAProxy Configuration Syntax
```bash
sudo haproxy -c -f /etc/haproxy/haproxy.cfg
```

### View HAProxy Logs
```bash
sudo tail -f /var/log/haproxy.log
```

### Check if HAProxy is Listening
```bash
sudo netstat -tuln | grep :80
```

### Test Backend Servers Directly
```bash
curl -I http://[WEB-01-IP]
curl -I http://[WEB-02-IP]
```

### Verify Nginx Custom Header
```bash
curl -I http://[WEB-SERVER-IP] | grep X-Served-By
```

## High Availability Considerations

### Active-Passive vs Active-Active

**Active-Passive:**
- One load balancer active, one standby
- Standby takes over if active fails
- Requires heartbeat monitoring

**Active-Active:**
- Multiple load balancers handle traffic simultaneously
- Better resource utilization
- More complex setup

### Health Checks
HAProxy performs regular health checks on backend servers:
- If a server fails health check, traffic is not sent to it
- Automatic failover to healthy servers
- Automatic recovery when server becomes healthy again

## Security Considerations

1. **Firewall Rules** - Only allow necessary ports
2. **SSL/TLS Termination** - HAProxy can handle HTTPS
3. **Rate Limiting** - Prevent DDoS attacks
4. **Access Control Lists** - Restrict access to admin interfaces
5. **Regular Updates** - Keep HAProxy and web servers patched

## Common Issues and Solutions

### Issue: HAProxy won't start
**Solution:** Check configuration syntax and logs

### Issue: Traffic not distributed evenly
**Solution:** Verify roundrobin algorithm is configured

### Issue: Custom header not appearing
**Solution:** Check Nginx configuration and reload service

### Issue: Backend server unreachable
**Solution:** Verify firewall rules and server status

## Resources

- [Introduction to load-balancing and HAProxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HAProxy Documentation](http://www.haproxy.org/#docs)
- [HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)
- [Load Balancing Algorithms](https://kemptechnologies.com/load-balancer/load-balancing-algorithms-techniques)
- [High Availability](https://en.wikipedia.org/wiki/High_availability)

## Author
This project is part of the ALX Software Engineering Program.

## License
This project is licensed under the terms of the ALX Software Engineering Program.
