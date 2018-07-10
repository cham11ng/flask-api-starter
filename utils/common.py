'''
    Common utils of the application.
'''

from flask import current_app


def env(key, value=None):
    """Return environment variable.

    Arguments:
        key {str} -- Key of environment variable.

    Keyword Arguments:
        value {any} -- Default value of environment variable (default: {None})

    Returns:
        str -- Environment variable value.
    """

    return current_app.config.get(key, value)
