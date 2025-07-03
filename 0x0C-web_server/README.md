# 0x0C. Web Server

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests

### DNS
- What DNS stands for
- What is DNS main role

### DNS Record Types
- A
- CNAME
- TXT
- MX

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script does

## Background Context

In this project, some of the tasks will be graded on 2 aspects:

1. Is your web server configured correctly
2. Does your answer file contain a Bash script that automatically performs the task

For example, if you need to create a file `/tmp/test` containing the string `hello world` and modify the configuration of Nginx to listen on port 8080 instead of 80, you can use emacs on your server to create the file and to modify the Nginx configuration file `/etc/nginx/sites-enabled/default`.

But your answer file would contain:

```bash
#!/usr/bin/env bash
# This script creates a file and configures Nginx
echo "hello world" > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
```

As you can tell, I am not using emacs to perform the task in my answer file, but the command line and a script instead.

## Tasks

### 0. Transfer a file to your server
**mandatory**

Write a Bash script that transfers a file from our client to a server:

Requirements:
- Accepts 4 parameters
  1. The path to the file to be transferred
  2. The IP of the server we want to transfer the file to
  3. The username scp connects with
  4. The path to the SSH private key that scp uses
- Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
- `scp` must transfer the file to the user home directory `~/`
- Strict host key checking must be disabled when using scp

**File:** `0-transfer_file`

### 1. Install nginx web server
**mandatory**

Web servers are the piece of software generating and serving HTML pages, let's install one!

Requirements:
- Install `nginx` on your `web-01` server
- Nginx should be listening on port 80
- When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
- As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
- You can't use `systemctl` for restarting nginx

**File:** `1-install_nginx_web_server`

### 2. Setup a domain name
**mandatory**

[.TECH Domains](https://get.tech/) is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS.

.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your [tools space](https://intranet.alxswe.com/). Feel free to drop a thank you tweet for [.TECH Domains](https://twitter.com/dottechdomains).

Provide the domain name in your answer file.

Requirement:
- provide the domain name only (example: `foobar.tech`), no subdomain (example: `www.foobar.tech`)
- configure your DNS records with an A entry so that your root domain points to your `web-01` IP address **Warning: the propagation of your records can take time (~1-2 hours)**
- go to [your profile](https://intranet.alxswe.com/users/my_profile) and enter your domain in the `Project website url` field

**File:** `2-setup_a_domain_name`

### 3. Redirection
**mandatory**

Readme:
- [Replace a line with multiple lines with sed](https://stackoverflow.com/questions/26041088/replace-a-line-with-multiple-lines-with-sed)

Configure your Nginx server so that `/redirect_me` is redirecting to another page.

Requirements:
- The redirection must be a "301 Moved Permanently"
- Your answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
- Using what you did with `1-install_nginx_web_server`, write `3-redirection` so that it configures a brand new Ubuntu machine to the requirements asked in this task

**File:** `3-redirection`

### 4. Not found page 404
**mandatory**

Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.

Requirements:
- The page must return an HTTP 404 error code
- The page must contain the string `Ceci n'est pas une page`
- Using what you did with `3-redirection`, write `4-not_found_page_404` so that it configures a brand new Ubuntu machine to the requirements asked in this task

**File:** `4-not_found_page_404`

### 5. Install Nginx web server (w/ Puppet)
**#advanced**

Time to practice configuring your server with Puppet! Just as you did before, we'd like you to install and configure an Nginx server using Puppet instead of Bash.

Requirements:
- Nginx should be listening on port 80
- When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
- The redirection must be a "301 Moved Permanently"
- Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements

**File:** `7-puppet_install_nginx_web_server.pp`

## Resources

**Read or watch:**
- [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [Nginx](https://en.wikipedia.org/wiki/Nginx)
- [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-configure-nginx-to-serve-your-site)
- [Child process concept page](https://intranet.alxswe.com/concepts/110)
- [Root and sub domain](https://landingi.com/help/domains-vs-subdomains/)
- [HTTP requests](https://www.tutorialspoint.com/http/http_methods.htm)
- [HTTP redirection](https://moz.com/learn/seo/redirection)
- [Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)
- [Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)

**For reference:**
- [RFC 7231 (HTTP/1.1)](https://tools.ietf.org/html/rfc7231)
- [RFC 3986 (URI)](https://tools.ietf.org/html/rfc3986)

## Author

**Your Name**  
Software Engineer Student at ALX School

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.