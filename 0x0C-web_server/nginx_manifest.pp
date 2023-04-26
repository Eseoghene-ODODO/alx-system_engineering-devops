class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => file,
    content => "server {\n  listen 80;\n  server_name _;\n  location / {\n    return 200 'Hello World!';\n  }\n  location /redirect_me {\n    return 301 https://one-techschool.tech;\n  }\n}\n",
    require => Package['nginx'],
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => File['/etc/nginx/sites-enabled/default'],
  }
}

class { 'nginx': }
