from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(50), unique=True)

  def __repr__(self):
    return '<User %r>' % self.email

class Word(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  wordName = db.Column(db.String(50), unique=True)