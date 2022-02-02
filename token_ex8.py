import requests
import time
URL = 'https://playground.learnqa.ru/ajax/api/longtime_job'

cookie = requests.get(URL).json()
assert isinstance(cookie, dict)

print(requests.get(URL, params={"token":cookie['token']}).text)
assert requests.get(URL, params={"token":cookie['token']}).json()["status"] == \
        "Job is NOT ready"
time.sleep(7)
print(requests.get(URL, params={"token":cookie['token']}).text)
assert requests.get(URL, params={"token":cookie['token']}).json()["result"] == \
        "42"
assert requests.get(URL, params={"token":cookie['token']}).json()["status"] == \
        "Job is ready"
