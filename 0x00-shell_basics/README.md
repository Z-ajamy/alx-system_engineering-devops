# 0x00. Shell, basics

This project introduces fundamental shell commands and navigation techniques in Unix/Linux environments. Students will learn essential command-line operations, file system navigation, and basic shell scripting concepts that form the foundation of system administration.

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- What does RTFM mean?
- What is a Shebang
- What is the Shell
- What is the shell
- What is the difference between a terminal and a shell
- What is the shell prompt
- How to use the history (the basics)

### Navigation
- What do the commands or built-ins `cd`, `pwd`, `ls` do
- How to navigate the filesystem
- What are the `.` and `..` directories
- What is the working directory, how to print it and how to change it
- What is the root directory
- What is the home directory, and how to go there
- What is the difference between the root directory and the home directory of the user root
- What are the characteristics of hidden files and how to list them
- What does the command `cd -` do

### Looking Around
- What do the commands `ls`, `less`, `file` do
- How do you use options and arguments with commands
- Understand the ls long format and how to display it
- What does the `ln` command do
- What do you find in the most common/important directories
- What is a symbolic link
- What is a hard link
- What is the difference between a hard link and a symbolic link

### Manipulating Files
- What do the commands `cp`, `mv`, `rm`, `mkdir` do
- What are wildcards and how do they work
- How to use wildcards

### Working with Commands
- What do `type`, `which`, `help`, `man` commands do
- What are the different kinds of commands
- What is an alias
- When do you use the command help instead of man

### Reading Man Pages
- How to read a man page
- What are man page sections
- What are the section numbers for User commands, System calls and Library functions

### Keyboard Shortcuts for Bash
- Common shortcuts for Bash
- LTS
- Shebang

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, describing what each script is doing
- You are not allowed to use backticks, `&&`, `||` or `;`
- All your scripts must be executable. To make your file executable: `chmod +x file`
- You are not allowed to use `sed` or `awk`

## Tasks

### 0. Where am I?
**File:** `0-current_working_directory`

Write a script that prints the absolute path name of the current working directory.

**Example:**
```bash
$ ./0-current_working_directory
/root/alx-system_engineering-devops/0x00-shell_basics
```

### 1. What's in there?
**File:** `1-listit`

Display the contents list of your current directory.

**Example:**
```bash
$ ./1-listit
Applications    Documents   Dropbox Movies Pictures
Desktop         Downloads   Library Music   Public
```

### 2. There is no place like home
**File:** `2-bring_me_home`

Write a script that changes the working directory to the user's home directory.

- You are not allowed to use any shell variables

### 3. The long format
**File:** `3-listfiles`

Display current directory contents in a long format.

**Example:**
```bash
$ ./3-listfiles
total 32
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
```

### 4. Hidden files
**File:** `4-listmorefiles`

Display current directory contents, including hidden files (starting with `.`). Use the long format.

**Example:**
```bash
$ ./4-listmorefiles
total 32
drwxr-xr-x@ 6 sylvain staff 204 Jan 25 00:29 .
drwxr-xr-x@ 43 sylvain staff 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:41 4-listmorefiles
```

### 5. I love numbers
**File:** `5-listfilesdigitonly`

Display current directory contents:
- Long format
- with user and group IDs displayed numerically
- And hidden files (starting with .)

**Example:**
```bash
$ ./5-listfilesdigitonly
total 32
drwxr-xr-x@ 6 501 20 204 Jan 25 00:29 .
drwxr-xr-x@ 43 501 20 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:41 4-listmorefiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:43 5-listfilesdigitonly
```

### 6. Welcome
**File:** `6-firstdirectory`

Create a script that creates a directory named `my_first_directory` in the `/tmp/` directory.

**Example:**
```bash
$ ./6-firstdirectory
$ file /tmp/my_first_directory/
/tmp/my_first_directory/: directory
```

### 7. Betty in my first directory
**File:** `7-movethatfile`

Move the file `betty` from `/tmp/` to `/tmp/my_first_directory`.

**Example:**
```bash
$ ./7-movethatfile
$ ls /tmp/my_first_directory/
betty
```

### 8. Bye bye Betty
**File:** `8-firstdelete`

Delete the file `betty` in `/tmp/my_first_directory`.

**Example:**
```bash
$ ./8-firstdelete
$ ls /tmp/my_first_directory/
```

### 9. Bye bye My first directory
**File:** `9-firstdirdeletion`

Delete the directory `my_first_directory` that is in the `/tmp` directory.

