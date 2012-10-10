#=============================================================================
#       Author: Eric Zhang
#        Email: zhang.chuan@ymail.com
#      LICENCE: Copyright (c) 2012 ,Eric Zhang
#   LastChange: 2012-10-10 09:27:02
#=============================================================================
from pymongo import Connection, DESCENDING, ASCENDING


db_ip='localhost'
db_name='opscm'
db_col=['auth','cron','daemon','syslog','kern']

connection = Connection("mongodb://@%s/%s" %
                           (db_ip,
                            db_name)
                       )

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
create()
