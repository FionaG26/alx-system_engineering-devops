# Puppet manifest to install and configure Nginx server

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx server
file { '/etc/nginx/nginx.conf':
  ensure  => 'file',
  content => "
    # Your Nginx configuration here
    # Example:
    worker_processes auto;
    events {
      worker_connections 2000;
    }
    http {
      include mime.types;
      default_type application/octet-stream;

      sendfile on;
      keepalive_timeout 120;

      server {
        listen 80;
        server_name localhost;

        location / {
          root /path/to/your/web/root;
          index index.html;
          keepalive_requests 100;
        }
      }
    }
  ",
  notify  => Service['nginx'],
}

# Restart Nginx service when configuration changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/nginx.conf'],
}

