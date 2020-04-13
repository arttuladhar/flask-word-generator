from flask import render_template
from flask import Blueprint
from flask.json import jsonify

bp = Blueprint('hello', __name__)

@bp.route('/hello')
def index():
  return jsonify({"message": "Hello User"})
