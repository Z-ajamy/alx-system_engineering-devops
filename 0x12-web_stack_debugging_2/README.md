# 0x12. Web stack debugging #2

## Description
This is the third project in the Web Stack Debugging series. In this project, you'll focus on user privileges and permissions in Unix/Linux systems. You'll learn how to run processes with different user accounts and fix permission-related issues that prevent web servers from functioning correctly. This project emphasizes the importance of the principle of least privilege in security.

## Concepts
For this project, you should understand:
- **Linux/Unix user accounts**
- **File permissions and ownership**
- **Process management**
- **Sudo and privilege escalation**
- **Web server security best practices**

## Background Context
In production environments, it's a security best practice to run web servers with minimal privileges. Running services as the root user is a security risk because if the service is compromised, the attacker gains root access to the entire system.

In this project, you'll debug why certain services aren't running with the correct user and fix permission issues that arise from improper user configurations.

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
- Cannot use `apt-get` to install a package (use already installed packages)

## Tasks

### 0. Run software as another user
**File:** `0-iamsomeoneelse`

The user `root` is executing a Bash script `/tmp/test_as_me.sh`. You need to create a Bash script that runs this script as the user `nobody`.

**Requirements:**
- Write a Bash script that executes the file `/tmp/test_as_me.sh` as the user `nobody`
- The script should have no more than 5 lines
- You cannot use `su`, `sudo`, or any other user switching commands directly on the script file

**Example:**
```bash
root@d15b0259e66d:/tmp# whoami
root
root@d15b0259e66d:/tmp# cat test_as_me.sh
#!/bin/bash
whoami
root@d15b0259e66d:/tmp# ./0-iamsomeoneelse
nobody
root@d15b0259e66d:/tmp# cat 0-iamsomeoneelse
#!/usr/bin/env bash
# Run the test script as the nobody user
sudo -u nobody bash /tmp/test_as_me.sh
```

---

### 1. Run Nginx as Nginx
**File:** `1-run_nginx_as_nginx`

Currently, Nginx is running as the `root` user, which is a security vulnerability. You need to fix this by making Nginx run as the `nginx` user.

**Requirements:**
- Write a Bash script that fixes the issue so that Nginx is running as the `nginx` user
- Nginx must be running
- Nginx must be listening on all active IPv4 IPs on port 80
- You cannot use `apt-get` to install packages
- The script should have no more than 5 lines
- After running your script, the container should have no processes running as `root` (except for the `init` process and your script itself)

**Example:**
```bash
root@d15b0259e66d:/# ps aux | grep -i nginx
root      12853  0.0  0.0  77360  2744 ?        Ss   19:26   0:00 nginx: master process /usr/sbin/nginx -g daemon off;
root      12854  0.0  0.1  77932  4928 ?        S    19:26   0:00 nginx: worker process
root@d15b0259e66d:/#
root@d15b0259e66d:/# ./1-run_nginx_as_nginx
root@d15b0259e66d:/#
root@d15b0259e66d:/# ps aux | grep -i nginx
nginx    12858  0.0  0.0  77360  2768 ?        Ss   19:26   0:00 nginx: master process /usr/sbin/nginx -g daemon off;
nginx    12859  0.0  0.1  77932  4904 ?        S    19:26   0:00 nginx: worker process
root@d15b0259e66d:/#
```

---

## Linux Users and Permissions

### User Concepts

#### User Types

**1. System Users**
- Created by the system
- Used to run services and daemons
- UIDs typically below 1000 (on many systems)
- Examples: www-data, nginx, mysql, postgres

**2. Regular Users**
- Created by administrators
- Used by humans to log in
- UIDs typically 1000 and above
- Examples: ubuntu, john, alice

**3. Root User**
- System administrator account
- UID 0
- Has all privileges
- Should be used sparingly

#### Special Users

**nobody**
- Unprivileged system user
- Used for services that need minimal privileges
- UID typically 65534
- Often used as a fallback user

**nginx/www-data**
- Used to run web servers
- Allows web server to access web files
- Cannot access sensitive system files
- Provides sandboxing

### Viewing User Information

