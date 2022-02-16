import datetime
import os

from requests import Response


class Logger:
    file_name = f'logs/log' + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + '.log'

    @classmethod
    def write_log_to_file(cls, data:str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url, data, headers, cookies, method):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        data_to_add = f'\n-----\n'
        data_to_add += f'Test: {test_name}\n'
        data_to_add += f'Time: {str(datetime.datetime.now())}\n'
        data_to_add += f'Request METHOD: {method}\n'
        data_to_add += f'Request URL: {url}\n'
        data_to_add += f'Request DATA: {data}\n'
        data_to_add += f'Request HEADERS: {headers}\n'
        data_to_add += f'Request COOKIES: {cookies}\n'
        data_to_add += f'\n'

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)

        data_add = f'Response CODE: {response.status_code}\n'
        data_add += f'Response TEXT: {response.text}\n'
        data_add += f'Response COOKIES: {cookies_as_dict}\n'
        data_add += f'Response HEADERS: {headers_as_dict}\n'
        data_add += f'\n-----\n'

        cls.write_log_to_file(data_add)