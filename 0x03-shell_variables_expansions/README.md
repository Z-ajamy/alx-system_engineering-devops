# 0x03. Shell, variables and expansions

## Description
This project explores shell variables, expansions, and initialization files in Unix-like systems. You'll learn how to create, manipulate, and use variables, understand different types of expansions, and work with shell initialization files to customize your environment.

## Learning Objectives
By the end of this project, you should be able to explain:

- What happens when you type `$ ls -l *.txt`
- What are the `/etc/profile` file and the `/etc/profile.d` directory
- What is the `~/.bashrc` file
- What is the difference between a local and a global variable
- What is a reserved variable
- How to create, update and delete shell variables
- What are the roles of the following reserved variables: `HOME`, `PATH`, `PS1`
- What are special parameters
- What is the special parameter `$?`
- What is expansion and how to use expansions
- What is the difference between single and double quotes and how to use them properly
- How to do command substitution with `$()` and backticks

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All scripts will be tested on Ubuntu 20.04 LTS
- All scripts should be exactly two lines long (`wc -l file` should print 2)
- All files should end with a new line
- The first line of all files should be exactly `#!/bin/bash`
- A `README.md` file at the root of the project folder is mandatory
- You are not allowed to use `&&`, `||` or `;`
- You are not allowed to use `bc`, `sed` or `awk`
- All files must be executable

### File Naming Convention
All script files should follow the naming pattern and be executable:
```bash
chmod +x filename
```

## Concepts Covered

### Shell Variables
- **Local Variables**: Available only in current shell session
- **Global Variables**: Available to current shell and child processes
- **Environment Variables**: System-wide variables available to all processes
- **Reserved Variables**: Special variables with predefined meanings

### Variable Operations
```bash
# Create/Set variable
VARIABLE_NAME="value"

# Access variable
echo $VARIABLE_NAME
echo ${VARIABLE_NAME}

# Export to environment
export VARIABLE_NAME

# Unset variable
unset VARIABLE_NAME
```

### Reserved Variables
- `$HOME`: User's home directory
- `$PATH`: Executable search path
- `$PS1`: Primary prompt string
- `$PWD`: Current working directory
- `$USER`: Current username
- `$SHELL`: Current shell
- `$?`: Exit status of last command
- `$$`: Process ID of current shell
- `$!`: Process ID of last background command

### Special Parameters
- `$0`: Name of the script
- `$1, $2, ...`: Positional parameters
- `$#`: Number of positional parameters
- `$@`: All positional parameters as separate words
- `$*`: All positional parameters as single word

### Expansions

#### Parameter Expansion
```bash
${parameter}           # Basic expansion
${parameter:-default}  # Use default if unset
${parameter:=default}  # Set default if unset
${parameter:+alternate} # Use alternate if set
${#parameter}          # Length of parameter
```

#### Command Substitution
```bash
$(command)    # Modern syntax
`command`     # Legacy syntax (backticks)
```

#### Arithmetic Expansion
```bash
$((expression))    # Arithmetic evaluation
$[expression]      # Legacy arithmetic (deprecated)
```

#### Brace Expansion
```bash
{a,b,c}        # Expands to: a b c
{1..10}        # Expands to: 1 2 3 4 5 6 7 8 9 10
file{1,2,3}.txt # Expands to: file1.txt file2.txt file3.txt
```

#### Pathname Expansion (Globbing)
```bash
*        # Matches any string
?        # Matches any single character
[abc]    # Matches any character in brackets
[a-z]    # Matches any character in range
```

### Quoting
- **Single Quotes (`'`)**: Preserve literal value of all characters
- **Double Quotes (`"`)**: Preserve literal value except `$`, backticks, and `\`
- **Backslash (`\`)**: Escape single character

## Examples

### Variable Usage
```bash
# Local variable
name="John"
echo "Hello $name"

# Environment variable
export PATH="$PATH:/new/directory"

# Using reserved variables
echo "Current user: $USER"
echo "Home directory: $HOME"
echo "Last command status: $?"
```

### Expansions
```bash
# Parameter expansion
file="document.txt"
echo "${file%.txt}.pdf"  # Output: document.pdf

# Command substitution
current_date=$(date)
echo "Today is $current_date"

# Arithmetic expansion
result=$((5 + 3))
echo "5 + 3 = $result"
```

### Quoting Examples
```bash
# Single quotes - no expansion
echo 'The user is $USER'  # Output: The user is $USER

# Double quotes - expansion occurs
echo "The user is $USER"  # Output: The user is john

# Mixed quoting
echo 'Hello' "$USER"      # Output: Hello john
```

## Shell Initialization Files

### System-wide Files
- `/etc/profile`: Executed for login shells
- `/etc/bash.bashrc`: Executed for interactive non-login shells
- `/etc/profile.d/`: Directory containing additional initialization scripts

### User-specific Files
- `~/.bash_profile`: User's login shell initialization
- `~/.bash_login`: Alternative login shell initialization
- `~/.profile`: POSIX-compliant login shell initialization
- `~/.bashrc`: Interactive non-login shell initialization
- `~/.bash_logout`: Executed when login shell exits

### Execution Order
1. **Login Shell**: `/etc/profile` → `~/.bash_profile` → `~/.bash_login` → `~/.profile`
2. **Interactive Non-login**: `/etc/bash.bashrc` → `~/.bashrc`

## Tasks Overview
This directory contains shell scripts demonstrating various aspects of shell variables, expansions, and environment manipulation. Each script showcases specific techniques for working with variables and expansions.

## File Structure
```
0x03-shell_variables_expansions/
├── README.md
├── 0-alias
├── 1-hello_you
├── 2-path
├── 3-paths
├── 4-global_variables
├── 5-local_variables
├── 6-create_local_variable
├── 7-create_global_variable
├── 8-true_knowledge
├── 9-divide_and_rule
├── 10-love_exponent_breath
└── [additional script files...]
```

## Common Commands
```bash
# Display environment variables
env
printenv

# Display all variables (including local)
set

# Display specific variable
echo $VARIABLE_NAME
printenv VARIABLE_NAME

# Create alias
alias ll='ls -la'

# Remove alias
unalias ll
```

## Usage
Each script can be executed directly:
```bash
./script_name
```

Or sourced to affect current shell:
```bash
source script_name
. script_name
```

## Testing
Test your scripts with:
- Different variable values
- Special characters in variables
- Undefined variables
- Various quoting scenarios

## Debugging Tips
```bash
# Enable debugging
set -x

# Check variable existence
if [ -z "$VARIABLE" ]; then
    echo "Variable is empty or unset"
fi

# Display all variables starting with specific prefix
env | grep "^PREFIX"
```

## Resources
- [Bash Manual - Shell Variables](https://www.gnu.org/software/bash/manual/bash.html#Shell-Variables)
- [Bash Manual - Shell Expansions](https://www.gnu.org/software/bash/manual/bash.html#Shell-Expansions)
- [Advanced Bash Scripting Guide](https://tldp.org/LDP/abs/html/)

## License
This project is part of the ALX Software Engineering Program curriculum.
