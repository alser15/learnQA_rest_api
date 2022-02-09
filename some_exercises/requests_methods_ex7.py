# Задание 7
import requests
from json.decoder import JSONDecodeError



URL = 'https://playground.learnqa.ru/ajax/api/compare_query_type'
WRONG_ANSWER = 'Wrong method provided'
METHOD = ['GET','POST', 'PUT', 'DELETE']

# 1) Без параметра
print(requests.get(URL).text)
assert requests.get(URL).text == WRONG_ANSWER

# 2) С неправильным методом
response = requests.get(URL, params={"method":"head"}).text
print(response)
assert response == WRONG_ANSWER

# 3) С правильным методом
response = requests.get(URL, params={"method":METHOD[0]}).json()
print(response)
assert isinstance(response, dict)

# 4) С правильным методом
method_request = [requests.get,requests.post,requests.put,requests.delete]
success_answer = []
wrong_answer = []
for i in METHOD:
    for j in method_request:
        if j == method_request[0]:
            try:
                if isinstance(j(URL, params={"method":i}).json(),dict):
                    success_answer.append(j(URL, params={"method":i}).json())
                    print(f'Успешный ответ с методом {j} и параметром {i}')
            except JSONDecodeError:
                wrong_answer.append(j(URL, params={"method": i}).text)
        else:
            try:
                if isinstance(j(URL, data={"method": i}).json(), dict):
                    success_answer.append(j(URL, data={"method": i}).json())
                    print(f'Успешный ответ с методом {j} и датой {i}')
            except JSONDecodeError:
                wrong_answer.append(j(URL, data={"method": i}).text)

print(f'Успешных ответов {len(success_answer)}')
print(f'Неверных ответов {len(wrong_answer)}')