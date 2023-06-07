# Fixing error 500 in apache server with puppet
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  source  => 'puppet:///modules/apache/wp-settings.php',
  require => Package['apache2'],
  notify  => Service['apache2'],
}
