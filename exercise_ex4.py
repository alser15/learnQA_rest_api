import requests


def test_ex4():
    print(requests.get('https://playground.learnqa.ru/api/get_text').text)
