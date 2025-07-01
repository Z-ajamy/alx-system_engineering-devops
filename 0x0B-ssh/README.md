# 0x0B-ssh

## Description
This project covers the fundamentals of SSH (Secure Shell Protocol), focusing on secure remote connections, key-based authentication, and server configuration. You'll learn how to establish secure connections to remote servers and manage SSH configurations effectively.

## Learning Objectives
By the end of this project, you should be able to explain:

- What is a server and where servers usually live
- What is SSH and how it works
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`
- How to configure SSH client and server
- SSH security best practices

## Requirements
- **Allowed editors**: vi, vim, emacs
- **OS**: Ubuntu 20.04 LTS
- **File endings**: All files should end with a new line
- **Executable**: All Bash script files must be executable
- **Shebang**: First line of all Bash scripts should be `#!/usr/bin/env bash`
- **Documentation**: Second line of all Bash scripts should be a comment explaining what the script does

## Project Structure
```
0x0B-ssh/
├── README.md
├── 0-use_a_private_key
├── 1-create_ssh_key_pair
├── 2-ssh_config
└── 100-puppet_ssh_config.pp
```

## Tasks

### 0. Use a private key
**File**: `0-use_a_private_key`

Write a Bash script that uses SSH to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

Requirements:
- Only use SSH single-character flags
- You cannot use `-l`
- You do not need to handle the case of a private key protected by a passphrase

### 1. Create an SSH key pair
**File**: `1-create_ssh_key_pair`

Write a Bash script that creates an RSA key pair.

Requirements:
- Name of the created private key must be `school`
- Number of bits in the created key must be 4096
- The created key must be protected by the passphrase `betty`

### 2. Client configuration file
**File**: `2-ssh_config`

Your machine has an SSH configuration file for the local SSH client. Configure it to use the private key `~/.ssh/school` and to refuse to authenticate using a password.

### 3. Let me in!
Add the provided SSH public key to your server so that we can connect using the `ubuntu` user.

### 4. Client configuration file (w/ Puppet)
**File**: `100-puppet_ssh_config.pp`

Using Puppet, make changes to the SSH client configuration file so that you can connect to a server without typing a password.

## Educational Resources

### What is SSH?
SSH (Secure Shell) is a cryptographic network protocol that allows secure communication between two networked devices. It's commonly used for:
- Remote command-line login
- Remote command execution
- File transfers (SCP, SFTP)
- Port forwarding and tunneling

### How SSH Works
1. **Connection Establishment**: Client initiates connection to SSH server (typically port 22)
2. **Protocol Negotiation**: Client and server agree on SSH version and encryption methods
3. **Key Exchange**: Cryptographic keys are exchanged using algorithms like Diffie-Hellman
4. **Authentication**: User authentication via password or public key
5. **Secure Communication**: All data is encrypted using negotiated algorithms

### SSH Key Authentication
SSH supports two main authentication methods:

#### Password Authentication
- Simple username/password combination
- Less secure due to brute force vulnerability
- Passwords transmitted over encrypted connection

#### Public Key Authentication
- Uses cryptographic key pairs (public/private)
- Private key stays on client, public key on server
- More secure and convenient for automation
- Supports passphrases for additional security

### Common SSH Commands

```bash
# Connect to remote host
ssh username@hostname

# Connect using specific private key
ssh -i ~/.ssh/private_key username@hostname

# Copy files to remote host
scp file.txt username@hostname:/remote/path/

# Copy files from remote host
scp username@hostname:/remote/file.txt ./local/path/

# Create SSH tunnel
ssh -L local_port:remote_host:remote_port username@hostname

# Run remote command
ssh username@hostname 'command to execute'
```

### SSH Configuration Files

#### Client Configuration (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.100
    User ubuntu
    Port 22
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
```

#### Server Configuration (`/etc/ssh/sshd_config`)
```
Port 22
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
```

### SSH Security Best Practices

1. **Use Key-Based Authentication**
   - Disable password authentication
   - Use strong key pairs (RSA 4096-bit or Ed25519)
   - Protect private keys with passphrases

2. **Server Hardening**
   - Change default SSH port
   - Disable root login
   - Use fail2ban for brute force protection
   - Keep SSH server updated

3. **Key Management**
   - Regularly rotate SSH keys
   - Use different keys for different purposes
   - Store private keys securely
   - Remove unused public keys from authorized_keys

4. **Network Security**
   - Use firewalls to restrict SSH access
   - Implement VPN for additional security layer
   - Monitor SSH logs for suspicious activity

### Troubleshooting SSH

#### Common Issues and Solutions

**Permission Denied (publickey)**
```bash
# Check SSH agent
ssh-add -l

# Add key to agent
ssh-add ~/.ssh/private_key

# Check file permissions
chmod 700 ~/.ssh
chmod 600 ~/.ssh/private_key
chmod 644 ~/.ssh/public_key
```

**Connection Timeout**
```bash
# Test connectivity
telnet hostname 22

# Check SSH service status
sudo systemctl status ssh

# Verify firewall rules
sudo ufw status
```

**Host Key Verification Failed**
```bash
# Remove old host key
ssh-keygen -R hostname

# Accept new host key
ssh -o StrictHostKeyChecking=no username@hostname
```

### Additional Resources

- [OpenSSH Manual](https://www.openssh.com/manual.html)
- [SSH Protocol Specification (RFC 4251)](https://tools.ietf.org/html/rfc4251)
- [Digital Ocean SSH Tutorials](https://www.digitalocean.com/community/tags/ssh)
- [SSH Academy](https://www.ssh.com/academy/ssh)

### Tools and Utilities

- **ssh-keygen**: Generate SSH key pairs
- **ssh-agent**: Manage SSH keys in memory
- **ssh-add**: Add keys to SSH agent
- **ssh-copy-id**: Copy public key to remote host
- **sshd**: SSH daemon (server)
- **ssh-audit**: Security auditing tool for SSH

## Author
This project is part of the ALX Software Engineering curriculum focusing on system administration and DevOps fundamentals.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.