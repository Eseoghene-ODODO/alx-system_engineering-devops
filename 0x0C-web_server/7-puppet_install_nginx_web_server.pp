# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
      listen 80;
      server_name _;

      location / {
        return 200 'Hello World!';
      }

      location /redirect_me {
        return 301 /redirected;
      }

      location /redirected {
        return 200 'You have been redirected.';
      }
    }
  ",
  notify => Service['nginx'],
}
