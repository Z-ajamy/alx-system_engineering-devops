# 0x0A. Configuration management

## Description
This project introduces configuration management using Puppet, a powerful automation tool for managing system configurations. You'll learn how to write Puppet manifests to automate server setup, software installation, and system configuration tasks. Configuration management is essential for maintaining consistency across multiple servers and environments.

## Learning Objectives
At the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- Intro to configuration management
- Puppet resource type: file
- Puppet's Declarative Language
- Puppet lint
- Puppet emacs mode

### Background Context
When I was working for SlideShare, I worked on an auto-remediation tool called Skynet that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server's hostname or any other metadata we had (server type, server environment...). At some point, a bug was present in my code that sent `nil` to the filter method.

There were 2 pieces of bad news:
1. When MCollective receives `nil` as an argument for its filter method, it takes this to mean 'all servers'
2. The action I sent was to terminate the selected servers

I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare's entire production infrastructure. Actually, 75% of all our servers were shut down, our 3 environment clusters: production, staging and dev, were affected.

Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways).

Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.

## Requirements

### General
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension `.pp`

### Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

### Install puppet
```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

### Install puppet-lint
```bash
$ gem install puppet-lint
```

## Tasks

### 0. Create a file
**File:** `0-create_a_file.pp`

Using Puppet, create a file in `/tmp`.

Requirements:
- File path is `/tmp/school`
- File permission is `0744`
- File owner is `www-data`
- File group is `www-data`
- File contains `I love Puppet`

**Example:**
```bash
root@6712bef7a528:~# puppet-lint --version
puppet-lint 2.1.1
root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
root@6712bef7a528:~# 
root@6712bef7a528:~# puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
root@6712bef7a528:~#
root@6712bef7a528:~# ls -l /tmp/school
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
root@6712bef7a528:~# cat /tmp/school
I love Puppetroot@6712bef7a528:~#
```

### 1. Install a package
**File:** `1-install_a_package.pp`

Using Puppet, install `flask` from `pip3`.

Requirements:
- Install `flask`
- Version must be `2.1.0`

**Example:**
```bash
root@9665f0a47391:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for 9665f0a47391 in environment production in 0.14 seconds
Notice: /Stage[main]/Main/Package[flask]/ensure: created
Notice: Finished catalog run in 0.20 seconds
root@9665f0a47391:/# flask --version
Python 3.8.10
Flask 2.1.0
Werkzeug 2.1.1
```

### 2. Execute a command
**File:** `2-execute_a_command.pp`

Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:
- Must use the `exec` Puppet resource
- Must use `pkill`

**Example:**
Terminal #0 - starting a process:
```bash
root@d391259bf577:/# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

root@d391259bf577:/# ./killmenow
```

Terminal #1 - executing our manifest:
```bash
root@d391259bf577:/# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
root@d391259bf577:/# 
```

Terminal #0 - process has been terminated:
```bash
root@d391259bf577:/# ./killmenow
Terminated
root@d391259bf577:/#
```

## Puppet Fundamentals

### What is Configuration Management?
Configuration management is the practice of handling changes systematically so that a system maintains its integrity over time. It involves:
- Maintaining consistency across multiple servers
- Automating system setup and configuration
- Ensuring reproducible deployments
- Managing infrastructure as code

### What is Puppet?
Puppet is a configuration management tool that uses a declarative language to describe system configuration. It allows you to:
- Define the desired state of your systems
- Automatically enforce that state
- Manage configurations across multiple machines
- Track and audit changes

### Puppet Architecture
- **Puppet Master**: Central server that stores configurations
- **Puppet Agent**: Runs on managed nodes, applies configurations
- **Manifests**: Files containing Puppet code (`.pp` files)
- **Resources**: Basic units of configuration (files, packages, services)
- **Catalog**: Compiled configuration for a specific node

## Puppet Language Basics

### Puppet Manifest Structure
```puppet
# Comment explaining what this manifest does
resource_type { 'resource_title':
  attribute => 'value',
  attribute => 'value',
}
```

### Common Resource Types

#### File Resource
```puppet
file { '/path/to/file':
  ensure  => present,        # or absent
  content => 'file content',
  owner   => 'username',
  group   => 'groupname',
  mode    => '0644',
  source  => 'puppet:///path/to/source',
}
```

#### Package Resource
```puppet
package { 'package_name':
  ensure   => present,       # or absent, latest, specific version
  provider => 'pip3',        # or apt, yum, etc.
}
```

#### Service Resource
```puppet
service { 'service_name':
  ensure => running,         # or stopped
  enable => true,            # start on boot
}
```

#### Exec Resource
```puppet
exec { 'command_name':
  command => '/path/to/command',
  path    => ['/bin', '/usr/bin'],
  unless  => 'test_command',
  onlyif  => 'test_command',
}
```

#### User Resource
```puppet
user { 'username':
  ensure => present,
  home   => '/home/username',
  shell  => '/bin/bash',
  uid    => '1001',
}
```

### Puppet Attributes
- **ensure**: Desired state (present, absent, running, stopped)
- **owner/group**: File ownership
- **mode**: File permissions
- **content**: File content (inline)
- **source**: File source (from puppet server)
- **path**: Search path for commands
- **command**: Command to execute

## Best Practices

### Manifest Organization
- Use meaningful resource titles
- Group related resources together
- Use consistent naming conventions
- Comment your code thoroughly

### Resource Ordering
```puppet
# Using before/require
package { 'apache2':
  ensure => present,
  before => Service['apache2'],
}

