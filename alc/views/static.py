from flask import Blueprint
from flask import render_template

bp = Blueprint('static', __name__, url_prefix='')


@bp.route('/')
def home():
    return render_template('home.j2')
