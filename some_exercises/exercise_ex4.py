import requests


def test_ex4():
    print(requests.get(
        'http://schemas.xmlsoap.org/soap/envelope/'
    ).text)