service { 'apache2':
  ensure  => running,
  require => Package['apache2'],
}

# Using arrows
Package['apache2'] -> Service['apache2']
Package['apache2'] ~> Service['apache2']  # notify relationship
```

### Variables and Facts
```puppet
# Variables
$package_name = 'apache2'
$config_file = '/etc/apache2/apache2.conf'

# Using facts
if $::osfamily == 'Debian' {
  $package_name = 'apache2'
} elsif $::osfamily == 'RedHat' {
  $package_name = 'httpd'
}
```

### Conditionals
```puppet
# If statement
if $::operatingsystem == 'Ubuntu' {
  package { 'apache2':
    ensure => present,
  }
}

# Case statement
case $::operatingsystem {
  'Ubuntu', 'Debian': {
    $package_name = 'apache2'
  }
  'CentOS', 'RedHat': {
    $package_name = 'httpd'
  }
  default: {
    fail("Unsupported OS: ${::operatingsystem}")
  }
}
```

## Puppet Lint

### What is Puppet Lint?
Puppet Lint is a tool that checks Puppet manifests against style guidelines and best practices.

### Common Lint Rules
- **Line length**: Keep lines under 140 characters
- **Indentation**: Use 2 spaces for indentation
- **Trailing whitespace**: Remove trailing spaces
- **Quotes**: Use single quotes unless interpolation is needed
- **Variables**: Use lowercase with underscores

### Running Puppet Lint
```bash
# Check a single file
puppet-lint manifest.pp

# Check all files in a directory
puppet-lint manifests/

# Auto-fix certain issues
puppet-lint --fix manifest.pp
```

## Testing and Validation

### Syntax Validation
```bash
# Check syntax
puppet parser validate manifest.pp

# Dry run (don't apply changes)
puppet apply --noop manifest.pp

# Apply manifest
puppet apply manifest.pp
```

### Debugging
```bash
# Verbose output
puppet apply --verbose manifest.pp

# Debug output
puppet apply --debug manifest.pp

# Test mode
puppet apply --test manifest.pp
```

## Common Patterns

### LAMP Stack Setup
```puppet
# Install packages
package { ['apache2', 'mysql-server', 'php']:
  ensure => present,
}

# Configure Apache
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Package['apache2'],
}

# Create virtual host
file { '/etc/apache2/sites-available/mysite.conf':
  ensure  => present,
  content => template('apache/vhost.conf.erb'),
  notify  => Service['apache2'],
}
```

### User Management
```puppet
# Create user with home directory
user { 'deploy':
  ensure     => present,
  home       => '/home/deploy',
  managehome => true,
  shell      => '/bin/bash',
}

# Create SSH key
file { '/home/deploy/.ssh':
  ensure  => directory,
  owner   => 'deploy',
  group   => 'deploy',
  mode    => '0700',
  require => User['deploy'],
}
```

## Troubleshooting

### Common Issues
1. **Permission denied**: Check file ownership and permissions
2. **Package not found**: Verify package name and repository
3. **Service won't start**: Check dependencies and configuration
4. **Syntax errors**: Use `puppet parser validate`

### Debugging Tips
- Use `--noop` flag to test without applying changes
- Check `/var/log/syslog` for error messages
- Verify resource dependencies
- Test manifests in isolation

## File Structure
```
0x0A-configuration_management/
├── README.md
├── 0-create_a_file.pp
├── 1-install_a_package.pp
└── 2-execute_a_command.pp
```

## Resources
Read or watch:
- [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
- [Puppet resource type: file](https://puppet.com/docs/puppet/5.5/types/file.html)
- [Puppet's Declarative Language: Modeling Instead of Scripting](https://puppet.com/blog/puppets-declarative-language-modeling-instead-of-scripting/)
- [Puppet lint](http://puppet-lint.com/)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

## Installation Commands Summary
```bash
# Install Puppet
sudo apt-get update
sudo apt-get install -y ruby=1:2.7+1 --allow-downgrades
sudo apt-get install -y ruby-augeas ruby-shadow puppet

# Install puppet-lint
sudo gem install puppet-lint

# Verify installation
puppet --version
puppet-lint --version
```

## Author
This project is part of the ALX Software Engineering Program.

## Repository
- **GitHub repository:** `alx-system_engineering-devops`
- **Directory:** `0x0A-configuration_management`