**Example:**
```bash
$ ./9-firstdirdeletion
$ file /tmp/my_first_directory
/tmp/my_first_directory: cannot open `/tmp/my_first_directory' (No such file or directory)
```

### 10. Back to the future
**File:** `10-back`

Write a script that changes the working directory to the previous one.

**Example:**
```bash
julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ cd /var
julien@ubuntu:/var$ pwd
/var
julien@ubuntu:/var$ source ./10-back
/tmp
julien@ubuntu:/tmp$ pwd
/tmp
```

### 11. Lists
**File:** `11-lists`

Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.

### 12. File type
**File:** `12-file_type`

Write a script that prints the type of the file named `iamafile`. The file `iamafile` will be in the `/tmp` directory when we will run your script.

**Example:**
```bash
ubuntu@ip-172-31-63-244:~$ ./12-file_type
/tmp/iamafile: ELF 64-bit LSB  executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=bd39c07194a778ccc066fc963ca152bdfaa3f971, stripped
```

### 13. We are symbols, and inhabit symbols
**File:** `13-symbolic_link`

Create a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory.

**Example:**
```bash
ubuntu@ip-172-31-63-244:~$ ls -la __ls__
lrwxrwxrwx 1 ubuntu ubuntu 7 Sep 20 03:24 __ls__ -> /bin/ls
```

### 14. Copy HTML files
**File:** `14-copy_html`

Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

You can consider that all HTML files have the extension `.html`.

## Advanced Tasks

### 15. Let's move
**File:** `100-lets_move`

Create a script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.

You can assume that the directory `/tmp/u` will exist when we will run your script.

**Example:**
```bash
ubuntu@ip-172-31-63-244:~$ ls -la
total 148
drwxr-xr-x 1 ubuntu ubuntu   4096 Sep 20 03:54 .
drwxr-xr-x 3 root   root     4096 Sep 20 03:12 ..
-rw-r--r-- 1 ubuntu ubuntu    220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu   3771 Feb 25  2020 .bashrc
-rw-r--r-- 1 ubuntu ubuntu    807 Feb 25  2020 .profile
-rwxrw-r-- 1 ubuntu ubuntu     69 Sep 20 03:54 100-lets_move
-rw-rw-r-- 1 ubuntu ubuntu      0 Sep 20 03:54 Holberton
-rw-rw-r-- 1 ubuntu ubuntu      0 Sep 20 03:54 Idea
-rw-rw-r-- 1 ubuntu ubuntu      0 Sep 20 03:54 Random
-rw-rw-r-- 1 ubuntu ubuntu      0 Sep 20 03:54 School
-rw-rw-r-- 1 ubuntu ubuntu      0 Sep 20 03:54 holberton
-rw-rw-r-- 1 ubuntu ubuntu      0 Sep 20 03:54 idea
-rw-rw-r-- 1 ubuntu ubuntu      0 Sep 20 03:54 random
-rw-rw-r-- 1 ubuntu ubuntu      0 Sep 20 03:54 school
ubuntu@ip-172-31-63-244:~$ ./100-lets_move
ubuntu@ip-172-31-63-244:~$ ls -la
total 132
drwxr-xr-x 1 ubuntu ubuntu   4096 Sep 20 03:54 .
drwxr-xr-x 3 root   root     4096 Sep 20 03:12 ..
-rw-r--r-- 1 ubuntu ubuntu    220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu   3771 Feb 25  2020 .bashrc
-rw-r--r-- 1 ubuntu ubuntu    807 Feb 25  2020 .profile
-rwxrw-r-- 1 ubuntu ubuntu     69 Sep 20 03:54 100-lets_move
-rw-rw-r-- 1 ubuntu ubuntu      0 Sep 20 03:54 holberton
-rw-rw-r-- 1 ubuntu ubuntu      0 Sep 20 03:54 idea
-rw-rw-r-- 1 ubuntu ubuntu      0 Sep 20 03:54 random
-rw-rw-r-- 1 ubuntu ubuntu      0 Sep 20 03:54 school
ubuntu@ip-172-31-63-244:~$ ls -la /tmp/u
total 16
drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:54 .
drwxrwxrwt 9 root   root   4096 Sep 20 03:54 ..
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:54 Holberton
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:54 Idea
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:54 Random
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:54 School
```

### 16. Clean Emacs
**File:** `101-clean_emacs`

Create a script that deletes all files in the current working directory that end with the character `~`.

**Example:**
```bash
ubuntu@ip-172-31-63-244:~$ ls
main.c~ Makefile~ 
ubuntu@ip-172-31-63-244:~$ ./101-clean_emacs
ubuntu@ip-172-31-63-244:~$ ls
ubuntu@ip-172-31-63-244:~$
```

### 17. Tree
**File:** `102-tree`

Create a script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory.

You are only allowed to use two spaces (and lines) in your script, not more.

**Example:**
```bash
julien@ubuntu:~/holbertonschool-sysadmin_devops/0x00-shell_basics$ ls -la
total 44
drwxrwxr-x 2 julien julien 4096 Sep 20 12:09 .
drwxrwxr-x 6 julien julien 4096 Sep 20 12:09 ..
julien@ubuntu:~/holbertonschool-sysadmin_devops/0x00-shell_basics$ ./102-tree
julien@ubuntu:~/holbertonschool-sysadmin_devops/0x00-shell_basics$ tree
.
└── welcome
    └── to
        └── school

