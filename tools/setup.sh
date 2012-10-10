#!/bin/bash
#author:syshack
arch=`uname -m`
SRCDIR=/usr/local/src/opslog
if [ ! -d "$SRCDIR" ]; 
  then 
    mkdir -p "$SRCDIR" 
fi 
#INSTALL MONGODB
cd $SRCDIR
echo "Download Mongo"
wget -c http://fastdl.mongodb.org/linux/mongodb-linux-$arch-2.2.0.tgz
echo "****Install Mongo****"
tar -xvf $SRCDIR/mongodb* -C /opt/
mv -f /opt/mongodb-linux-${arch}-2.2.0 /opt/mongodb

cat > /opt/mongodb/etc/mongo.conf << EOF
logpath=/var/log/mongod.log
rest=true
logappend=true
# fork and run in background
fork = true
port = 27017
dbpath=/opt/mongodb/data
journal = true
EOF
mkdir /opt/mongodb/{data,etc}
echo "****COMPLETE****"
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
echo "****Complete****"  