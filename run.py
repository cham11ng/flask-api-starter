"""
    Flask API starting point.
"""

from flask import Flask, jsonify


app = Flask(__name__)  # pylint: disable=invalid-name


@app.route('/')
def home():
    """Controller to handle / request."""

    return jsonify(name='Flask API', version='0.0.1')


if __name__ == '__main__':
    app.run(debug=True)
