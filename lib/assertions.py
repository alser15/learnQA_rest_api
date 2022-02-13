import json

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
        assert name in response_as_dict, f"Нет ключа {name} в " \
                                         f"{response_as_dict}"
        assert response_as_dict[name] == expected_value, error_massage

    @staticmethod
    def assert_response_text(response: Response, expected_value,
                             error_massage):
        assert response.text == expected_value, error_massage

    @staticmethod
    def assert_json_values_by_names(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Ответ не в формате json, текст ответа " \
                          f"{response.text}"
        for name in names:
            assert name in response_as_dict, f"Нет ключа {name} в " \
                                             f"{response_as_dict}"
