# 0x09. Web infrastructure design

## Description
This project focuses on understanding and designing web infrastructure systems. You'll learn about servers, load balancers, databases, monitoring, security, and how these components work together to create scalable and reliable web applications. The emphasis is on system design concepts, high availability, scalability, and security considerations.

## Learning Objectives
At the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
- You must be able to explain what each component is doing
- You must be able to explain system redundancy
- Know all the mentioned acronyms: LAMP, SPOF, QPS

### Concepts to Master
- **DNS**: Domain Name System and how it works
- **Monitoring**: What it is and why it's important
- **Web Server**: Role and functionality
- **Network basics**: Understanding network protocols and communication
- **Load balancer**: Types and distribution algorithms
- **Server**: Physical vs virtual servers, their roles

## Requirements

### General
- A `README.md` file, at the root of the folder of the project, is mandatory
- For each task, once you have completed your whiteboard diagram, take a picture/screenshot of your diagram
- This project will be manually reviewed
- As each task is completed, the name of that task will turn green
- Upload a screenshot, showing that you completed the required levels, to any image hosting service
- For the following questions, insert the link to your screenshot in the answer file
- After pushing your answer file to GitHub, insert the GitHub file link into the URL box

### Whiteboard Requirements
- You will be asked to whiteboard in front of a mentor, staff or student
- You will have 30 minutes to complete the task
- No computer or notes are allowed during the whiteboarding session
- Focus on what you are asked
- Cover what the requirements mention, it is fine to ask questions
- Keep in mind that you will have 30 minutes for 3 tasks, so 10 minutes per task

## Tasks

### 0. Simple web stack
**File:** `0-simple_web_stack`

A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a LAMP stack.

On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via `www.foobar.com`. Start your explanation by having a user wanting to access your website.

Requirements:
- You must use:
  - 1 server
  - 1 web server (Nginx)
  - 1 application server
  - 1 application files (your code base)
  - 1 database (MySQL)
  - 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

You must be able to explain:
- What is a server
- What is the role of the domain name
- What type of DNS record www is in www.foobar.com
- What is the role of the web server
- What is the role of the application server
- What is the role of the database
- What is the server using to communicate with the computer of the user requesting the website

Issues with this infrastructure:
- SPOF (Single Point of Failure)
- Downtime when maintenance needed (like deploying new code web server needs to be restarted)
- Cannot scale if too much incoming traffic

### 1. Distributed web infrastructure
**File:** `1-distributed_web_infrastructure`

On a whiteboard, design a three server web infrastructure that hosts the website `www.foobar.com`.

Requirements:
- You must add:
  - 2 servers
  - 1 web server (Nginx)
  - 1 application server
  - 1 load-balancer (HAproxy)
  - 1 set of application files (your code base)
  - 1 database (MySQL)

You must be able to explain:
- For every additional element, why you are adding it
- What distribution algorithm your load balancer is configured with and how it works
- Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
- How a database Primary-Replica (Master-Slave) cluster works
- What is the difference between the Primary node and the Replica node in regard to the application

Issues with this infrastructure:
- Where are the SPOF
- Security issues (no firewall, no HTTPS)
- No monitoring

### 2. Secured and monitored web infrastructure
**File:** `2-secured_and_monitored_web_infrastructure`

On a whiteboard, design a three server web infrastructure that hosts the website `www.foobar.com`, it must be secured, serve encrypted traffic, and be monitored.

Requirements:
- You must add:
  - 3 firewalls
  - 1 SSL certificate to serve www.foobar.com over HTTPS
  - 3 monitoring clients (data collector for Sumologic or other monitoring services)

You must be able to explain:
- For every additional element, why you are adding it
- What are firewalls for
- Why is the traffic served over HTTPS
- What monitoring is used for
- How the monitoring tool is collecting data
- Explain what to do if you want to monitor your web server QPS

Issues with this infrastructure:
- Why terminating SSL at the load balancer level is an issue
- Why having only one MySQL server capable of accepting writes is an issue
- Why having servers with all the same components (database, web server and application server) might be a problem

### 3. Scale up
**File:** `3-scale_up`

Readme
- [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)

Requirements:
- You must add:
  - 1 server
  - 1 load-balancer (HAproxy) configured as cluster with the other one
  - Split components (web server, application server, database) with their own server

You must be able to explain:
- For every additional element, why you are adding it

The application server vs web server concept is important here; the idea is that to avoid SPOF, you want to have redundant server of each type: web server, application server, database server.

## Key Concepts and Definitions

### LAMP Stack
- **L**inux (Operating System)
- **A**pache/Nginx (Web Server)
- **M**ySQL (Database)
- **P**HP/Python/Perl (Programming Language)

### Important Acronyms
- **SPOF**: Single Point of Failure - A part of a system that, if it fails, will stop the entire system from working
- **QPS**: Queries Per Second - A measure of how much traffic a server can handle
- **DNS**: Domain Name System - Translates domain names to IP addresses
- **HTTP/HTTPS**: HyperText Transfer Protocol (Secure) - Protocol for web communication
- **SSL/TLS**: Secure Sockets Layer/Transport Layer Security - Encryption protocols

