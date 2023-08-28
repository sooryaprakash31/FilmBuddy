from flask import Blueprint

controller = Blueprint('controller', __name__)


@controller.route('/recommend/', methods=['GET'])
def recommend():
    return "ok"
