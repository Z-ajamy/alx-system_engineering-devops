# Define an exec resource to fix a typo in the WordPress configuration file
exec { 'Fix WordPress site':
  # Command to be executed: uses sed to replace '.phpp' with '.php' in wp-settings.php
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',

  # Specify the provider to use for execution
  provider => shell,
}