```bash
# Current user
whoami

# Current user details
id

# All users
cat /etc/passwd

# User details for specific user
getent passwd nginx
getent passwd nobody

# Specific format
id -u nginx        # UID
id -g nginx        # GID
id -g -n nginx     # Group name

# Check user groups
groups nginx
id -G nginx
```

---

## Running Commands as Different Users

### Using `sudo`

#### Basic Syntax
```bash
sudo -u <username> <command>
```

#### Examples
```bash
# Run command as specific user
sudo -u nobody whoami

# Run script as specific user
sudo -u nginx bash /path/to/script.sh

# Run with shell specification
sudo -u www-data /bin/bash -c "whoami"

# Preserve environment
sudo -u nginx -E command

# Run as group
sudo -g groupname command
```

### Using `sudo` with Scripts

```bash
#!/usr/bin/env bash
# Example: Run test script as nobody

sudo -u nobody bash /tmp/test_as_me.sh
```

### Using `su` (Alternative)

```bash
# Switch to user (requires password)
su - nginx

# Run command as user without switching
su -s /bin/bash -c 'whoami' nginx
```

---

## Nginx User Configuration

### Default Nginx Configuration

Nginx user is typically defined in the main configuration file:

**Location:** `/etc/nginx/nginx.conf`

```nginx
# /etc/nginx/nginx.conf

user nginx;  # <- This line specifies the user
worker_processes auto;
pid /run/nginx.pid;

events {
    worker_connections 768;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Rest of configuration...
}
```

### Changing Nginx User

#### Step 1: Edit Configuration
```bash
sudo nano /etc/nginx/nginx.conf
```

Change:
```nginx
user root;
```

To:
```nginx
user nginx;
```

#### Step 2: Test Configuration
```bash
sudo nginx -t
```

#### Step 3: Reload Nginx
```bash
sudo service nginx reload
# or
sudo systemctl reload nginx
```

### Ensuring Nginx User Exists

```bash
# Check if nginx user exists
getent passwd nginx

# Create nginx user if it doesn't exist
sudo useradd -r -s /bin/false nginx
```

### File Permissions for Web Files

Nginx running as `nginx` user needs appropriate permissions:

```bash
# Typical web root permissions
sudo chown -R nginx:nginx /var/www/html
sudo chmod -R 755 /var/www/html

# More restrictive permissions
sudo chown -R nginx:nginx /var/www/html
sudo chmod -R 750 /var/www/html
sudo chmod 644 /var/www/html/*
```

---

## Process Management and Privileges

### Viewing Running Processes

```bash
# List all processes with user
ps aux

# Filter for specific process
ps aux | grep nginx

# Show process with user
ps -eo user,pid,cmd | grep nginx

# Show process tree
pstree -a -p | grep nginx
```

### Understanding `ps aux` Output

```
USER       PID %CPU %MEM  VSZ  RSS TTY STAT START TIME COMMAND
root      1234  0.0  0.1 77360 2744 ?   Ss  19:26 0:00 nginx: master process
nginx     1235  0.0  0.1 77932 4928 ?   S   19:26 0:00 nginx: worker process
```

- **USER**: User running the process
- **PID**: Process ID
- **%CPU**: CPU usage percentage
- **%MEM**: Memory usage percentage
- **VSZ**: Virtual memory size (KB)
- **RSS**: Resident set size (KB)
- **STAT**: Process state (Ss=session leader sleep, S=sleep, R=running)
- **COMMAND**: Command that started the process

### Killing and Restarting Nginx

```bash
# Graceful restart (reload config)
sudo service nginx reload
sudo systemctl reload nginx

# Full restart
sudo service nginx restart
sudo systemctl restart nginx

# Graceful stop
sudo service nginx stop
sudo systemctl stop nginx

# Force kill all nginx processes
sudo pkill -9 nginx
```

---

## Security: Principle of Least Privilege

### Why Not Run Services as Root?

**Security Risks:**
- If the service is compromised, attacker gets root access
- Can modify system files, install backdoors, etc.
- Can access sensitive data from other services
- Can interfere with system stability

### Best Practices

#### 1. Create Service-Specific Users
```bash
# Each service has its own user
sudo useradd -r -s /bin/false nginx
sudo useradd -r -s /bin/false mysql
sudo useradd -r -s /bin/false postgresql
```

