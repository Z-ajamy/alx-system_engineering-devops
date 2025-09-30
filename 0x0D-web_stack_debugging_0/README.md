# 0x0D. Web stack debugging #0

## Description
This project is an introduction to the Web Stack Debugging series. In this debugging exercise, you'll learn how to diagnose and fix issues in a web stack. The goal is to get Apache running inside a Docker container and serving a page when querying the root of the server.

Web stack debugging is a crucial skill for DevOps engineers and system administrators. This series will train you to identify and resolve common web server issues quickly and efficiently.

## Concepts
For this project, you should understand the following concepts:
- **Network basics**
- **Docker**
- **Web stack debugging**

## Background Context
The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that's the "fun" part of the job!).

Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.

In this debugging series, broken/bugged webstacks will be given to you, and the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash scripts must pass `Shellcheck` without any error
- Your Bash scripts must run without error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script does

## Installing Docker

For this project, you will be given a container which you can use to solve the task. If you would like to have Docker so that you can experiment with it and/or solve this problem locally, you can install it on your machine, your Ubuntu 14.04 VM, or your Ubuntu 16.04 VM if you upgraded.

### Installation Instructions

#### Mac OS
- [Install Docker for Mac](https://docs.docker.com/docker-for-mac/)

#### Windows
- [Install Docker for Windows](https://docs.docker.com/docker-for-windows/)

#### Ubuntu 14.04
```bash
$ sudo apt-get update
$ sudo apt-get install docker.io
$ sudo service docker start
```

#### Ubuntu 16.04 and Higher
```bash
$ sudo apt-get update
$ sudo apt-get install docker-ce
$ sudo service docker start
```

## Tasks

### 0. Give me a page! (mandatory)

**File:** `0-give_me_a_page`

In this first debugging project, you need to get Apache to run on a Docker container and return a page containing "Hello Holberton" when querying the root of it.

#### Example
```bash
$ docker run -p 8080:80 -d -it holbertonschool/265-0
47b3566546a9b9b0bbdc8de5e7dd8f4b6b1b1c6e1b1b1c6e1b1b1c6e1b1b1c6e

$ docker ps
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47b3566546a9        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla

$ curl 0:8080
curl: (52) Empty reply from server

# After debugging and running your script:
$ curl 0:8080
Hello Holberton
```

#### Task Requirements
- Write a Bash script that fixes the container
- After connecting to the container and fixing the issue, the script should:
  - Start the Apache service
  - Ensure Apache is running and serving content on port 80
  - The page should return "Hello Holberton" when querying the root

## Debugging Process

### Step 1: Access the Container
```bash
# Get the container ID
$ docker ps

# Execute bash in the container
$ docker exec -ti <container_id> /bin/bash
```

### Step 2: Diagnose the Problem
Common checks to perform:
- Is Apache installed? (`which apache2` or `which httpd`)
- Is Apache running? (`service apache2 status`)
- Is Apache configured correctly? (check `/etc/apache2/` or `/etc/httpd/`)
- Are there any error logs? (`/var/log/apache2/error.log`)
- Is the correct content in the web root? (`/var/www/html/`)

### Step 3: Fix the Issue Manually
Test your fixes manually before scripting them.

### Step 4: Create the Bash Script
Once you know what fixes the issue, create a script that automates the solution.

## Solution Approach

Your script should:
1. Start the Apache service
2. Ensure it's configured to serve on port 80
3. Verify the content exists in the web root
4. Handle any necessary permissions or configuration issues

## Testing

### Test with Docker
```bash
# Start the container
$ docker run -p 8080:80 -d -it holbertonschool/265-0

# Get container ID
$ docker ps

# Run your debugging script inside the container
$ docker exec -ti <container_id> /bin/bash
root@container:/# ./0-give_me_a_page

# Test from your host machine
$ curl 0:8080
Hello Holberton
```

## Common Issues in Web Stack Debugging

1. **Service not running** - The web server process isn't started
2. **Wrong port** - Server listening on wrong port
3. **Permission issues** - Files or directories have incorrect permissions
4. **Configuration errors** - Server configuration files have syntax errors
5. **Missing content** - The index file doesn't exist or is in the wrong location
6. **Firewall rules** - Port is blocked by firewall

## Tips

- Always check if the service is running first
- Read error logs - they often tell you exactly what's wrong
- Test changes incrementally
- Use `curl` to test from inside and outside the container
- Check file permissions with `ls -la`
- Verify configuration syntax before restarting services

## Resources

- [Docker Documentation](https://docs.docker.com/)
- [Apache HTTP Server Documentation](https://httpd.apache.org/docs/)
- [curl man page](https://curl.se/docs/manpage.html)
- [Docker exec command](https://docs.docker.com/engine/reference/commandline/exec/)
- [Debugging](https://en.wikipedia.org/wiki/Debugging)

## Author
This project is part of the ALX Software Engineering Program.

## License
This project is licensed under the terms of the ALX Software Engineering Program.
