from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from flask_openid import OpenID
from config import basedir



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))


