# 0x14. MySQL

## Description
This project focuses on setting up and managing MySQL databases in a distributed environment. You'll learn about database replication, backup strategies, and how to implement master-slave replication for data redundancy and high availability. Understanding MySQL administration is crucial for managing production databases and ensuring data integrity.

## Concepts
For this project, you should understand:
- **MySQL basics**
- **Database replication**
- **Master-Slave architecture**
- **Database backup and recovery**
- **Replication users and privileges**
- **Binary logs**

## Background Context
In production environments, you cannot afford to have a single point of failure for your database. MySQL replication allows you to:
- Create backups without stopping the database
- Distribute read queries across multiple servers
- Implement high availability solutions
- Ensure data redundancy

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file at the root of the folder of the project is mandatory
- All your Bash script files must be executable
- Your Bash scripts must pass `Shellcheck` without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script does

## Your Servers

| Name | Username | IP | State |
|------|----------|-----|-------|
| [STUDENT_ID]-db-01 | ubuntu | XXX.XXX.XXX.XXX | running |
| [STUDENT_ID]-db-02 | ubuntu | XXX.XXX.XXX.XXX | running |

## Tasks

### 0. Install MySQL
**File:** `0-install_mysql`

First, let's get MySQL installed on both `db-01` and `db-02`.

**Requirements:**
- MySQL must be installed on both servers
- MySQL version must be 5.7.x
- The MySQL service must be running on both servers
- You do not need to replicate any database, just install the software

**Installation Steps:**
```bash
# Update package list
sudo apt-get update

# Install MySQL 5.7
sudo apt-get install -y mysql-server-5.7

# Start MySQL service
sudo service mysql start

# Enable MySQL on boot
sudo systemctl enable mysql

# Verify installation
mysql --version
sudo service mysql status
```

---

### 1. Let us in!
**File:** `1-create_user`

Create a MySQL user named `holberton_user` on both servers with the host wildcard `%` that can connect from anywhere.

**Requirements:**
- Create user `holberton_user` with password (choose a strong password)
- User must have host `%` (allow connection from any host)
- User must have REPLICATION CLIENT privilege
- User must be able to check replication status

**SQL Commands:**
```sql
-- Create user with password
CREATE USER 'holberton_user'@'%' IDENTIFIED BY 'your_password_here';

-- Grant REPLICATION CLIENT privilege
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'%';

-- Apply privileges
FLUSH PRIVILEGES;

-- Verify user creation
SELECT User, Host FROM mysql.user WHERE User='holberton_user';

-- Check privileges
SHOW GRANTS FOR 'holberton_user'@'%';
```

**Testing Connection:**
```bash
# From any machine (replace with actual IP)
mysql -h db-01_ip -u holberton_user -p

# Or using the script method
mysql -h localhost -u holberton_user -p -e "SELECT 1"
```

---

### 2. MySQL backup
**File:** `2-create_read_replica`

Create a script that generates a MySQL dump to backup the database.

**Requirements:**
- Create a dump of the current database
- The dump file must include all databases
- The dump should be in SQL format
- Include comments with the timestamp

**Backup Script Example:**
```bash
#!/usr/bin/env bash
# Script to create a MySQL backup

# Set variables
BACKUP_DIR="/home/ubuntu/backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
DUMP_FILE="${BACKUP_DIR}/backup_${TIMESTAMP}.sql"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Create dump (this requires credentials)
mysqldump -u root -p --all-databases --single-transaction > "$DUMP_FILE"

# Or using root without password (if configured)
mysqldump -u root --all-databases --single-transaction > "$DUMP_FILE"

# Verify backup
if [ -f "$DUMP_FILE" ]; then
    echo "Backup created successfully: $DUMP_FILE"
else
    echo "Backup failed!"
    exit 1
fi
```

---

## MySQL Replication

### Master-Slave Replication Overview

**What is Replication?**
MySQL replication allows data from one database (master) to be replicated to one or more databases (slaves). This provides:
- Data redundancy
- Read scaling
- Backup without stopping the master
- High availability

