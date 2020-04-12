from app.repositories import Word
from app import app, db


"""
Store Word to Database
"""
def add_word(word):
  word = Word(wordName = word)
  db.session.add(word)
  db.session.commit()
  return

"""
Get Random Work from Database
"""
def get_all_words_db():
  return Word.query.all()

"""
Get Random Work from Database
"""
def get_random_word():
  words = Word.query.all()

  return words[2]