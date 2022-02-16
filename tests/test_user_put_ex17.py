import allure
from lib.assertions import Assertions
from lib.my_requests import MyRequests


@allure.epic('Case put user')
class TestUserPut:

    @allure.description('Тест изменения юзера без авторизации')
    def test_change_data_user_without_auth(self, create_login_delete_user):
        """
        Тест изменения юзера без авторизации
        """
        with allure.step('Send PUT request'):
            response = MyRequests.put(f'/user/{create_login_delete_user.json()["user_id"]}',
                                      data={'username':'Vanay'})
        with allure.step('check response'):
            Assertions.assert_response_text(response, 'Auth token not supplied',
                                            'Неверный текст ответа')

    @allure.description('Тест изменения юзера, используя куки  и токен другого юзера')
    def test_change_data_user_with_auth_another_user(self, create_login_delete_user):
        """
        Тест изменения юзера, используя куки  и токен другого юзера
        """
        with allure.step('Send PUT request witch invalid user'):
            response = MyRequests.put(f'/user/2',
                data={'email': 'ololo'},
                headers={'x-csrf-token':create_login_delete_user.headers['x-csrf-token']},
                cookies={'auth_sid':dict(create_login_delete_user.cookies)['auth_sid']})
        with allure.step('check response'):
            assert response.status_code == 400, f'Неверный код ответа {response.status_code}'

    @allure.description('Тест смены мейла на невалидный (без @)')
    def test_change_email_invalid(self, create_login_delete_user):
        """
        Тест смены мейла на невалидный (без @)
        """
        with allure.step('Send PUT request witch invalid email'):
            response = MyRequests.put(f'/user/{create_login_delete_user.json()["user_id"]}',
                data={'email': 'ololo.nail.ru'},
                headers={'x-csrf-token':create_login_delete_user.headers['x-csrf-token']},
                cookies={'auth_sid':dict(create_login_delete_user.cookies)['auth_sid']})
        with allure.step('check response'):
            Assertions.assert_response_text(response, 'Invalid email format',
                                            'Неверный текст ответа')

    @allure.description('Текст смену очень короткого имени')
    def test_change_firstname_invalid(self, create_login_delete_user):
        """
        Текст смену очень короткого имени
        """
        with allure.step('Send PUT request witch invalid firstName'):
            response = MyRequests.put(f'/user/{create_login_delete_user.json()["user_id"]}',
                                      data={'firstName': 'o'},
                                      headers={'x-csrf-token': create_login_delete_user.headers['x-csrf-token']},
                                      cookies={'auth_sid': dict(create_login_delete_user.cookies)['auth_sid']})
        with allure.step('check response'):
            Assertions.assert_type_obj(response.json(), dict)
            Assertions.assert_json_value_by_name(response,'error','Too short value for field firstName',
                                                 f'Неверное значение {response.json()}'
                                                 f'{response.json()["error"]}')
