"""
    Flask API starting point.
"""

from flask import Flask, jsonify

from config import config
from utils.common import env


app = Flask(__name__)   # pylint: disable=invalid-name
app.config.from_object(config['development'])


@app.route('/')
def home():
    """Controller to handle / request."""

    return jsonify(name=env('APP_NAME'), version=env('APP_VERSION'))


if __name__ == '__main__':
    app.run(debug=True)