### Architecture

```
Master (db-01)
    ↓ (Binary Log)
    ↓ (Replication)
Slave (db-02)
    ↓
Read replicas / Backups
```

### Replication Process

1. **Master writes data** - Data is written to master database
2. **Binary Log** - Changes are recorded in binary log on master
3. **Replication Channel** - Slave connects to master using replication user
4. **IO Thread** - Slave's IO thread reads from master's binary log
5. **Relay Log** - Slave stores copied binary log events
6. **SQL Thread** - Slave's SQL thread replays events on slave database

### Types of Replication

#### 1. Statement-Based Replication (SBR)
- Replicates SQL statements
- Smaller log files
- Can be non-deterministic

#### 2. Row-Based Replication (RBR)
- Replicates actual row changes
- More storage, more network traffic
- Fully deterministic
- MySQL 5.7+ default

#### 3. Mixed Replication
- Uses both SBR and RBR
- Automatic decision based on statement

---

## Setting Up Master-Slave Replication

### Step 1: Configure Master (db-01)

#### Edit MySQL Configuration
```bash
# Edit /etc/mysql/mysql.conf.d/mysqld.cnf
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf

# Add or modify these settings:
[mysqld]
server-id = 1                          # Unique ID for master
log_bin = /var/log/mysql/mysql-bin.log  # Enable binary logging
binlog_do_db = database_name           # Database to replicate (optional)
binlog_ignore_db = mysql               # Ignore mysql system database
```

#### Restart MySQL
```bash
sudo service mysql restart
```

#### Create Replication User
```sql
-- Login to MySQL
mysql -u root -p

-- Create replication user
CREATE USER 'replication_user'@'%' IDENTIFIED BY 'replication_password';

-- Grant replication privileges
GRANT REPLICATION SLAVE ON *.* TO 'replication_user'@'%';

-- Apply privileges
FLUSH PRIVILEGES;

-- Verify
SHOW GRANTS FOR 'replication_user'@'%';
```

#### Get Master Status
```sql
-- Get binary log position (IMPORTANT!)
SHOW MASTER STATUS;

-- Output example:
-- File: mysql-bin.000003
-- Position: 1234
-- Binlog_Do_DB: database_name
-- Binlog_Ignore_DB: mysql
-- Executed_Gtid_Set:
```

**Note:** Keep this information! You'll need it for the slave.

### Step 2: Backup Master Database

```bash
# Create dump from master
mysqldump -u root -p --all-databases --single-transaction \
  --quick --lock-tables=false > /home/ubuntu/backup.sql
```

### Step 3: Transfer Backup to Slave

```bash
# On master
scp /home/ubuntu/backup.sql ubuntu@db-02_ip:/home/ubuntu/

# Or on slave
scp ubuntu@db-01_ip:/home/ubuntu/backup.sql /home/ubuntu/
```

### Step 4: Configure Slave (db-02)

#### Edit MySQL Configuration
```bash
# Edit /etc/mysql/mysql.conf.d/mysqld.cnf
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf

# Add or modify:
[mysqld]
server-id = 2                          # Different from master
relay-log = /var/log/mysql/mysql-relay-bin
relay-log-index = /var/log/mysql/mysql-relay-bin.index
log_bin = /var/log/mysql/mysql-bin.log  # Optional: for cascading replication
binlog_do_db = database_name           # Same as master
```

#### Restart MySQL
```bash
sudo service mysql restart
```

#### Import Master Backup
```bash
# Restore the backup on slave
mysql -u root -p < /home/ubuntu/backup.sql
```

#### Configure Slave Replication
```sql
-- Login to slave MySQL
mysql -u root -p

-- Configure replication with master information
CHANGE MASTER TO
  MASTER_HOST='db-01_ip',
  MASTER_USER='replication_user',
  MASTER_PASSWORD='replication_password',
  MASTER_LOG_FILE='mysql-bin.000003',    -- From SHOW MASTER STATUS
  MASTER_LOG_POS=1234;                   -- From SHOW MASTER STATUS

-- Start slave
START SLAVE;

-- Check slave status
SHOW SLAVE STATUS\G
```

