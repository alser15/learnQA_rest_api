import pytest
from lib.my_requests import MyRequests
from lib.assertions import Assertions
from lib.base_case import BaseCase


class TestAuthUser(BaseCase):
    exclude_params = [('no_cookie'), ('no_token')]

    def test_auth_user(self,setup):
        auth_sid, token, user_id_from_auth_method = setup
        response2 = MyRequests.get(
            '/user/auth',
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
            response2 = MyRequests.get(
                '/user/auth',
                headers={'x-csrf-token':token})
        else:
            response2 = MyRequests.get(
                '/user/auth',
                cookies={'auth_sid': auth_sid})

        Assertions.assert_json_value_by_name(
            response2, 'user_id', 0, f'Юзер авторизовался с условием '
                                     f'{condition}'
        )