from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired
from wtforms.validators import Email

class AddWordForm(FlaskForm):
  word = StringField('word', validators=[DataRequired()])

class SignupNewsLetter(FlaskForm):
  userEmail = StringField('email', validators=[DataRequired(), Email()])