3 directories, 0 files
julien@ubuntu:~/holbertonschool-sysadmin_devops/0x00-shell_basics$
```

### 18. Life is a series of commas, not periods
**File:** `103-commas`

Write a command that lists all the files and directories of the current directory, separated by commas (`,`).

**Requirements:**
- Directory names should end with a slash (`/`)
- Files and directories starting with a dot (`.`) should be listed
- The listing should be alpha ordered, except for the directories `.` and `..` which should be listed at the very beginning
- Only digits and letters are used to sort; Digits should come first
- You can assume that all the files we will test with will have at least one letter or one digit
- The listing should end with a new line

**Example:**
```bash
ubuntu@ubuntu:~/$ ls -a

.  ..  0-commas  0-commas-checks  1-empty_casks  2-gifs  3-directories  4-zeros  5-rot13  6-odd  7-sort_rot13  Makefile  quote  .test  test_dir  test.var

ubuntu@ubuntu:~/$ ./103-commas

./, ../, 0-commas, 0-commas-checks/, 1-empty_casks, 2-gifs, 3-directories/, 4-zeros, 5-rot13, 6-odd, 7-sort_rot13, Makefile, quote, .test, test_dir/, test.var
ubuntu@ubuntu:~/$
```

## Key Concepts

### Essential Commands

| Command | Description | Example |
|---------|-------------|---------|
| `pwd` | Print working directory | `pwd` |
| `ls` | List directory contents | `ls -la` |
| `cd` | Change directory | `cd /home/user` |
| `mkdir` | Create directory | `mkdir mydir` |
| `rmdir` | Remove directory | `rmdir mydir` |
| `rm` | Remove files | `rm file.txt` |
| `cp` | Copy files | `cp file1 file2` |
| `mv` | Move/rename files | `mv old.txt new.txt` |
| `ln` | Create links | `ln -s target link` |
| `file` | Determine file type | `file myfile` |

### Directory Navigation

- `.` - Current directory
- `..` - Parent directory  
- `~` - Home directory
- `/` - Root directory
- `cd -` - Previous directory

### File Permissions

The long format (`ls -l`) shows:
```
-rwxrw-r-- 1 user group size date filename
```

- First character: file type (`-` file, `d` directory, `l` link)
- Next 9 characters: permissions (user, group, others)
- `r` - read, `w` - write, `x` - execute

## Resources

### Read or watch:
- [What Is "The Shell"?](http://linuxcommand.org/lc3_lts0010.php)
- [Navigation](http://linuxcommand.org/lc3_lts0020.php)
- [Looking Around](http://linuxcommand.org/lc3_lts0030.php)
- [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)
- [Manipulating Files](http://linuxcommand.org/lc3_lts0050.php)
- [Working With Commands](http://linuxcommand.org/lc3_lts0060.php)
- [Reading Man pages](http://linuxcommand.org/lc3_man_pages/man1.html)
- [Keyboard shortcuts for Bash](https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/)
- [LTS](https://wiki.ubuntu.com/LTS)
- [Shebang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29)

### man or help:
- `cd`
- `ls`
- `pwd`
- `less`
- `file`
- `ln`
- `cp`
- `mv`
- `rm`
- `mkdir`
- `type`
- `which`
- `help`
- `man`

## Common Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + C` | Interrupt/Kill current command |
| `Ctrl + D` | Exit/logout |
| `Ctrl + Z` | Suspend current command |
| `Ctrl + A` | Move to beginning of line |
| `Ctrl + E` | Move to end of line |
| `Ctrl + U` | Delete from cursor to beginning |
| `Ctrl + K` | Delete from cursor to end |
| `Ctrl + L` | Clear screen |
| `Tab` | Auto-complete |
| `↑/↓` | Command history |

## Testing Your Scripts

```bash
# Make script executable
chmod +x script_name

# Test the script
./script_name

# Check script length (should be 2 lines)
wc -l script_name
```

**ALX Software Engineering Program** | *0x00. Shell, basics*
