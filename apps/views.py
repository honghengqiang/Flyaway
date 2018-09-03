from flask import Blueprint

bp = Blueprint("front", __name__, )


@bp.route('/')
def hello_world():
    return 'Hello World!'