#### 2. Assign Minimal Permissions
```bash
# Only allow access to necessary files/directories
sudo chown nginx:nginx /var/www/html
sudo chmod 750 /var/www/html
```

#### 3. Use System Users
```bash
# Create system user (not for login)
sudo useradd -r -s /bin/false nginx
# -r: system user
# -s /bin/false: no login shell
```

#### 4. Separate Web and System Files
```bash
# Web files (accessible by nginx)
sudo chown nginx:nginx /var/www/html
sudo chmod 755 /var/www/html

# System files (not accessible by nginx)
sudo chown root:root /etc/nginx/nginx.conf
sudo chmod 644 /etc/nginx/nginx.conf
```

---

## Sudo Configuration

### Basic Sudo Rules

Edit `/etc/sudoers` using `visudo`:

```bash
sudo visudo
```

#### Allow User to Run Commands as Another User

```bash
# Allow ubuntu user to run any command as nginx user
ubuntu ALL=(nginx) ALL

# Allow ubuntu to run specific commands as nginx without password
ubuntu ALL=(nginx) NOPASSWD: /path/to/specific/command

# Allow all users in group www to run nginx commands
%www ALL=(nginx) ALL
```

### Common Sudo Options

```bash
# Run as specific user
sudo -u username command

# Run as specific group
sudo -g groupname command

# Run with root privileges (default)
sudo command

# Non-interactive mode
sudo -n command

# List sudo privileges
sudo -l

# Edit sudoers safely
sudo visudo
```

---

## Common Issues and Solutions

### Issue 1: Permission Denied Errors
```bash
# Symptom: /tmp/test_as_me.sh: Permission denied

# Check permissions
ls -la /tmp/test_as_me.sh

# Make executable
chmod +x /tmp/test_as_me.sh
```

### Issue 2: Nginx Still Running as Root
```bash
# Check Nginx user
ps aux | grep nginx

# If still root, check config
grep "^user" /etc/nginx/nginx.conf

# Edit if necessary
sudo sed -i 's/^user root;/user nginx;/' /etc/nginx/nginx.conf

# Reload
sudo nginx -t && sudo service nginx reload
```

### Issue 3: Nginx Can't Access Web Files
```bash
# Problem: nginx user can't read files

# Check permissions
ls -la /var/www/html/

# Fix ownership
sudo chown -R nginx:nginx /var/www/html

# Fix permissions (755 for directories, 644 for files)
sudo chmod -R 755 /var/www/html
find /var/www/html -type f -exec chmod 644 {} \;
```

### Issue 4: Sudo Requires Password

**Problem:** Running `sudo -u nginx command` asks for password

**Solution:** Add to sudoers (carefully):
```bash
sudo visudo

# Add line:
# your_user ALL=(nginx) NOPASSWD: ALL
```

### Issue 5: User Doesn't Exist

**Problem:** `sudo -u nobody` fails with "unknown user"

**Solution:**
```bash
# Create user
sudo useradd -r -s /bin/false nobody

# Or use different user
sudo -u www-data command
```

---

## Script Writing Tips for These Tasks

### Task 0: Run as Different User
```bash
#!/usr/bin/env bash
# This script runs a test script as the nobody user

sudo -u nobody bash /tmp/test_as_me.sh
```

**Key Points:**
- Use `sudo -u username` syntax
- Specify the shell to execute
- Keep it simple and under 5 lines

### Task 1: Run Nginx as Nginx

**Approach:**
1. Stop current Nginx (if running as root)
2. Update Nginx config to use nginx user
3. Start Nginx with new configuration

```bash
#!/usr/bin/env bash
# Fix Nginx to run as nginx user instead of root

sed -i 's/^user root;/user nginx;/' /etc/nginx/nginx.conf
nginx -t && service nginx reload
```

**Key Points:**
- Use `sed` to change config without `apt-get`
- Test configuration with `nginx -t`
- Reload to apply changes

---

## Testing Your Solution

### Verify User for Task 0
```bash
# Create test script if needed
echo '#!/bin/bash' > /tmp/test_as_me.sh
echo 'whoami' >> /tmp/test_as_me.sh
chmod +x /tmp/test_as_me.sh

# Run your script
./0-iamsomeoneelse

# Should output: nobody
```

