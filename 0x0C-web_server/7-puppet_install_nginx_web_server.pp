# Start and enable Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => @(EOF)
server {
    listen 80;
    server_name 54.166.138.37;

    location / {
        return 200 'Hello World!';
    }

    location /redirect_me {
        return 301 http://$server_name/redirected;
    }

    location /redirected {
        return 200 'You have been redirected.';
    }
}
EOF
,
  notify  => Service['nginx'],
}
