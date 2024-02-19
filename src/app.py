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

with open("en.json", encoding="utf-8") as f:
    app.config.from_mapping(MESSAGES=json.load(f))


@app.route("/")
def home():
    """Controller to handle / request."""

    return jsonify(name=env("APP_NAME"), version=env("APP_VERSION")), HTTPStatus.OK


@app.route("/health", methods=["GET", "POST"])
def health():
    """Controller to handle health check."""
    if request.method == "GET":
        app.logger.debug("Request headers:")
        app.logger.debug({"args": request.args})
        return jsonify(data=request.args, method="GET"), HTTPStatus.OK

    if request.method == "POST":
        app.logger.debug("Request headers:")
        app.logger.debug({"json": request.json})

        return jsonify(data=request.json, method="POST"), HTTPStatus.OK

    abort(HTTPStatus.METHOD_NOT_ALLOWED)


@app.route("/dynamic/<string:url>")
def dynamic(url):
    """Controller to handle dynamic routes."""
    return jsonify(url=url), HTTPStatus.OK


@app.route("/error")
def error():
    """Controller to handle error."""
    data = 1 / 0
    app.logger.info(data)
    return jsonify(data=data), HTTPStatus.OK


@app.errorhandler(HTTPStatus.NOT_FOUND)
def not_found(err):
    """Error handler for not found exception."""
    app.logger.error(err)

    return enum_response(Codes.NOT_FOUND)


@app.errorhandler(HTTPStatus.METHOD_NOT_ALLOWED)
def method_not_allowed(err):
    """Error handler for method not allowed exception."""
    app.logger.error(err)

    return enum_response(Codes.METHOD_NOT_ALLOWED)


@app.errorhandler(Exception)
def server_error(err):
    """Error handler for server error."""
    app.logger.error(err)

    return enum_response(Codes.INTERNAL_SERVER_ERROR)


if __name__ == "__main__":
    app.run(debug=True)
