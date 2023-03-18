from flask import Blueprint, jsonify

test_bp = Blueprint('test', __name__)


@test_bp.route("/test")
def route_test():
    return jsonify({'a': 2})