### Load Balancer Distribution Algorithms
1. **Round Robin**: Requests distributed sequentially across servers
2. **Least Connections**: Directs traffic to server with fewest active connections
3. **IP Hash**: Routes based on client IP hash
4. **Weighted Round Robin**: Assigns different weights to servers based on capacity

### Active-Active vs Active-Passive
- **Active-Active**: All servers handle traffic simultaneously, providing better resource utilization
- **Active-Passive**: One server handles traffic while others remain on standby, simpler but less efficient

### Database Clustering
- **Primary (Master)**: Handles write operations and replicates data
- **Replica (Slave)**: Handles read operations and receives data from primary
- **Benefits**: Improved read performance, data redundancy, load distribution

## Infrastructure Components

### Server Types
- **Web Server**: Serves static content, handles HTTP requests (Nginx, Apache)
- **Application Server**: Executes application logic, processes dynamic content
- **Database Server**: Stores and manages data (MySQL, PostgreSQL)
- **Load Balancer**: Distributes incoming requests across multiple servers

### Security Components
- **Firewall**: Filters network traffic based on security rules
- **SSL Certificate**: Enables HTTPS encryption for secure communication
- **VPN**: Secure connection for remote access

### Monitoring and Logging
- **Monitoring Tools**: Datadog, New Relic, Sumologic, Nagios
- **Metrics to Monitor**:
  - Server performance (CPU, memory, disk)
  - Application performance (response time, error rates)
  - Network metrics (bandwidth, latency)
  - Database performance (query time, connections)

## Common Issues and Solutions

### Single Points of Failure
- **Problem**: One component failure brings down entire system
- **Solution**: Implement redundancy at every level

### Scalability Issues
- **Vertical Scaling**: Adding more power to existing servers
- **Horizontal Scaling**: Adding more servers to handle load

### Security Concerns
- **SSL Termination**: Where encryption/decryption happens
- **Network Segmentation**: Isolating different components
- **Access Control**: Limiting who can access what resources

### Performance Optimization
- **Caching**: Store frequently accessed data in memory
- **CDN**: Distribute static content globally
- **Database Optimization**: Indexing, query optimization, connection pooling

## Best Practices

### Design Principles
1. **Redundancy**: Eliminate single points of failure
2. **Scalability**: Design for growth
3. **Security**: Implement defense in depth
4. **Monitoring**: Observe system health and performance
5. **Automation**: Reduce manual intervention

### Infrastructure as Code
- Version control infrastructure configurations
- Automate deployment and scaling
- Ensure consistency across environments

### Disaster Recovery
- Regular backups
- Geographic distribution
- Recovery time objectives (RTO)
- Recovery point objectives (RPO)

## Tools and Technologies

### Load Balancers
- **HAProxy**: High availability proxy and load balancer
- **Nginx**: Can function as both web server and load balancer
- **AWS ELB**: Amazon's Elastic Load Balancer
- **Cloudflare**: Global load balancing and CDN

### Monitoring Solutions
- **Datadog**: Cloud monitoring and analytics
- **New Relic**: Application performance monitoring
- **Sumologic**: Log management and analytics
- **Prometheus + Grafana**: Open-source monitoring stack

### Security Tools
- **Let's Encrypt**: Free SSL certificates
- **iptables**: Linux firewall utility
- **fail2ban**: Intrusion prevention system

## Resources
Read or watch:
- [Network basics concept page](https://intranet.alxswe.com/concepts/33)
- [Server concept page](https://intranet.alxswe.com/concepts/67)
- [Web server concept page](https://intranet.alxswe.com/concepts/17)
- [DNS concept page](https://intranet.alxswe.com/concepts/12)
- [Load balancer concept page](https://intranet.alxswe.com/concepts/46)
- [Monitoring concept page](https://intranet.alxswe.com/concepts/13)
- [What is a database](https://www.oracle.com/database/what-is-database/)
- [What's the difference between a web server and an app server?](https://www.infoworld.com/article/2077354/app-server-web-server-what-s-the-difference.html)
- [DNS record types](https://kb.pressable.com/article/dns-record-types-explained/)
- [Single point of failure](https://en.wikipedia.org/wiki/Single_point_of_failure)
- [How to avoid downtime when deploying new code](https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt)
- [High availability cluster (active-active/active-passive)](https://docs.oracle.com/cd/A91202_01/901_doc/rac.901/a89867/pshavdtl.htm)
- [What is HTTPS](https://www.instantssl.com/http-vs-https)
- [What is a firewall](https://www.webopedia.com/definitions/firewall/)

## File Structure
```
0x09-web_infrastructure_design/
├── README.md
├── 0-simple_web_stack
├── 1-distributed_web_infrastructure
├── 2-secured_and_monitored_web_infrastructure
└── 3-scale_up
```


## Submission Guidelines
1. Create whiteboard diagrams for each task
2. Take clear screenshots of your diagrams
3. Upload screenshots to an image hosting service
4. Insert the image URLs into the respective answer files
5. Push your answer files to GitHub
6. Insert GitHub file links into the submission form

## Author
This project is part of the ALX Software Engineering Program.

## Repository
- **GitHub repository:** `alx-system_engineering-devops`
- **Directory:** `0x09-web_infrastructure_design`