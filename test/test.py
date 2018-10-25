import requests


def test_signup_button():
    resp = requests.get('http://chris-demo-alb-1402233261.us-east-1.elb.amazonaws.com/')
    assert 'Try it now' in resp.text
