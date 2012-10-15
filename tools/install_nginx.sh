#!/bin/bash
#author:syshack
arch=`uname -m`
SRCDIR=/usr/local/src/opslog
if [ ! -d "$SRCDIR" ]; 
  then 
    mkdir -p "$SRCDIR" 
fi 
cd $SRCDIR
#INSTALL NGINX
echo "Start Install Nginx"
wget -c http://nginx.org/download/nginx-1.3.7.tar.gz
cd $SRCDIR
tar -xvf nginx-1.3.7.tar.gz
cd nginx-1.3.7
./configure --prefix=/opt/nginx
make && make install 
cat > /opt/nginx/conf/nginx.conf << EOF
    worker_processes  1;
    events {
        worker_connections  1024;
    }
    http {
        include       mime.types;
        default_type  application/octet-stream;
        sendfile        on;
        keepalive_timeout  65;
        server {
            listen       80;
            server_name  0.0.0.0;
        root /data/project/opslog/static;
            location / { 
            include uwsgi_params; 
            uwsgi_pass unix:/tmp/uwsgi.sock; 
            }
        }
    }
EOF
cp init.d-nginx /etc/rc.d/init.d/nginx
chmod +x /etc/rc.d/init.d/nginx
echo "****Complete****" 