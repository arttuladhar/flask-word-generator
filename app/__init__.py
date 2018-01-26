import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from random import randint

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object('config')
app.config['SECRET_KEY'] = '5accdb11b2c10a78d7c92c5fa102ea77fcd50c2058b00f6e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'words.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import views, models