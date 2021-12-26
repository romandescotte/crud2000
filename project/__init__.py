from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app=Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://bdac5df4f61814:6aa32f11@us-cdbr-east-05.cleardb.net/heroku_abb3b37cb667098'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db= SQLAlchemy(app)
ma=Marshmallow(app)

from project import routes



