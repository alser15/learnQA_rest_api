def test_ex11():
    import requests
    cookie = dict(requests.get(
        'https://playground.learnqa.ru/api/homework_cookie').cookies)
    print(cookie)
    assert "HomeWork" in cookie, f"Нет ключа HomeWork в {cookie}"
    assert cookie["HomeWork"] == 'hw_value', f'Неверное значение' \
                                          f' MyCookie {cookie["HomeWork"]},' \
                                          f' ожидается 12345'
