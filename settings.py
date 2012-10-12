#coding=utf-8

from flask import Flask
from flaskext.mongoalchemy import MongoAlchemy
from string import ascii_uppercase

app = Flask(__name__)
app.config['MONGOALCHEMY_SAFE_SESSION'] = False
app.config['DEBUG'] = True
#app.config['MONGOALCHEMY_SERVER'] = '118.122.117.134'
app.config['MONGOALCHEMY_SERVER'] = '216.12.198.98'
app.config['MONGOALCHEMY_DATABASE'] = 'opscm'
app.config['MONGOALCHEMY_PORT'] = 27017
app.config['MONGOALCHEMY_USER'] = 'opscm'
app.config['MONGOALCHEMY_PASSWORD'] = 'stm123'
app.config['MONGOALCHEMY_SERVER_AUTH'] = False

db = MongoAlchemy(app)
db.init_app(app)
