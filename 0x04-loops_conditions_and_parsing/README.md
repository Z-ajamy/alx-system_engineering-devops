# 0x04. Loops, conditions and parsing

This project focuses on learning shell scripting fundamentals including loops, conditional statements, and text parsing in Bash. Students will master control structures and text manipulation techniques essential for system administration and automation.

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- How to create SSH keys
- What is the advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`
- How to use `while`, `until` and `for` loops
- How to use `if`, `else`, `elif` and `case` condition statements
- How to use the `cut` command
- What are files and other comparison operators, and how to use them

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- You are not allowed to use `awk`
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

### Shellcheck
Shellcheck is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that most people don't think about.

Install Shellcheck:
```bash
sudo apt-get install -y shellcheck
```

## Tasks

### 0. Create a SSH RSA key pair
**File:** `0-RSA_public_key.pub`

Create a RSA key pair and share your public key in the file `0-RSA_public_key.pub`.

**Example:**
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

### 1. For Best School loop
**File:** `1-for_best_school`

Write a Bash script that displays `Best School` 10 times using a `for` loop.

**Requirements:**
- You must use the `for` loop (`while` and `until` are forbidden)

**Example:**
```bash
./1-for_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
```

### 2. While Best School loop
**File:** `2-while_best_school`

Write a Bash script that displays `Best School` 10 times using a `while` loop.

**Requirements:**
- You must use the `while` loop (`for` and `until` are forbidden)

### 3. Until Best School loop
**File:** `3-until_best_school`

Write a Bash script that displays `Best School` 10 times using an `until` loop.

**Requirements:**
- You must use the `until` loop (`for` and `while` are forbidden)

### 4. If 9, say Hi!
**File:** `4-if_9_say_hi`

Write a Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi` on a new line.

**Requirements:**
- You must use the `while` loop (`for` and `until` are forbidden)
- You must use the `if` statement

**Example:**
```bash
./4-if_9_say_hi
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Hi
Best School
```

### 5. 4 bad luck, 8 is your chance
**File:** `5-4_bad_luck_8_is_your_chance`

Write a Bash script that loops from 1 to 10 and:
- displays `bad luck` for the 4th loop iteration
- displays `good luck` for the 8th loop iteration
- displays `Best School` for the other iterations

**Requirements:**
- You must use the `while` loop (`for` and `until` are forbidden)
- You must use the `if`, `elif` and `else` statements

### 6. Superstitious numbers
**File:** `6-superstitious_numbers`

Write a Bash script that displays numbers from 1 to 20 and:
- displays `4` and then `bad luck from China` for the 4th loop iteration
- displays `9` and then `bad luck from Japan` for the 9th loop iteration
- displays `17` and then `bad luck from Italy` for the 17th loop iteration

**Requirements:**
- You must use the `while` loop (`for` and `until` are forbidden)
- You must use the `case` statement

### 7. Clock
**File:** `7-clock`

Write a Bash script that displays the time for 12 hours and 59 minutes:
- display hours from 0 to 12
- display minutes from 1 to 59

**Format:** `Hour: X` followed by `Minute: Y`

**Requirements:**
- You must use the `while` loop (`for` and `until` are forbidden)

### 8. For ls
**File:** `8-for_ls`

Write a Bash script that displays:
- The content of the current directory
- In a list format
- Where only the part of the name after the first dash is displayed

**Requirements:**
- You must use the `for` loop (`while` and `until` are forbidden)
- Do not display hidden files

### 9. To file, or not to file
**File:** `9-to_file_or_not_to_file`

Write a Bash script that gives you information about the `school` file.

**Requirements:**
- You must use `if` and, `else` (`case` is forbidden)
- Your Bash script should check if the file exists and print:
  - if the file exists: `school file exists`
  - if the file does not exist: `school file does not exist`
- If the file exists, print:
  - if the file is empty: `school file is empty`
  - if the file is not empty: `school file is not empty`
  - if the file is a regular file: `school is a regular file`
  - if the file is not a regular file: (nothing)

