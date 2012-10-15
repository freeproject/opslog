#!/usr/bin/env python
from pymongo import Connection, DESCENDING, ASCENDING


db_ip='localhost'
db_name='opscm'
db_col=['syslog.auth','syslog.cron','syslog.daemon','syslog.syslog','syslog.kern']

#connection = Connection()
connection = Connection("mongodb://user:passwd@ip/opscm")

db = connection[db_name]

def flush():
    # cols = db.collection_names()
    for col in db_col:
        #db[col].drop()
        db.drop_collection(col)

def create():
    for col in db_col:
        db.create_collection(col, capped=True, size=10737418240)   
        db[col].create_index([("time", DESCENDING), ('host',ASCENDING)])

flush()
#create()
