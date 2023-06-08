# Puppet code to fix wordpress configuration file in apache2 error

file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => inline_template('<%= File.read("/var/www/html/wp-settings.php").gsub(/\.phpp/, ".php") %>'),
}
