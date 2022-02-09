import json.decoder

from requests import Response


class BaseCase:

    @staticmethod
    def get_cookies(response: Response, cookie_name):
        assert cookie_name in response.cookies,\
        f'Нет куки с именем {cookie_name} в последнем ответе'
        return response.cookies[cookie_name]

    @staticmethod
    def get_headers(response: Response, headers_name):
        s = response.headers
        assert headers_name in response.headers, \
                f'Нет заголовка с именем {headers_name} в последнем ответе'
        return response.headers[headers_name]

    @staticmethod
    def get_json_value(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert  False, f'Ответ не в формате JSON. Текст ответа ' \
                           f'{response.text}'
        assert name in response_as_dict, f"Ключа {name} нет в " \
                                         f"{response_as_dict}"
        return response_as_dict[name]
