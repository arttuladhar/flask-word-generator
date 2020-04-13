from app.models.User import User
from app.utils.db import db

def get_all_users_db():
  return User.query.all()

def createUser(email):
  newUser = User(email)
  db.session.add(newUser)
  db.session.commit()