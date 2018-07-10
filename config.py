"""
    Configuration file.
"""

import os


class Config(object):
    """Common config class."""

    SECRET_KEY = os.environ.get('SECRET_KEY', '<SECRET_KEY>')

    APP_NAME = os.environ.get('APP_NAME', 'Flask API')
    APP_VERSION = os.environ.get('APP_VERSION', '0.0.1')


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True
    FLASK_ENV = 'development'


config = {  # pylint: disable=invalid-name
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}
