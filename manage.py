#! /usr/bin/env python

from app import app, db
from flask_script import Manager, prompt_bool

manager = Manager(app)

@manager.command
def initdb():
  db.create_all()
  print ("Initialized Database")

@manager.command
def dropdb():
  if prompt_bool("Are you sure you want to delete all your data"):
    db.drop_all()
    print ("Dropped Database")

if __name__ == '__main__':
  manager.run()