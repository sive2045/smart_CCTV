from flask import Blueprint

bp = Blueprint('main',__name__, url_prefix='/')

@bp.route('/')
def inedx():
    return 'indxe page!'

@bp.route('/home')
def home():
    return 'home page!'