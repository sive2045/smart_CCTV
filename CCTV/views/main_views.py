from flask import Blueprint, render_template, url_for
#from CCTV.modules.motion_sense import motion_detect_mode

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def inedx():
    return render_template('html/main.html')


@bp.route('/detected', methods=['POST'])
def detected():
    print("움직임 감지!")
    return '정상적인 감지', 200
