from flask import render_template, request, redirect, url_for

from forms import AddWordForm, SignupNewsLetter
from models import User, Word

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


# Index
@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html', user="Minneapolis", year="2018")

# Hello
@app.route('/hello')
def hello():
    return "Hello, Flask"

# Add Words
@app.route('/add', methods=['GET', 'POST'])
def add_words():
  form = AddWordForm()

  if request.method == "POST":
    word = request.form['word']
    add_word(word)
    app.logger.debug("Stored Word: " + word)

  return render_template('add.html', form=form)


# GET Word
@app.route('/word')
def get_word():
  return render_template('getWords.html', word=get_random_word())

# GET All Word
@app.route('/words-all')
def get_all_word():
  return render_template('getAllWords.html', words=get_all_words_db())


@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.route('/signup-newsletter', methods=['GET', 'POST'])
def signup_newsletter():
  form = SignupNewsLetter()
  if request.method == "POST":
    if form.validate_on_submit():
      form_email = form.userEmail.data
      user = User(email=form_email)
      db.session.add(user)
      db.session.commit()
      app.logger.debug("Saving to DB")
      return redirect(url_for('index'))

  return render_template('signup_newsletter.html', form=form)