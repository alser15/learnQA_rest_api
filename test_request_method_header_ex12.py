def test_ex12():
    import requests
    header = requests.get(
        'https://playground.learnqa.ru/api/homework_header').headers
    print(header)
    values = [header[i] for i in header]
    for i in range(len(header)):
        assert header[list(header)[i]] == values[i],\
            f'Значение {header[list(header)[i]]} не соответствует {values[i]}'
