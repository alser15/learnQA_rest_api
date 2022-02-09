import pytest
import requests

from lib.assertions import Assertions
from lib.base_case import BaseCase

@pytest.fixture
def setup():
    data = {
        'email': 'vinkotov@example.com',
        'password': '1234'
    }
    response1 = requests.post('https://playground.learnqa.ru/api/user/login',
                              data=data)
    auth_sid = BaseCase.get_cookies(response1, 'auth_sid')
    t = response1.headers
    token = BaseCase.get_headers(response1, 'x-csrf-token')
    user_id_from_auth_method = BaseCase.get_json_value(response1, 'user_id')

    return (auth_sid, token, user_id_from_auth_method)


class TestAuthUser(BaseCase):
    exclude_params = [('no_cookie'), ('no_token')]

    def test_auth_user(self,setup):
        auth_sid, token, user_id_from_auth_method = setup
        response2 = requests.get(
            'https://playground.learnqa.ru/api/user/auth',
            headers={'x-csrf-token':token},
            cookies={'auth_sid': auth_sid})

        Assertions.assert_json_value_by_name(response2,
                                             'user_id',
                                             user_id_from_auth_method,
                                             'Не совпадают айди юзера')

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_user(self, setup, condition):
        auth_sid, token, user_id_from_auth_method = setup

        if condition == 'no_cookie':
            response2 = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                headers={'x-csrf-token':token})
        else:
            response2 = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                cookies={'auth_sid': auth_sid})

        Assertions.assert_json_value_by_name(
            response2, 'user_id', 0, f'Юзер авторизовался с условием '
                                     f'{condition}'
        )