### Verifying Replication

```sql
-- On slave, check replication status
SHOW SLAVE STATUS\G

-- Important fields:
-- Slave_IO_Running: Yes       <- Should be YES
-- Slave_SQL_Running: Yes      <- Should be YES
-- Seconds_Behind_Master: 0    <- Should be 0 or small number
-- Last_Error:                 <- Should be empty
```

---

## MySQL Binary Logs

### What are Binary Logs?
Binary logs record all changes to databases except for SELECT statements. They're essential for:
- Replication
- Point-in-time recovery
- Auditing

### Viewing Binary Logs

```bash
# List binary log files
sudo ls -la /var/log/mysql/mysql-bin.*

# Show binary log events
mysqlbinlog /var/log/mysql/mysql-bin.000003

# Show events from specific position
mysqlbinlog --start-position=1234 /var/log/mysql/mysql-bin.000003
```

### Binary Log Configuration

```ini
# In /etc/mysql/mysql.conf.d/mysqld.cnf
[mysqld]
# Enable binary logging
log_bin = /var/log/mysql/mysql-bin.log

# Maximum log file size (default 1GB)
max_binlog_size = 100M

# Which databases to log
binlog_do_db = production_db

# Which databases to ignore
binlog_ignore_db = mysql
binlog_ignore_db = test

# Expire logs after N days
expire_logs_days = 7

# Replication format (ROW, STATEMENT, or MIXED)
binlog_format = ROW
```

---

## MySQL Users and Privileges

### User Syntax

```sql
-- Create user with password
CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';

-- Host options
'username'@'localhost'       -- Only local connections
'username'@'192.168.1.100'   -- Specific IP
'username'@'192.168.1.%'     -- Subnet
'username'@'%'               -- Any host (remote access)
```

### Essential Privileges for Replication

```sql
-- Replication user
GRANT REPLICATION SLAVE ON *.* TO 'replication_user'@'%';

-- Replication monitoring user
GRANT REPLICATION CLIENT ON *.* TO 'monitoring_user'@'%';

-- Application user (read/write specific database)
GRANT SELECT, INSERT, UPDATE, DELETE ON database_name.* TO 'app_user'@'%';

-- All privileges on database
GRANT ALL PRIVILEGES ON database_name.* TO 'admin_user'@'localhost';

-- All privileges on all databases
GRANT ALL PRIVILEGES ON *.* TO 'root_user'@'localhost' WITH GRANT OPTION;
```

### Managing Users

```sql
-- List all users
SELECT User, Host FROM mysql.user;

-- Show user privileges
SHOW GRANTS FOR 'username'@'hostname';

-- Update user password
SET PASSWORD FOR 'username'@'hostname' = PASSWORD('new_password');
-- Or (MySQL 5.7.6+)
ALTER USER 'username'@'hostname' IDENTIFIED BY 'new_password';

-- Delete user
DROP USER 'username'@'hostname';

-- Rename user (MySQL 5.7.8+)
RENAME USER 'old_name'@'hostname' TO 'new_name'@'hostname';
```

---

## MySQL Backup Strategies

### Full Backups

```bash
# Backup all databases
mysqldump -u root -p --all-databases --single-transaction > full_backup.sql

# Backup specific database
mysqldump -u root -p database_name > database_backup.sql

# With compression
mysqldump -u root -p database_name | gzip > database_backup.sql.gz

# Parallel dump (MySQL 5.7.11+)
mysqldump -u root -p --all-databases --single-transaction --parallel=4 > full_backup.sql
```

### Incremental Backups

```bash
# Using binary logs for incremental backup
mysqlbinlog --start-position=154 /var/log/mysql/mysql-bin.000003 > incremental_backup.sql
```

### Backup Best Practices

