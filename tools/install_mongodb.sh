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
mkdir /opt/mongodb/{data,etc}
cp init.d-mongod /etc/rc.d/init.d/mongod
chmod +x /etc/rc.d/init.d/mongod
cat > /opt/mongodb/etc/mongo.conf << EOF
logpath=/var/log/mongod.log
auth=true
rest=true
logappend=true
# fork and run in background
fork = true
port = 27017
dbpath=/opt/mongodb/data
journal = true
EOF

echo "****COMPLETE****"
 