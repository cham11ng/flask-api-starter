"""
    Configuration file.
"""

import os

from dotenv import load_dotenv
from os.path import join, dirname


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class Config(object):
    """Common config class."""

    APP_NAME = os.environ.get("APP_NAME")
    APP_VERSION = os.environ.get("APP_VERSION")

    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True
    FLASK_ENV = "development"


class ProductionConfig(Config):
    """Production configuration."""

    DEBUG = False
    FLASK_ENV = "production"


def get_config():
    config = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "default": DevelopmentConfig,
    }

    return config.get(os.environ.get("FLASK_ENV", "default"))