```bash
# Lock-free backup (InnoDB)
mysqldump -u root -p --all-databases --single-transaction --quick

# Options explained:
# --single-transaction: Consistent snapshot without locks
# --quick: Minimal memory usage
# --lock-tables=false: Don't lock tables
# --events: Include scheduled events
# --routines: Include stored procedures
```

### Backup Verification

```bash
# Check dump integrity
mysql -u root -p -e "mysql < full_backup.sql" 2>&1 | head -20

# Restore to test server
mysql -u root -p < full_backup.sql
```

---

## Common Issues and Solutions

### Issue 1: Slave Cannot Connect to Master
```
Error: "Can't connect to MySQL server on 'master_ip'"
```

**Solutions:**
```bash
# 1. Check network connectivity
ping master_ip
telnet master_ip 3306

# 2. Check MySQL is listening on network
sudo netstat -tuln | grep 3306

# 3. Check firewall allows 3306
sudo ufw allow 3306

# 4. Verify user can connect
mysql -h master_ip -u replication_user -p
```

### Issue 2: Slave Out of Sync
```
Seconds_Behind_Master: Large number or NULL
```

**Solutions:**
```sql
-- Check slave status for errors
SHOW SLAVE STATUS\G

-- If there's an error, skip it
-- WARNING: Only in test environments!
SET GLOBAL SQL_SLAVE_SKIP_COUNTER = 1;
START SLAVE;

-- Or restart replication
STOP SLAVE;
START SLAVE;
```

### Issue 3: Binary Log Fills Disk

**Solution:**
```bash
# Check log file sizes
sudo du -sh /var/log/mysql/

# Set expiration in config
# expire_logs_days = 7

# Or manually delete old logs
# PURGE BINARY LOGS BEFORE DATE_SUB(NOW(), INTERVAL 7 DAY);

sudo service mysql restart
```

### Issue 4: Replication Lag

**Causes:**
- Slow master queries
- Network issues
- Large transactions
- Slave hardware too slow

**Solutions:**
```bash
# Check master load
# Use parallel replication (MySQL 5.7+)
# Optimize queries
# Upgrade slave hardware
```

### Issue 5: Cannot Write to Relay Log

**Solution:**
```bash
# Check permissions
sudo ls -la /var/log/mysql/

# Fix permissions
sudo chown mysql:mysql /var/log/mysql
sudo chmod 750 /var/log/mysql

# Restart MySQL
sudo service mysql restart
```

---

## MySQL Commands Reference

### Connection and Database

```bash
# Connect to MySQL
mysql -u username -p
mysql -h hostname -u username -p database_name

# Execute command and exit
mysql -u root -p -e "SHOW DATABASES;"

# Execute script file
mysql -u root -p < script.sql

# Export to file
mysql -u root -p database_name > dump.sql
```

### Database Operations

```sql
-- Show databases
SHOW DATABASES;

-- Select database
USE database_name;

-- Show tables
SHOW TABLES;

-- Show table structure
DESCRIBE table_name;
SHOW CREATE TABLE table_name\G

-- Show storage engine
SHOW TABLE STATUS\G
```

### User and Privilege Operations

```sql
-- Show current user
SELECT USER();

-- Show privileges
SHOW GRANTS FOR 'username'@'host';

-- Flush privileges
FLUSH PRIVILEGES;
```

### Replication Operations

```sql
-- Master
SHOW MASTER STATUS;
SHOW BINARY LOGS;

-- Slave
SHOW SLAVE STATUS\G
SHOW RELAY LOG EVENTS;
START SLAVE;
STOP SLAVE;

-- Replication info
SHOW PROCESSLIST;
```

---

## Configuration File Locations

### MySQL Configuration Files

```bash
# Main configuration
/etc/mysql/mysql.conf.d/mysqld.cnf

# Additional configurations
/etc/mysql/conf.d/
/etc/mysql/mysql.conf.d/

# Ubuntu specific
/etc/default/mysql

# Data directory
/var/lib/mysql

# Log files
/var/log/mysql

# Binary logs
/var/log/mysql/mysql-bin.*

# Relay logs (slave)
/var/log/mysql/mysql-relay-bin.*
```

