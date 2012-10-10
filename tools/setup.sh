#!/usr/bin/env bash
echo "Download Mongo"
arch = `uname -m`
SRCDIR = /usr/local/src/opslog
if [ ! -d "$SRCDIR"]; 
  then 
    mkdir "$SRCDIR" 
fi 
wget -c -P  $SRCDIR http://fastdl.mongodb.org/linux/mongodb-linux-$arch-2.2.0.tgz
tar -xvf $SRCDIR/mongodb* 
