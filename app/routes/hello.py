from flask import render_template
from flask import Blueprint

bp = Blueprint('hello', __name__)

# Index
@bp.route('/hello')
def index():
  return "Hello API"
