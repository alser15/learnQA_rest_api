import pytest
from lib.my_requests import MyRequests
from lib.assertions import Assertions
from lib.base_case import BaseCase
import allure


@allure.epic('Case auth user')
class TestAuthUser(BaseCase):
    exclude_params = [('no_cookie'), ('no_token')]

    @allure.description('Test auth user')
    def test_auth_user(self,setup):
        auth_sid, token, user_id_from_auth_method = setup
        with allure.step(f'auth with {auth_sid}, {token}, {user_id_from_auth_method}'):
            response2 = MyRequests.get(
                '/user/auth',
                headers={'x-csrf-token':token},
                cookies={'auth_sid': auth_sid})
        with allure.step('assert value response'):
            Assertions.assert_json_value_by_name(response2,
                                                 'user_id',
                                                 user_id_from_auth_method,
                                                 'Не совпадают айди юзера')

    @allure.description('Test auth user')
    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_user(self, setup, condition):
        auth_sid, token, user_id_from_auth_method = setup
        with allure.step(f'auth with {auth_sid}, {token}, {user_id_from_auth_method}'):
            if condition == 'no_cookie':
                response2 = MyRequests.get(
                    '/user/auth',
                    headers={'x-csrf-token':token})
            else:
                response2 = MyRequests.get(
                    '/user/auth',
                    cookies={'auth_sid': auth_sid})
        with allure.step('assert response'):
            Assertions.assert_json_value_by_name(
                response2, 'user_id', 0, f'Юзер авторизовался с условием '
                                         f'{condition}'
            )