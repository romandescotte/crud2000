from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from project.config import Config

app=Flask(__name__)
app.config.from_object(Config)

CORS(app)

#aca iba el app.config que borre para que vaya por variables de entorno

db= SQLAlchemy(app)
ma=Marshmallow(app)

from project import routes



