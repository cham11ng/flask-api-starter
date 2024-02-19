"""

Flask API starting point.
"""

import json
from http import HTTPStatus

from flask import Flask, jsonify, request, abort

from config import get_config
from src.enums.codes import Codes
from src.utils.common import env, enum_response

app = Flask(__name__)
app.config.from_object(get_config())

with open("en.json") as f:
    app.config.from_mapping(MESSAGES=json.load(f))


@app.route("/")
def home():
    """Controller to handle / request."""

    return jsonify(name=env("APP_NAME"), version=env("APP_VERSION")), 200


@app.route("/health", methods=["GET", "POST"])
def health():
    app.logger.debug("Request headers:")
    app.logger.debug({"json": request.json, "args": request.args})

    if request.method == "GET":
        return jsonify(status="OK", method="GET"), 200

    if request.method == "POST":
        return jsonify(status="OK", method="POST"), 200


@app.route("/dynamic/<string:url>")
def dynamic(url):
    """Controller to handle dynamic routes."""
    return jsonify(url=url), 200


@app.route("/error")
def err():
    """Controller to handle error."""
    err = 1 / 0
    app.logger.info(err)


@app.errorhandler(HTTPStatus.NOT_FOUND)
def not_found(err):
    """Error handler for not found exception."""

    return enum_response(Codes.NOT_FOUND)


@app.errorhandler(Exception)
def not_found(err):
    """Error handler for server error."""
    app.logger.error(err)

    return enum_response(Codes.INTERNAL_SERVER_ERROR)


if __name__ == "__main__":
    app.run(debug=True)
