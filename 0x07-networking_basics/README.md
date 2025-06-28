# 0x07. Networking basics #0

## Description
This project introduces the fundamental concepts of networking, covering essential topics such as the OSI model, types of networks, MAC and IP addresses, UDP and TCP protocols, and network troubleshooting tools. Through practical exercises and theoretical understanding, you'll gain a solid foundation in computer networking principles.

## Learning Objectives
At the end of this project, you should be able to explain to anyone, without the help of Google:

### OSI Model
- What it is
- How many layers it has
- How it is organized

### What is a LAN
- Typical usage
- Typical geographical size

### What is a WAN
- Typical usage
- Typical geographical size

### What is the Internet
- What is an IP address
- What are the 2 types of IP address
- What is localhost
- What is a subnet
- Why IPv6 was created

### TCP/UDP
- What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
- What is the main difference between TCP and UDP
- What is a port
- Memorize SSH, HTTP and HTTPS port numbers
- What tool/protocol is often used to check if a device is connected to a network

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your Bash script files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `shellcheck` without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

## Tasks

### 0. OSI model
**File:** `0-OSI_model`

What is the OSI model?
1. Set of specifications that network hardware manufacturers must respect
2. The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

How is the OSI model organized?
1. Alphabetically
2. From the lowest to the highest level
3. Randomly

### 1. Types of network
**File:** `1-types_of_network`

What type of network are Holberton iMacs connected to?
1. Internet
2. WAN
3. LAN

What type of network could connect an office in one building to another office in a building a few streets away?
1. Internet
2. WAN
3. LAN

What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?
1. Internet
2. WAN
3. LAN

### 2. MAC and IP address
**File:** `2-MAC_and_IP_address`

What is a MAC address?
1. The name of a network interface
2. The unique identifier of a network interface
3. A network interface

What is an IP address?
1. Is to devices connected to a network what postal address is to houses
2. The unique identifier of a network interface
3. Is a number that network devices use to connect to networks

### 3. UDP and TCP
**File:** `3-UDP_and_TCP`

Which statement is correct for the TCP box:
1. It is a protocol that is transferring data in a slow way but surely
2. It is a protocol that is transferring data in a fast way and might loss data along in the process

Which statement is correct for the UDP box:
1. It is a protocol that is transferring data in a slow way but surely
2. It is a protocol that is transferring data in a fast way and might loss data along in the process

Which statement is correct for the TCP worker:
1. Have you received boxes x, y, z?
2. May I increase the rate at which I am sending you boxes?

### 4. TCP and UDP ports
**File:** `4-TCP_and_UDP_ports`

Write a Bash script that displays listening ports:
- That only shows listening sockets
- That shows the PID and name of the program to which each socket belongs

### 5. Is the host on the network
**File:** `5-is_the_host_on_the_network`

Write a Bash script that pings an IP address passed as an argument:
- Accepts a string as an argument
- Displays `Usage: 5-is_the_host_on_the_network {IP_ADDRESS}` if no argument passed
- Ping the IP 5 times

## Resources
Read or watch:
- [OSI model](https://en.wikipedia.org/wiki/OSI_model)
- [Different types of network](https://www.lifewire.com/lans-wans-and-other-area-networks-817376)
- [LAN network](https://en.wikipedia.org/wiki/Local_area_network)
- [WAN network](https://en.wikipedia.org/wiki/Wide_area_network)
- [Internet](https://en.wikipedia.org/wiki/Internet)
- [MAC address](https://whatismyipaddress.com/mac-address)
- [What is an IP address](https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/)
- [Private and public address](https://www.iplocation.net/public-vs-private-ip-address)
- [IPv4 and IPv6](https://www.webopedia.com/insights/ipv6-ipv4-difference/)
- [Localhost](https://en.wikipedia.org/wiki/Localhost)
- [TCP and UDP](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
- [TCP/UDP ports List](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
- [What is ping /ICMP](https://en.wikipedia.org/wiki/Ping_%28networking_utility%29)
- [Positional parameters](https://wiki.bash-hackers.org/scripting/posparams)

## Key Concepts to Remember

### OSI Model Layers (Bottom to Top)
1. Physical Layer
2. Data Link Layer
3. Network Layer
4. Transport Layer
5. Session Layer
6. Presentation Layer
7. Application Layer

### Important Port Numbers
- SSH: 22
- HTTP: 80
- HTTPS: 443

### Network Types
- **LAN (Local Area Network)**: Small geographical area (home, office, building)
- **WAN (Wide Area Network)**: Large geographical area (cities, countries)
- **Internet**: Global network of networks

### IP Address Types
- **IPv4**: 32-bit addresses (e.g., 192.168.1.1)
- **IPv6**: 128-bit addresses (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
- **Private IP**: Used within local networks
- **Public IP**: Used to identify devices on the internet

## Author
This project is part of the ALX Software Engineering Program.

## Repository
- **GitHub repository:** `alx-system_engineering-devops`
- **Directory:** `0x07-networking_basics`