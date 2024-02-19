"""Flask API tests."""

import sys
import os
import pytest

from src.app import app


def test_home():
    with app.test_client() as client:
        rv = client.get("/")
        json_data = rv.get_json()

        assert json_data == {"name": "Flask API", "version": "0.1.0"}