### 10. FizzBuzz
**File:** `10-fizzbuzz`

Write a Bash script that displays numbers from 1 to 100.

**Requirements:**
- Displays `FizzBuzz` when the number is a multiple of 3 and 5
- Displays `Fizz` when the number is multiple of 3
- Displays `Buzz` when the number is a multiple of 5
- Otherwise, displays the number
- In a list format

## Advanced Tasks

### 11. Read and cut
**File:** `100-read_and_cut`

Write a Bash script that displays the content of the file `/etc/passwd`.

**Requirements:**
- Your script should only display: username, user id, Home directory path for the user
- You must use the `while` loop (`for` and `until` are forbidden)

### 12. Tell the story of passwd
**File:** `101-tell_the_story_of_passwd`

Write a Bash script that displays the content of the file `/etc/passwd`, using the `while` loop + IFS.

**Format:** `The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO`

**Requirements:**
- You must use the `while` loop (`for` and `until` are forbidden)

### 13. Let's parse Apache logs
**File:** `102-lets_parse_apache_logs`

Write a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file.

**Requirements:**
- Format: `IP HTTP_CODE`
- in a list format
- You must use `awk`
- You are not allowed to use `while`, `for`, `until` and `if`

### 14. Dig the data
**File:** `103-dig_the-data`

Using what you did in the previous task, write a Bash script that groups visitors by IP and HTTP status code, and displays this data.

**Requirements:**
- The exact format must be: `OCCURENCE_NUMBER IP HTTP_CODE`
- In list format
- Ordered from the greatest to the lowest number of occurrences
- You must use `awk`
- You are not allowed to use `while`, `for`, `until` and `if`

## Resources

### Read or watch:
- [Loops sample](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
- [Variable assignment and arithmetic](https://tldp.org/LDP/abs/html/ops.html)
- [Comparison operators](https://tldp.org/LDP/abs/html/comparison-ops.html)
- [File test operators](https://tldp.org/LDP/abs/html/fto.html)
- [Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)

### man or help:
- `env`
- `cut`
- `for`
- `while`
- `until`
- `if`

## Key Concepts

### Loop Types

**For Loop:**
```bash
for variable in list
do
    commands
done
```

**While Loop:**
```bash
while [ condition ]
do
    commands
done
```

**Until Loop:**
```bash
until [ condition ]
do
    commands
done
```

### Conditional Statements

**If Statement:**
```bash
if [ condition ]
then
    commands
elif [ condition ]
then
    commands
else
    commands
fi
```

**Case Statement:**
```bash
case $variable in
    pattern1)
        commands
        ;;
    pattern2)
        commands
        ;;
    *)
        default commands
        ;;
esac
```

### File Test Operators
- `-e file`: file exists
- `-f file`: file is a regular file
- `-d file`: file is a directory
- `-s file`: file is not empty
- `-r file`: file is readable
- `-w file`: file is writable
- `-x file`: file is executable

### Comparison Operators
- `-eq`: equal to
- `-ne`: not equal to
- `-lt`: less than
- `-le`: less than or equal to
- `-gt`: greater than
- `-ge`: greater than or equal to

## Best Practices

1. **Always use `#!/usr/bin/env bash`** for portability
2. **Add descriptive comments** explaining what your script does
3. **Use meaningful variable names**
4. **Quote variables** to prevent word splitting
5. **Check your scripts with Shellcheck**
6. **Make scripts executable** with `chmod +x filename`
7. **Test scripts thoroughly** before submission

## Testing Your Scripts

```bash
# Make script executable
chmod +x script_name

# Run the script
./script_name

# Check with Shellcheck
shellcheck script_name
```

## Author

**[Your Name]**
- GitHub: [@yourusername](https://github.com/yourusername)
- ALX Student ID: [Your Student ID]

---

**ALX Software Engineering Program** | *0x04. Loops, conditions and parsing*
