# 0x01. Shell, permissions

This project focuses on understanding and manipulating file permissions, ownership, and user management in Unix/Linux systems. Students will learn how to control access to files and directories, manage user accounts, and implement security through proper permission settings.

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:

### Permissions
- What do the commands `chmod`, `sudo`, `su`, `chown`, `chgrp` do
- Linux file permissions
- How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- How to change permissions, owner and group of a file
- Why can't a normal user `chown` a file
- How to run a command with root privileges
- How to change user ID or become another user

### Other Man Pages
- How to create a user
- How to create a group
- How to print real and effective user and group IDs
- How to print the groups a user is in
- How to print the effective userid

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- A `README.md` file, at the root of the folder of the project, describing what each script is doing
- You are not allowed to use backticks, `&&`, `||` or `;`
- All your files must be executable

## Tasks

### 0. My name is Betty
**File:** `0-iam_betty`

Create a script that switches the current user to the user `betty`.

- You should use exactly 8 characters for your command
- You can assume that the user `betty` will exist when we will run your script

**Example:**
```bash
julien@ubuntu:~/0x01$ tail -1 0-iam_betty | wc -c
9
julien@ubuntu:~/0x01$ 
```

### 1. Who am I
**File:** `1-who_am_i`

Write a script that prints the effective username of the current user.

**Example:**
```bash
julien@ubuntu:~/0x01$ ./1-who_am_i
julien
julien@ubuntu:~/0x01$ 
```

### 2. Groups
**File:** `2-groups`

Write a script that prints all the groups the current user is part of.

**Example:**
```bash
julien@ubuntu:~/0x01$ ./2-groups
julien adm cdrom sudo dip plugdev lpadmin sambashare
julien@ubuntu:~/0x01$ 
```

### 3. New owner
**File:** `3-new_owner`

Write a script that changes the owner of the file `hello` to the user `betty`.

**Example:**
```bash
julien@ubuntu:~/0x01$ ls -l
total 24
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 julien julien  0 Sep 20 14:18 hello
julien@ubuntu:~/0x01$ sudo ./3-new_owner 
julien@ubuntu:~/0x01$ ls -l
total 24
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 betty  julien  0 Sep 20 14:18 hello
julien@ubuntu:~/0x01$ 
```

### 4. Empty!
**File:** `4-empty`

Write a script that creates an empty file called `hello`.

### 5. Execute
**File:** `5-execute`

Write a script that adds execute permission to the owner of the file `hello`.

- The file `hello` will be in the working directory

**Example:**
```bash
julien@ubuntu:~/0x01$ ls -l hello
-rw-rw-r-- 1 julien julien 0 Sep 20 14:22 hello
julien@ubuntu:~/0x01$ ./5-execute 
julien@ubuntu:~/0x01$ ls -l hello
-rwxrw-r-- 1 julien julien 0 Sep 20 14:22 hello
julien@ubuntu:~/0x01$ 
```

### 6. Multiple permissions
**File:** `6-multiple_permissions`

Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.

- The file `hello` will be in the working directory

**Example:**
```bash
julien@ubuntu:~/0x01$ ls -l hello
-rw-rw-r-- 1 julien julien 0 Sep 20 14:22 hello
julien@ubuntu:~/0x01$ ./6-multiple_permissions 
julien@ubuntu:~/0x01$ ls -l hello
-rwxrwxr-- 1 julien julien 0 Sep 20 14:22 hello
julien@ubuntu:~/0x01$ 
```

### 7. Everybody!
**File:** `7-everybody`

Write a script that adds execution permission to the owner, the group owner and the other users, to the file `hello`

- The file `hello` will be in the working directory
- You are not allowed to use commas for this script

**Example:**
```bash
julien@ubuntu:~/0x01$ ls -l hello
-rw-rw-r-- 1 julien julien 0 Sep 20 14:22 hello
julien@ubuntu:~/0x01$ ./7-everybody 
julien@ubuntu:~/0x01$ ls -l hello
-rwxrwxrwx 1 julien julien 0 Sep 20 14:22 hello
julien@ubuntu:~/0x01$ 
```

### 8. James Bond
**File:** `8-James_Bond`

Write a script that sets the permission to the file `hello` as follows:

- Owner: no permission at all
- Group: no permission at all
- Other users: all the permissions

**Example:**
```bash
julien@ubuntu:~/0x01$ ls -l hello
-rwxrwxrwx 1 julien julien 0 Sep 20 14:22 hello
julien@ubuntu:~/0x01$ ./8-James_Bond 
julien@ubuntu:~/0x01$ ls -l hello
-------rwx 1 julien julien 0 Sep 20 14:22 hello
julien@ubuntu:~/0x01$ 
```

### 9. John Doe
**File:** `9-John_Doe`

Write a script that sets the mode of the file `hello` to this:

```bash
-rwxr-x-wx 1 julien julien 0 Sep 20 14:22 hello
```

