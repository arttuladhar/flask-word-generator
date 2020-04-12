import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.blueprints import Blueprint

import app.config
from app.routes import hello

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = '5accdb11b2c10a78d7c92c5fa102ea77fcd50c2058b00f6e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'words.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Index
@app.route('/')
def index():
  return "Hello User"

# Blueprint register
app.register_blueprint(hello.bp, url_prefix='/')
app.run(host=config.HOST, port=config.PORT)