# 0x02. Shell, I/O Redirections and filters

## Description
This project covers the fundamentals of shell I/O redirections and filters in Unix-like systems. You'll learn how to manipulate input and output streams, redirect data between commands, and use powerful filtering tools to process text and data efficiently.

## Learning Objectives
By the end of this project, you should be able to explain:

- What do the commands `head`, `tail`, `find`, `wc`, `sort`, `uniq`, `grep`, `tr` do
- How to redirect standard output to a file
- How to get standard input from a file instead of the keyboard
- How to send the output from one program to the input of another program
- How to combine commands and filters with redirections
- What are special characters and how to use them
- What is the difference between `>` and `>>`
- What is `/dev/null` and how to use it
- What are environment variables and how to display them

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All scripts will be tested on Ubuntu 20.04 LTS
- All scripts should be exactly two lines long (`wc -l file` should print 2)
- All files should end with a new line
- The first line of all files should be exactly `#!/bin/bash`
- A `README.md` file at the root of the project folder is mandatory
- You are not allowed to use backticks, `&&`, `||` or `;`
- All files must be executable
- You are not allowed to use `sed` or `awk`

### File Naming Convention
All script files should follow the naming pattern and be executable:
```bash
chmod +x filename
```

## Concepts Covered

### I/O Redirection
- **Standard Input (stdin)**: Input stream (file descriptor 0)
- **Standard Output (stdout)**: Output stream (file descriptor 1) 
- **Standard Error (stderr)**: Error stream (file descriptor 2)

### Redirection Operators
- `>`: Redirect stdout to file (overwrite)
- `>>`: Redirect stdout to file (append)
- `<`: Redirect stdin from file
- `2>`: Redirect stderr to file
- `2>&1`: Redirect stderr to stdout
- `&>`: Redirect both stdout and stderr to file

### Pipe Operator
- `|`: Send output of one command as input to another

### Common Filter Commands
- `cat`: Display file contents
- `head`: Display first lines of a file
- `tail`: Display last lines of a file
- `grep`: Search for patterns in text
- `sort`: Sort lines of text
- `uniq`: Remove duplicate lines
- `wc`: Count lines, words, and characters
- `tr`: Translate or delete characters
- `cut`: Extract columns from text
- `find`: Search for files and directories

## Examples

### Basic Redirection
```bash
# Redirect output to file
echo "Hello World" > hello.txt

# Append to file
echo "Second line" >> hello.txt

# Use file as input
cat < hello.txt
```

### Pipes and Filters
```bash
# Count lines in a file
cat file.txt | wc -l

# Sort and remove duplicates
cat names.txt | sort | uniq

# Search and count matches
grep "pattern" file.txt | wc -l
```

### Advanced Examples
```bash
# Find all .txt files and count them
find . -name "*.txt" | wc -l

# Display first 10 lines of sorted file
sort file.txt | head -10

# Remove duplicates and save to new file
sort file.txt | uniq > unique_lines.txt
```

## Tasks Overview
This directory contains shell scripts that demonstrate various I/O redirection and filtering techniques. Each script is designed to accomplish specific tasks using combinations of shell commands, redirections, and filters.

## File Structure
```
0x02-shell_io_redirections_filters/
├── README.md
├── 0-hello_world
├── 1-confused_smiley
├── 2-hellofile
├── 3-twofiles
├── 4-lastlines
├── 5-firstlines
├── 6-third_line
├── 7-file
├── 8-cwd_state
├── 9-duplicate_last_line
├── 10-no_more_js
└── [additional script files...]
```

## Usage
Each script can be executed directly:
```bash
./script_name
```

Or with bash:
```bash
bash script_name
```

## Testing
Test your scripts with various inputs and edge cases. Ensure they handle:
- Empty files
- Large files
- Special characters
- Non-existent files (where applicable)

## Resources
- [Shell I/O Redirection](https://www.gnu.org/software/bash/manual/bash.html#Redirections)
- [Bash Manual](https://www.gnu.org/software/bash/manual/)
- [Unix Text Processing Tools](https://en.wikipedia.org/wiki/List_of_Unix_commands)

## License
This project is part of the ALX Software Engineering Program curriculum.
