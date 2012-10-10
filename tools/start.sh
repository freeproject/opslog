#!/bin/bash
#author:syshack
#usage start.sh nginx/mongo

start_nginx()
{
    /opt/nginx/sbin/nginx
}
start_mongo()
{
    /opt/mongodb/bin/mongod -f  /opt/mongodb/etc/mongo.conf
}
OPT_=$1
case "$OPT_" in
    mongo)
        start_mongo  &
        ;;

    nginx)
        start_nginx
        ;;
esac
