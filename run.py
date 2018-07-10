"""
    Flask API starting point.
"""

import json
from http import HTTPStatus

from flask import Flask, jsonify

from config import config
from enums.codes import Codes
from utils.common import env, enum_response

app = Flask(__name__)   # pylint: disable=invalid-name
app.config.from_object(config['development'])

with open('en.json') as f:
    app.config.from_mapping(MESSAGES=json.load(f))


@app.route('/')
def home():
    """Controller to handle / request."""

    return jsonify(name=env('APP_NAME'), version=env('APP_VERSION'))


@app.errorhandler(HTTPStatus.NOT_FOUND)
def not_found(err):
    """Error handler for not found exception."""

    return enum_response(Codes.NOT_FOUND)


if __name__ == '__main__':
    app.run(debug=True)