- The file `hello` will be in the working directory
- You are not allowed to use commas for this script

### 10. Look in the mirror
**File:** `10-mirror_permissions`

Write a script that sets the mode of the file `hello` the same as `olleh`'s mode.

- The file `hello` will be in the working directory
- The file `olleh` will be in the working directory

**Example:**
```bash
julien@ubuntu:~/0x01$ ls -l
total 16
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rwxr-x-wx 1 julien julien  0 Sep 20 14:22 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:~/0x01$ ./10-mirror_permissions 
julien@ubuntu:~/0x01$ ls -l
total 16
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rw-rw-r-- 1 julien julien  0 Sep 20 14:22 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:~/0x01$ 
```

### 11. Directories
**File:** `11-directories_permissions`

Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.

- Regular files should not be changed.

**Example:**
```bash
julien@ubuntu:~/0x01$ ls -l
total 20
drwx------ 2 julien julien 4096 Sep 20 14:49 dir0
drwx------ 2 julien julien 4096 Sep 20 14:49 dir1
drwx------ 2 julien julien 4096 Sep 20 14:49 dir2
-rwxrw-r-- 1 julien julien   36 Sep 20 14:53 11-directories_permissions
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:~/0x01$ ./11-directories_permissions 
julien@ubuntu:~/0x01$ ls -l
total 20
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
-rwxrw-r-- 1 julien julien   36 Sep 20 14:53 11-directories_permissions
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:~/0x01$ 
```

### 12. More directories
**File:** `12-directory_permissions`

Create a script that creates a directory called `my_dir` with permissions 751 in the working directory.

**Example:**
```bash
julien@ubuntu:~/0x01$ ./12-directory_permissions 
julien@ubuntu:~/0x01$ ls -l
total 20
drwxr-x--x 2 julien julien 4096 Sep 20 14:58 my_dir
-rwxrw-r-- 1 julien julien   39 Sep 20 14:59 12-directory_permissions
julien@ubuntu:~/0x01$ 
```

### 13. Change group
**File:** `13-change_group`

Write a script that changes the group owner to `school` for the file `hello`

- The file `hello` will be in the working directory

**Example:**
```bash
julien@ubuntu:~/0x01$ ls -l hello
-rwxrw-r-- 1 julien julien 0 Sep 20 14:22 hello
julien@ubuntu:~/0x01$ sudo ./13-change_group 
julien@ubuntu:~/0x01$ ls -l hello
-rwxrw-r-- 1 julien school 0 Sep 20 14:22 hello
julien@ubuntu:~/0x01$ 
```

## Advanced Tasks

### 14. Owner and group
**File:** `100-change_owner_and_group`

Write a script that changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory.

**Example:**
```bash
julien@ubuntu:~/0x01$ ls -l
total 24
-rwxrw-r-- 1 julien julien   36 Sep 20 15:06 100-change_owner_and_group
-rwxrw-r-- 1 julien julien   34 Sep 20 15:12 13-change_group
drwxr-x--x 2 julien julien 4096 Sep 20 14:58 my_dir
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:~/0x01$ sudo ./100-change_owner_and_group 
julien@ubuntu:~/0x01$ ls -l
total 24
-rwxrw-r-- 1 vincent staff   36 Sep 20 15:06 100-change_owner_and_group
-rwxrw-r-- 1 vincent staff   34 Sep 20 15:12 13-change_group
drwxr-x--x 2 vincent staff 4096 Sep 20 14:58 my_dir
-rw-rw-r-- 1 vincent staff   23 Sep 20 14:25 hello
julien@ubuntu:~/0x01$ 
```

### 15. Symbolic links
**File:** `101-symbolic_link_permissions`

Write a script that changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively.

- The file `_hello` is in the working directory
- The file `_hello` is a symbolic link

**Example:**
```bash
julien@ubuntu:~/0x01$ ls -l
total 44
-rwxrw-r-- 1 julien julien   44 Sep 20 15:12 101-symbolic_link_permissions
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
lrwxrwxrwx 1 julien julien    5 Sep 20 15:17 _hello -> hello
julien@ubuntu:~/0x01$ sudo ./101-symbolic_link_permissions 
julien@ubuntu:~/0x01$ ls -l
total 44
-rwxrw-r-- 1 julien julien      44 Sep 20 15:12 101-symbolic_link_permissions
-rw-rw-r-- 1 julien julien      23 Sep 20 14:25 hello
lrwxrwxrwx 1 vincent  staff     5 Sep 20 15:17 _hello -> hello
julien@ubuntu:~/0x01$ 
```

### 16. If only
**File:** `102-if_only`

Write a script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.

- The file `hello` will be in the working directory

**Example:**
```bash
julien@ubuntu:~/0x01$ ls -l hello
-rw-rw-r-- 1 guillaume julien 23 Sep 20 14:25 hello
julien@ubuntu:~/0x01$ sudo ./102-if_only 
julien@ubuntu:~/0x01$ ls -l hello
-rw-rw-r-- 1 betty julien 23 Sep 20 14:25 hello
julien@ubuntu:~/0x01$ 
```