### Configuration Best Practices

```ini
[mysqld]
# Server
server-id = 1                    # Unique per server
pid-file = /var/run/mysqld/mysqld.pid
socket = /var/run/mysqld/mysqld.sock
datadir = /var/lib/mysql

# Logging
log_error = /var/log/mysql/error.log
log-bin = /var/log/mysql/mysql-bin.log
binlog_format = ROW
expire_logs_days = 7

# Performance
max_connections = 1000
thread_cache_size = 128
innodb_buffer_pool_size = 50%_of_RAM
innodb_log_file_size = 512M

# Replication
relay-log = /var/log/mysql/mysql-relay-bin
relay-log-index = /var/log/mysql/mysql-relay-bin.index
skip-slave-start                # Don't auto-start replication
```

---

## Security Best Practices

### 1. Strong Passwords
```sql
-- Use strong passwords
CREATE USER 'user'@'%' IDENTIFIED BY 'StrongP@ssw0rd123!';
```

### 2. Restrict User Access
```sql
-- Don't use wildcard for sensitive operations
GRANT REPLICATION SLAVE ON *.* TO 'replication'@'db-02_ip';

-- Not
GRANT REPLICATION SLAVE ON *.* TO 'replication'@'%';
```

### 3. Principle of Least Privilege
```sql
-- Give only necessary privileges
GRANT SELECT, INSERT, UPDATE ON app_db.* TO 'app_user'@'app_server';

-- Not
GRANT ALL PRIVILEGES ON *.* TO 'app_user'@'%';
```

### 4. Remove Default Users
```sql
-- Remove anonymous users
DELETE FROM mysql.user WHERE User='';

-- Remove root remote access
DELETE FROM mysql.user WHERE User='root' AND Host!='localhost';

-- Flush privileges
FLUSH PRIVILEGES;
```

### 5. Enable Binary Logging
```ini
# For security and disaster recovery
log-bin = /var/log/mysql/mysql-bin.log
```

---

## Monitoring and Troubleshooting

### Monitor Replication Status

```bash
#!/usr/bin/env bash
# Script to monitor replication status

mysql -u root -p -e "SHOW SLAVE STATUS\G" | grep -E "Slave_IO_Running|Slave_SQL_Running|Seconds_Behind_Master|Last_Error"
```

### Check Server Status

```bash
# Service status
sudo service mysql status

# Process status
sudo systemctl status mysql

# Port listening
sudo netstat -tuln | grep 3306

# Disk usage
du -sh /var/lib/mysql
du -sh /var/log/mysql
```

### View Error Logs

```bash
# Error log
sudo tail -f /var/log/mysql/error.log

# Filter errors
sudo grep ERROR /var/log/mysql/error.log
```

---

## Testing Your Setup

### Test Replication

```bash
# On master, create test data
mysql -u root -p -e "CREATE DATABASE test_replication;"
mysql -u root -p -e "CREATE TABLE test_replication.test_table (id INT PRIMARY KEY, name VARCHAR(100));"
mysql -u root -p -e "INSERT INTO test_replication.test_table VALUES (1, 'test');"

# Verify on slave
mysql -u root -p -e "SELECT * FROM test_replication.test_table;"

# Should show the same data
```

### Connection Test

```bash
# Test holberton_user connection
mysql -h db-01_ip -u holberton_user -p -e "SELECT 1;"

# Should return 1
```

---

## Resources

- [MySQL Replication Documentation](https://dev.mysql.com/doc/refman/5.7/en/replication.html)
- [MySQL Installation Guide](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/)
- [MySQL User and Privileges](https://dev.mysql.com/doc/refman/5.7/en/user-account-management.html)
- [MySQL Backup and Recovery](https://dev.mysql.com/doc/refman/5.7/en/backup-and-recovery.html)
- [Binary Logs](https://dev.mysql.com/doc/refman/5.7/en/binary-log.html)

## Author
This project is part of the ALX Software Engineering Program.

## License
This project is licensed under the terms of the ALX Software Engineering Program.
