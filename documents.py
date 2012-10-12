#coding=utf-8
from settings import db
from flaskext.mongoalchemy import BaseQuery
import re

class RegexQuery(BaseQuery):

    def regexp(self, host='', message='', bdate='', edate=''):
        host = r'.*' + host + r'.*'
        message = r'.*' + message + r'.*'
        return self.filter({'host': re.compile(host, re.IGNORECASE),
                            'message': re.compile(message, re.IGNORECASE),
                            'time': {"$gte": bdate, "$lt": edate}})


class syslog(db.Document):

    query_class = RegexQuery

    host = db.StringField()
    ident = db.StringField()
    pid = db.StringField()
    message = db.StringField()
    time = db.DateTimeField()