### 17. Star Wars
**File:** `103-Star_Wars`

Write a script that will play the StarWars IV episode in the terminal.

## Understanding File Permissions

### Permission Types
- **r (read)**: View file contents or list directory contents
- **w (write)**: Modify file contents or create/delete files in directory
- **x (execute)**: Run file as program or access directory

### Permission Groups
- **Owner (user)**: The file/directory owner
- **Group**: Users in the same group as the file/directory
- **Others**: All other users

### Symbolic Notation
```
-rwxrw-r--
```
- Position 1: File type (`-` file, `d` directory, `l` link)
- Positions 2-4: Owner permissions (rwx)
- Positions 5-7: Group permissions (rw-)
- Positions 8-10: Others permissions (r--)

### Numeric (Octal) Notation

| Permission | Binary | Octal |
|------------|--------|-------|
| --- | 000 | 0 |
| --x | 001 | 1 |
| -w- | 010 | 2 |
| -wx | 011 | 3 |
| r-- | 100 | 4 |
| r-x | 101 | 5 |
| rw- | 110 | 6 |
| rwx | 111 | 7 |

**Examples:**
- `755` = `rwxr-xr-x` (owner: rwx, group: r-x, others: r-x)
- `644` = `rw-r--r--` (owner: rw-, group: r--, others: r--)
- `777` = `rwxrwxrwx` (all permissions for everyone)

## Key Commands

### Permission Commands
| Command | Description | Example |
|---------|-------------|---------|
| `chmod` | Change file permissions | `chmod 755 file` |
| `chown` | Change file owner | `chown user:group file` |
| `chgrp` | Change group owner | `chgrp group file` |
| `umask` | Set default permissions | `umask 022` |

### User/Group Commands
| Command | Description | Example |
|---------|-------------|---------|
| `su` | Switch user | `su username` |
| `sudo` | Execute as another user | `sudo command` |
| `whoami` | Print current username | `whoami` |
| `id` | Print user and group IDs | `id username` |
| `groups` | Print group memberships | `groups username` |

### File Information
| Command | Description | Example |
|---------|-------------|---------|
| `ls -l` | Long format listing | `ls -l file` |
| `stat` | Detailed file information | `stat file` |
| `file` | Determine file type | `file filename` |

## Common Permission Patterns

### Files
- `644` (rw-r--r--): Standard file permissions
- `755` (rwxr-xr-x): Executable files
- `600` (rw-------): Private files (only owner access)
- `777` (rwxrwxrwx): World-writable (generally avoided)

### Directories
- `755` (rwxr-xr-x): Standard directory permissions
- `750` (rwxr-x---): Group-accessible directory
- `700` (rwx------): Private directory
- `1755` (rwxr-xr-t): Directory with sticky bit

## Special Permissions

### Sticky Bit (t)
- Set on directories to restrict deletion
- Only owner can delete files in the directory
- Example: `/tmp` directory

### SUID (s)
- Set on executable files
- File runs with owner's privileges
- Example: `passwd` command

### SGID (s)
- Set on directories or executable files
- New files inherit group ownership
- Executables run with group privileges

## Security Best Practices

1. **Principle of Least Privilege**: Grant minimum necessary permissions
2. **Regular Auditing**: Check file permissions regularly
3. **Avoid 777**: Never use world-writable permissions unless absolutely necessary
4. **Use Groups**: Organize users into appropriate groups
5. **Secure Home Directories**: Keep personal files private (700 or 750)
6. **System Files**: Never modify system file permissions without understanding consequences

## Resources

### Read or watch:
- [Permissions](http://linuxcommand.org/lc3_lts0090.php)
- [Linux File Permissions](https://www.guru99.com/file-permissions.html)
- [Understanding Linux File Permissions](https://www.digitalocean.com/community/tutorials/understanding-linux-permissions)

### man or help:
- `chmod`
- `sudo`
- `su`
- `chown`
- `chgrp`
- `id`
- `groups`
- `whoami`
- `adduser`
- `useradd`
- `addgroup`

## Testing Your Scripts

```bash
# Make script executable
chmod +x script_name

# Test the script
./script_name

# Check script length (should be 2 lines)
wc -l script_name

# Verify permissions with ls -l
ls -l filename
```

## Troubleshooting

### Common Issues
- **Permission denied**: Use `sudo` for administrative tasks
- **Command not found**: Check if file is executable (`chmod +x`)
- **Operation not permitted**: Regular users cannot change ownership to other users
- **Invalid permissions**: Use valid octal numbers (0-7)

### Debugging Tips
- Use `ls -l` to check current permissions
- Use `whoami` to verify current user
- Use `groups` to check group memberships
- Test with `sudo` if permission errors occur


**ALX Software Engineering Program** | *0x01. Shell, permissions*
