from flask import Blueprint, jsonify


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(400)
def invalid_data(error):
    error_list = []
    if isinstance(error.description, list):
        for error_message in error.description:
            error_list.append(error_message)
    else:
        error_list.append(error.description)
    return jsonify({"message": error_list}), 400


@errors.app_errorhandler(404)
def not_found(error):
    return jsonify({"message": error.description}), 404
