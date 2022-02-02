import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect')

# Кол-во редиректов
print(len(response.history))

# url первого редиректа
print(response.history[0].url)
assert response.history[0].status_code == 301

# url второго редиректа
print(response.history[1].url)
assert response.history[1].status_code == 301

# url третьего редиректа
print(response.history[2].url)
assert response.history[2].status_code == 301

# конечный url
print(response.url)
assert response.status_code == 200