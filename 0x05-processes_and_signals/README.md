# 0x05. Processes and signals

## Description
This project explores process management and signal handling in Unix-like systems. You'll learn how to create, monitor, and control processes, understand process identification, and work with signals to communicate between processes.

## Learning Objectives
By the end of this project, you should be able to explain:

- What is a PID (Process ID)
- What is a process
- How to find a process' PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored
- How to create and manage background processes
- How to use job control commands
- What happens when you press `Ctrl+C` and `Ctrl+Z`
- How to handle signals in shell scripts
- What is the difference between a program and a process

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- All Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.7.0) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does

### Bash Scripts
- You are not allowed to use `kill` command with a number (e.g., `kill -9`)
- You must use `kill` command with signal names when required

## Concepts Covered

### Processes
- **Process**: A running instance of a program
- **PID (Process ID)**: Unique identifier for each process
- **PPID (Parent Process ID)**: PID of the parent process
- **Process States**: Running, Sleeping, Stopped, Zombie
- **Foreground vs Background**: Process execution modes

### Process Management Commands
```bash
# Display running processes
ps                    # Show processes for current user
ps aux               # Show all processes with detailed info
ps -ef               # Show all processes in full format

# Display process tree
pstree               # Show processes in tree format

# Monitor processes in real-time
top                  # Interactive process viewer
htop                 # Enhanced interactive process viewer

# Find processes
pgrep pattern        # Find PIDs by name pattern
pidof program        # Find PID of running program
```

### Job Control
```bash
# Background processes
command &            # Run command in background
jobs                 # List active jobs
bg %1                # Put job 1 in background
fg %1                # Bring job 1 to foreground

# Process control
Ctrl+C               # Send SIGINT (interrupt)
Ctrl+Z               # Send SIGTSTP (suspend)
Ctrl+\               # Send SIGQUIT (quit with core dump)
```

### Signals
Signals are software interrupts used for inter-process communication.

#### Common Signals
| Signal | Number | Default Action | Description |
|--------|--------|----------------|-------------|
| SIGHUP | 1 | Terminate | Hangup detected on controlling terminal |
| SIGINT | 2 | Terminate | Interrupt from keyboard (Ctrl+C) |
| SIGQUIT | 3 | Core dump | Quit from keyboard (Ctrl+\) |
| SIGKILL | 9 | Terminate | Kill signal (cannot be caught) |
| SIGTERM | 15 | Terminate | Termination signal |
| SIGSTOP | 19 | Stop | Stop process (cannot be caught) |
| SIGTSTP | 20 | Stop | Terminal stop signal (Ctrl+Z) |
| SIGCONT | 18 | Continue | Continue if stopped |

#### Uncatchable Signals
- **SIGKILL (9)**: Cannot be caught, blocked, or ignored
- **SIGSTOP (19)**: Cannot be caught, blocked, or ignored

### Signal Commands
```bash
# Send signals to processes
kill PID             # Send SIGTERM to process
kill -SIGNAL PID     # Send specific signal
kill -9 PID          # Send SIGKILL (force kill)
kill -HUP PID        # Send SIGHUP (hangup)
kill -TERM PID       # Send SIGTERM (terminate)

# Kill processes by name
killall process_name # Kill all processes with name
pkill pattern        # Kill processes matching pattern

# Send signals to process groups
kill -SIGNAL -PGID   # Send signal to process group
```

### Signal Handling in Scripts
```bash
#!/usr/bin/env bash
# Script demonstrating signal handling

# Define signal handler function
cleanup() {
    echo "Cleaning up..."
    exit 0
}

# Trap signals
trap cleanup SIGINT SIGTERM

# Main script logic
while true; do
    echo "Running..."
    sleep 1
done
```

## Examples

### Process Information
```bash
# Find PID of a process
ps aux | grep nginx
pgrep nginx
pidof nginx

# Kill a process
kill 1234
kill -TERM 1234
killall nginx

# Background process management
sleep 100 &          # Run in background
jobs                 # List background jobs
kill %1              # Kill job 1
```

### Signal Handling
```bash
# Trap script to handle signals
#!/usr/bin/env bash
# Handle SIGINT and SIGTERM gracefully

trap 'echo "Received SIGINT"; exit 0' SIGINT
trap 'echo "Received SIGTERM"; exit 0' SIGTERM

while true; do
    echo "Working..."
    sleep 2
done
```

### Advanced Process Management
```bash
# Monitor specific process
watch -n 1 'ps aux | grep myprocess'

# Check if process is running
if pgrep -x "myprocess" > /dev/null; then
    echo "Process is running"
else
    echo "Process is not running"
fi

# Start process if not running
pgrep -x "myprocess" || myprocess &
```

## Tasks Overview
This directory contains scripts and programs that demonstrate various aspects of process management and signal handling. Each task focuses on specific process control techniques and signal manipulation.

## File Structure
```
0x05-processes_and_signals/
├── README.md
├── 0-what-is-my-pid
├── 1-list_your_processes
├── 2-show_your_bash_pid
├── 3-show_your_bash_pid_made_easy
├── 4-to_infinity_and_beyond
├── 5-dont_stop_me_now
├── 6-stop_me_if_you_can
├── 7-highlander
├── 8-beheaded_process
├── 100-process_and_pid_file
├── 101-manage_my_process
├── 102-zombie.c
└── manage_my_process
```

## Common Use Cases

### Daemon Process Management
```bash
# Start daemon
./my_daemon &
echo $! > /var/run/my_daemon.pid

# Stop daemon
kill $(cat /var/run/my_daemon.pid)
rm /var/run/my_daemon.pid

# Check daemon status
if kill -0 $(cat /var/run/my_daemon.pid) 2>/dev/null; then
    echo "Daemon is running"
fi
```

### Process Monitoring
```bash
# Monitor process resource usage
while true; do
    ps -p $PID -o pid,ppid,cmd,%mem,%cpu
    sleep 5
done

# Alert when process dies
while kill -0 $PID 2>/dev/null; do
    sleep 1
done
echo "Process $PID has terminated"
```

## Best Practices

### Signal Handling
- Always handle SIGTERM gracefully in long-running processes
- Use SIGKILL only when SIGTERM fails
- Implement proper cleanup in signal handlers
- Avoid doing complex operations in signal handlers

### Process Management
- Store PIDs in files for daemon processes
- Check if processes are still running before attempting operations
- Use appropriate signals for different situations
- Implement proper error handling

## Debugging

### Process Debugging
```bash
# Trace system calls
strace -p PID

# Debug with gdb
gdb -p PID

# Monitor file descriptors
lsof -p PID

# Check process limits
cat /proc/PID/limits
```

### Signal Debugging
```bash
# Send test signals
kill -USR1 PID       # User-defined signal 1
kill -USR2 PID       # User-defined signal 2

# Monitor signals
strace -e trace=signal -p PID
```

## Resources
- [Linux Process Management](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/cgroups.html)
- [Signal Handling in Linux](https://man7.org/linux/man-pages/man7/signal.7.html)
- [Advanced Programming in the UNIX Environment](https://stevens.com/)
- [Bash Manual - Job Control](https://www.gnu.org/software/bash/manual/bash.html#Job-Control)

## License
This project is part of the ALX Software Engineering Program curriculum.