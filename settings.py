#!/usr/bin/env python
#coding=utf-8

######
from flask import Flask
from flaskext.mongoalchemy import MongoAlchemy
from string import ascii_uppercase

app = Flask(__name__)
app.config['MONGOALCHEMY_SAFE_SESSION'] = False
app.config['MONGOALCHEMY_SERVER'] = 'localhost'
app.config['MONGOALCHEMY_DATABASE'] = 'opscm'
app.config['MONGOALCHEMY_PORT'] = 27017
app.config['DEBUG'] = True
db = MongoAlchemy(app)
db.init_app(app)
