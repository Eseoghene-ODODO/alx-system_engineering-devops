#!/usr/bin/env ruby
# A script that Install Nginx web server (w/ Puppet)


# Install Nginx package
class { 'nginx':
  ensure => installed,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => "server {\n  listen 80;\n  server_name _;\n  location / {\n    return 200 'Hello World!';\n  }\n  location /redirect_me {\n    return 301 https://one-techschool.tech;\n  }\n}\n",
  require => Package['nginx'],
}

# Reload Nginx to apply the configuration changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-enabled/default'],
}
