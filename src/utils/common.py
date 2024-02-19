"""
Common utils of the application.
"""

from http import HTTPStatus
from http.client import responses
from flask import jsonify, current_app, make_response


def env(key, value=None):
    """Return environment variable.

    :param key: Key of environment variable.
    :type key: str
    :param value: Default value of environment variable, defaults to None
    :type value: any, optional
    :return: Environment variable value.
    :rtype: str
    """

    return current_app.config.get(key, value)


def json_response(data=None, status=HTTPStatus.OK, headers=None):
    """Generate json response with given payload, status and headers.

    :param data: Response data, defaults to None
    :type data: json, optional
    :param status: HTTP status code, defaults to HTTPStatus.OK
    :type status: http, optional
    :param headers: Headers payload, defaults to None
    :type headers: json, optional
    :return: JSON response
    :rtype: json
    """

    return make_response(jsonify(data), status, headers or {})


def enum_response(enum):
    """Jsonify error response from given enum.

    :param enum: Custom enum.
    :type enum: Enum
    :return: API error response.
    :rtype: json
    """

    code, data = enum.value[2:], env("MESSAGES")

    return json_response(
        {
            "code": enum.value,
            "message": data[enum.value] if enum.value in data else responses[code],
        },
        code,
    )
