from . import db

class Word(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  wordName = db.Column(db.String(50), unique=True)

  def __init__(self, wordName):
      self.wordName = wordName
