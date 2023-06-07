# This manifest ensures that the wp-settings.php file for WordPress is present and has the correct content and permissions
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  source  => 'puppet:///modules/apache/wp-settings.php',
  require => Package['apache2'],
  notify  => Service['apache2'],
}
