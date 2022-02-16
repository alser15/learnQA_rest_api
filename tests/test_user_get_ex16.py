import allure
from lib.assertions import Assertions
from lib.my_requests import MyRequests


@allure.epic('Case test user get')
class TestUserGet:

    @allure.description(' test user get')
    def test_user_get(self, create_login_delete_user):
        with allure.step('get user info'):
            inf_request = MyRequests.get(
                f'/user/{create_login_delete_user.json()["user_id"]}',
                headers={'x-csrf-token':create_login_delete_user.headers['x-csrf-token']},
                cookies={'auth_sid':dict(create_login_delete_user.cookies)['auth_sid']})
        with allure.step('check input in response'):
            Assertions.assert_json_values_by_names(inf_request, ['id',
                                                                 'username',
                                                                 'email',
                                                                 'firstName',
                                                                 'lastName'])
        with allure.step('request for get info about user, used not valid cookie'
                         ' and token'):
            bad_request = MyRequests.get(
                f'/user/2',
                headers={'x-csrf-token': create_login_delete_user.headers['x-csrf-token']},
                cookies={'auth_sid': dict(create_login_delete_user.cookies)['auth_sid']})
        with allure.step('ckeck answer'):
            assert bad_request.json() == {'username': 'Vitaliy'}, f'Неверный ответ ' \
                                                              f'{bad_request.json()}'