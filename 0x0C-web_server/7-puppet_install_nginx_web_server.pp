# A Puppet manifest that installs and configures Nginx with a redirect.

# Step 1: Ensure the package list is updated before installing anything.
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin/',
}

# Step 2: Ensure the Nginx package is installed.
# This requires the apt-update command to have run first.
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-update'],
}

# Step 3: Ensure the Hello World page exists with the correct content.
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
  require => Package['nginx'], # Ensure this runs after Nginx is installed
}

# Step 4: Manage the entire default Nginx configuration file.
# This ensures it has our redirect and removes any unwanted default settings.
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm;

	server_name _;

	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

	location / {
		try_files \$uri \$uri/ =404;
	}
}
",
  require => Package['nginx'], # Ensure Nginx is installed before managing its config
}

# Step 5: Ensure the Nginx service is running and enabled.
# It will automatically restart if the config file it 'subscribes' to changes.
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'], # Restart if the config file changes
  require   => Package['nginx'],
}
