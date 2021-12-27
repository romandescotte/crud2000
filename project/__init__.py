from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from project.config import Config#, devConfig

app=Flask(__name__)
#development environment
#app.config.from_object(devConfig)
#production environment
app.config.from_object(Config)

CORS(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)

from project import routes



