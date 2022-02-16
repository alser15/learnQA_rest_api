import json
import allure
from requests import Response


class Assertions:

    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value,
                                  error_massage):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Ответ не в формате json, текст ответа " \
                          f"{response.text}"
        with allure.step(f'assert {name} in {response_as_dict}'):
            assert name in response_as_dict, f"Нет ключа {name} в " \
                                             f"{response_as_dict}"
        with allure.step(f'assert {response_as_dict[name]} equil {expected_value}'):
            assert response_as_dict[name] == expected_value, error_massage

    @staticmethod
    def assert_response_text(response: Response, expected_value,
                             error_massage):
        with allure.step(f'assert {response.text} equil {expected_value}'):
            assert response.text == expected_value, error_massage

    @staticmethod
    def assert_json_values_by_names(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Ответ не в формате json, текст ответа " \
                          f"{response.text}"
        with allure.step(f'assert {names} in {response_as_dict}'):
            for name in names:
                assert name in response_as_dict, f"Нет ключа {name} в " \
                                                 f"{response_as_dict}"

    @staticmethod
    def assert_type_obj(response: Response, class_):
        with allure.step(f'assert type response {class_}'):
            assert isinstance(response, class_), f'Неверный тип {response}, ожидается,' \
                                                 f'{class_}'

    @staticmethod
    def assert_status_code(response: Response, code):
        with allure.step(f'assert status code {code}'):
            assert response.status_code == code, f'Неверный код ответа {response.status_code},' \
                                             f'Ожидается {code}'