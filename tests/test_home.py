"""
    Flask API tests.
"""

from run import app


with app.test_client() as c:
    rv = c.get('/')             # pylint: disable=invalid-name
    json_data = rv.get_json()   # pylint: disable=invalid-name

    assert json_data == {
        'name': 'Flask API',
        'version': '0.0.1'
    }
