# This manifest ensures that the wp-settings.php file for WordPress is present and has the correct content and permissions

# Declare the apache module
include apache

# Manage the wp-settings.php file
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  source  => 'puppet:///modules/apache/wp-settings.php',
  require => Package['apache2'], # Require the apache2 package
  notify  => Service['apache2'], # Notify the apache2 service
}
