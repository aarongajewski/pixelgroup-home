import requests


def test_signup_button():
    resp = requests.get('http://localhost:8000/')
    assert 'Try it now' in resp.text
