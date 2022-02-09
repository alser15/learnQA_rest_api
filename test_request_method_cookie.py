def test_ex11():
    import requests
    cookie = dict(requests.get(
        'https://playground.learnqa.ru/api/get_cookie').cookies)
    print(cookie)
    assert "MyCookie" in cookie, f"Нет ключа MyCookie в {cookie}"
    assert cookie["MyCookie"] == '12345', f'Неверное значение' \
                                          f' MyCookie {cookie["MyCookie"]},' \
                                          f' ожидается 12345'
