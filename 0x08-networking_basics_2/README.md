# 0x08. Networking basics #1

## Description
This project builds upon the fundamental networking concepts from the previous project, diving deeper into practical networking skills. You'll learn about localhost, network interfaces, host files, and network configuration commands. The focus is on hands-on experience with network troubleshooting and configuration tools.

## Learning Objectives
At the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- What is localhost/127.0.0.1
- What is 0.0.0.0
- What is `/etc/hosts`
- How to display your machine's active network interfaces

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (version 0.7.0 via `apt-get`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

## Tasks

### 0. Change your home IP
**File:** `0-change_your_home_IP`

Write a Bash script that configures an Ubuntu server with the below requirements:
- `localhost` resolves to `127.0.0.2`
- `facebook.com` resolves to `8.8.8.8`

**Requirements:**
- The checker is running on Docker, so make sure to read the Docker concept page
- In this example, we're only showing the commands to run, but you could also configure your machine in the same way

**Example:**
```bash
sylvain@ubuntu$ ping localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.012 ms
^C
--- localhost ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.012/0.012/0.012/0.000 ms

sylvain@ubuntu$ ping facebook.com
PING facebook.com (157.240.11.35) 56(84) bytes of data.
64 bytes from edge-star-mini-shv-02-lax3.facebook.com (157.240.11.35): icmp_seq=1 ttl=63 time=15.4 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 15.432/15.432/15.432/0.000 ms

sylvain@ubuntu$ sudo ./0-change_your_home_IP
sylvain@ubuntu$ ping localhost
PING localhost (127.0.0.2) 56(84) bytes of data.
64 bytes from localhost (127.0.0.2): icmp_seq=1 ttl=64 time=0.012 ms
^C
--- localhost ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.012/0.012/0.012/0.000 ms

sylvain@ubuntu$ ping facebook.com
PING facebook.com (8.8.8.8) 56(84) bytes of data.
64 bytes from facebook.com (8.8.8.8): icmp_seq=1 ttl=63 time=8.06 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 8.065/8.065/8.065/0.000 ms
```

In this example, we can see that:
- Before running the script: `localhost` resolves to `127.0.0.1` and `facebook.com` resolves to `157.240.11.35`
- After running the script: `localhost` resolves to `127.0.0.2` and `facebook.com` resolves to `8.8.8.8`

If you're running this script on a machine that you'll continue to use, be sure to revert localhost to `127.0.0.1`. Otherwise, a lot of things will stop working!

### 1. Show attached IPs
**File:** `1-show_attached_IPs`

Write a Bash script that displays all active IPv4 IPs on the machine it's executed on.

**Example:**
```bash
sylvain@ubuntu$ ./1-show_attached_IPs | cat -n
     1  10.0.2.15
     2  127.0.0.1
```

Obviously, the IPs displayed may be different depending on which machine you are running the script on.

Note that we can see our `localhost` IP `127.0.0.1` :)

### 2. Port listening on localhost
**File:** `100-port_listening_on_localhost`

Write a Bash script that listens on port 98 on localhost.

**Terminal 0**
Starting my script:
```bash
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
```

**Terminal 1**
Connecting to localhost on port 98 using telnet and typing some text:
```bash
sylvain@ubuntu$ telnet localhost 98
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Hello world
test
```

**Terminal 0**
Receiving the text on the other side:
```bash
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
Hello world
test
```

For the checker, just use for 10 seconds. The checker will connect to your port, send you a message and check if you received it.

## Key Concepts

### Localhost (127.0.0.1)
- **Localhost** is a hostname that refers to the current computer used to access it
- **127.0.0.1** is the standard IPv4 loopback address
- It's used to establish an IP connection to the same machine or computer being used by the end-user
- Also known as the loopback address

### 0.0.0.0
- **0.0.0.0** is a non-routable meta-address used to designate an invalid, unknown, or non-applicable target
- In the context of servers, 0.0.0.0 means "all IPv4 addresses on the local machine"
- Used when binding a service to all available network interfaces

### /etc/hosts File
- The `/etc/hosts` file is a computer file used by an operating system to map hostnames to IP addresses
- It's a plain text file that associates IP addresses with hostnames, one line per IP address
- The hosts file is one of several system facilities that assists in addressing network nodes
- Format: `IP_ADDRESS hostname [alias...]`

### Network Interface Commands
- **ifconfig**: Configure network interface parameters (legacy command)
- **ip**: Show/manipulate routing, network devices, interfaces and tunnels (modern command)
- **hostname**: Display or set system hostname
- **netstat**: Display network connections, routing tables, interface statistics

## Common Network Commands

### Display Network Interfaces
```bash
# Using ip command (modern)
ip addr show
ip -4 addr show  # IPv4 only

# Using ifconfig (legacy)
ifconfig
ifconfig -a
```

### Test Network Connectivity
```bash
# Ping a host
ping hostname
ping -c 4 hostname  # Send 4 packets only

# Test port connectivity
telnet hostname port
nc -zv hostname port  # Using netcat
```

### Listen on a Port
```bash
# Using netcat
nc -l port_number

# Using netcat with specific interface
nc -l -s localhost port_number
```

## File Structure
```
0x08-networking_basics_2/
├── README.md
├── 0-change_your_home_IP
├── 1-show_attached_IPs
└── 100-port_listening_on_localhost
```

## Resources
Read or watch:
- [What is localhost](https://en.wikipedia.org/wiki/Localhost)
- [What is 0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0)
- [What is the hosts file](https://www.makeuseof.com/tag/modify-manage-hosts-file-linux/)
- [Netcat examples](https://www.varonis.com/blog/netcat-commands/)

## Tips and Best Practices

### Working with /etc/hosts
- Always backup the original file before making changes: `sudo cp /etc/hosts /etc/hosts.backup`
- Use proper format: `IP_ADDRESS hostname [alias...]`
- Be careful with localhost modifications as they can break system functionality
- The hosts file takes precedence over DNS resolution

### Network Troubleshooting
- Use `ping` to test basic connectivity
- Use `telnet` or `nc` to test specific ports
- Check listening ports with `netstat -tulpn` or `ss -tulpn`
- Verify network interfaces with `ip addr` or `ifconfig`

### Security Considerations
- Be cautious when binding services to 0.0.0.0 as it exposes the service to all network interfaces
- Always revert system changes after testing
- Use `sudo` carefully when modifying system configuration files

## Author
This project is part of the ALX Software Engineering Program.

## Repository
- **GitHub repository:** `alx-system_engineering-devops`
- **Directory:** `0x08-networking_basics_2`