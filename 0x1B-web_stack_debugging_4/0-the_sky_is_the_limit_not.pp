# This Puppet manifest optimizes Nginx settings to handle high traffic
# filename: nginx.pp

file {'/etc/nginx/nginx.conf':
  ensure => file,
  content => "
  worker_processes  auto;
  worker_rlimit_nofile 100000;

  events {
    worker_connections  1024;
    use epoll;
  }

  http {
    client_max_body_size 100m;
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    server_tokens off;

    server {
      listen 80;
      server_name localhost;
      root /usr/share/nginx/html;
      index index.html;
      location / {
        try_files $uri $uri/ /index.html;
      }
    }
  }
  ",
}

exec { 'reload-nginx':
  command     => '/usr/sbin/service nginx reload',
  refreshonly => true,
}