### Verify User for Task 1
```bash
# Check Nginx processes
ps aux | grep nginx

# Should show:
# nginx    ... nginx: master process
# nginx    ... nginx: worker process

# Verify Nginx is listening
netstat -tuln | grep :80
# or
ss -tuln | grep :80

# Test connection
curl -I localhost
# Should return 200 OK
```

### Verify No Root Processes
```bash
# After running task 1, check for root processes
ps aux | grep -v root | grep -v init

# Should not show any nginx processes running as root
```

---

## File Permissions Basics

### Permission Notation

```
-rwxr-xr-x
│ ││ ││ ││
│ ││ ││ │└─ Others execute
│ ││ ││ ├─ Others read
│ ││ │├─ Others (all)
│ ││ ├─ Group execute
│ ││ └─ Group read
│ │└─ Group (permission group)
│ ├─ Owner execute
│ ├─ Owner read
│ └─ Owner write
└─ File type (- = regular, d = directory, l = link)
```

### Changing Ownership

```bash
# Change owner
sudo chown user file

# Change group
sudo chown :group file

# Change both
sudo chown user:group file

# Recursive
sudo chown -R user:group /path
```

### Changing Permissions

```bash
# Symbolic (rwx)
chmod u+x file           # Add execute for user
chmod g-w file           # Remove write for group
chmod o=r file           # Set others to read only

# Octal (755, 644, etc.)
chmod 755 file           # rwxr-xr-x
chmod 644 file           # rw-r--r--
chmod 600 file           # rw-------
chmod 700 file           # rwx------
```

---

## References and Best Practices

### Useful Commands Summary

```bash
# User information
whoami                           # Current user
id                              # Current user details
id username                     # Specific user details
getent passwd username          # User from database

# Process management
ps aux | grep nginx             # Find processes
ps -eo user,pid,cmd | grep nginx  # Show user and process
pstree                          # Process tree

# Nginx management
nginx -t                        # Test config syntax
service nginx status            # Check status
service nginx reload            # Reload config
service nginx restart           # Full restart

# Sudo operations
sudo -u username command        # Run as user
sudo -l                         # List sudo privileges
sudo visudo                     # Edit sudoers safely

# File operations
chown user:group file           # Change owner
chmod 755 file                  # Change permissions
chown -R user:group /path       # Recursive change
```

---

## Common Nginx Configuration Errors

### Error: nginx: [emerg] permission denied
**Cause:** Nginx can't access a directory or file
**Solution:**
```bash
sudo chown nginx:nginx /var/www/html
sudo chmod 750 /var/www/html
```

### Error: nginx: [error] open() "/var/run/nginx.pid"
**Cause:** Can't write PID file
**Solution:**
```bash
sudo mkdir -p /var/run/nginx
sudo chown nginx:nginx /var/run/nginx
```

### Error: bind() to 0.0.0.0:80 failed
**Cause:** Port already in use or permission denied
**Solution:**
```bash
# Check what's using the port
sudo netstat -tuln | grep :80

# Kill process if necessary
sudo kill -9 <PID>

# Or run as root if that's the issue
sudo service nginx start
```

---

## Debugging Checklist

- [ ] Script is executable (`chmod +x`)
- [ ] Correct shebang (`#!/usr/bin/env bash`)
- [ ] Nginx config syntax is valid (`nginx -t`)
- [ ] Nginx user is set correctly in config
- [ ] Web files have correct ownership
- [ ] Web files have readable permissions
- [ ] No root processes for Nginx (except init)
- [ ] Port 80 is listening
- [ ] curl/telnet can connect to port 80
- [ ] Script passes `shellcheck`
- [ ] Script output matches expected output

---

## Resources

- [Linux Users and Groups](https://linuxize.com/post/how-to-create-users-in-linux-using-the-useradd-command/)
- [Understanding File Permissions](https://linuxize.com/post/understanding-linux-file-permissions/)
- [Sudo Documentation](https://www.sudo.ws/sudo/)
- [Nginx Beginner's Guide](https://nginx.org/en/docs/beginners_guide.html)
- [Process Management in Linux](https://www.kernel.org/doc/html/latest/admin-guide/index.html)
- [Principle of Least Privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)

## Author
This project is part of the ALX Software Engineering Program.

## License
This project is licensed under the terms of the ALX Software Engineering Program.
