import allure
import requests

from lib.logger import Logger


class MyRequests:
    @staticmethod
    def get(url: str,
            data: dict=None,
            headers: dict=None,
            cookies: dict=None):
        with allure.step(f'Отправит GET запрос на {url}'):
            return MyRequests.send_request(url, data, headers, cookies, 'GET')

    @staticmethod
    def post(url: str,
            data: dict = None,
            headers: dict = None,
            cookies: dict = None):
        with allure.step(f'Отправит POST запрос на {url}'):
            return MyRequests.send_request(url, data, headers, cookies, 'POST')

    @staticmethod
    def put(url: str,
            data: dict = None,
            headers: dict = None,
            cookies: dict = None):
        with allure.step(f'Отправит PUT запрос на {url}'):
            return MyRequests.send_request(url, data, headers, cookies, 'PUT')

    @staticmethod
    def delete(url: str,
            data: dict = None,
            headers: dict = None,
            cookies: dict = None):
        with allure.step(f'Отправит DELETE запрос на {url}'):
            return MyRequests.send_request(url, data, headers, cookies, 'DELETE')

    @staticmethod
    def send_request(url: str,
              data: dict,
              headers: dict,
              cookies: dict,
              method: str):
        url = f'https://playground.learnqa.ru/api{url}'

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_request(url, data, headers, cookies, method)
        if method == "GET":
            response = requests.get(url,
                                    params=data,
                                    headers=headers,
                                    cookies=cookies)
        elif method == "POST":
            response = requests.post(url,
                                    data=data,
                                    headers=headers,
                                    cookies=cookies)
        elif method == "PUT":
            response = requests.put(url,
                                    data=data,
                                    headers=headers,
                                    cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url,
                                    params=data,
                                    headers=headers,
                                    cookies=cookies)
        else:
            raise Exception(f'Неверный метод {method}')

        Logger.add_response(response)

        return response
