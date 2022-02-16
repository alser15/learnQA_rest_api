from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure


@allure.epic('Case delete user')
class TestDeleteUser:

    @allure.description('Тест на удаление юзера (администратора)')
    def test_delete_user_two(self):
        """
        Тест на удаление юзера (администратора)
        """
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        with allure.step('auth user'):
            response = MyRequests.post('/user/login',
                                       data={'email': data['email'],
                                             "password": data['password']})
        with allure.step('delete user'):
            response2 = MyRequests.delete(
                f'/user/2',
                headers={'x-csrf-token': response.headers['x-csrf-token']},
                cookies={'auth_sid': response.cookies['auth_sid']})
        with allure.step('validate answer'):
            Assertions.assert_response_text(
                response2,
                'Please, do not delete test users with ID 1, 2, 3, 4 or 5.',
                f'Неверный текст ответа {response2.text}')

    @allure.description('Тест на удаление созданного юзера')
    def test_delete_created_user(self,data):
        """
        Тест на удаление созданного юзера
        """
        with allure.step('Регистрация юзера'):
            MyRequests.post('/user/', data=data)

        with allure.step('Авторизация юзера'):
            response = MyRequests.post('/user/login',
                                       data={'email': data['email'],
                                             "password": data['password']})
        with allure.step('del user'):
            MyRequests.delete(
                f'/user/{response.json()["user_id"]}',
                headers={'x-csrf-token': response.headers['x-csrf-token']},
                cookies={'auth_sid': response.cookies['auth_sid']})
        with allure.step('check deleted user'):

            answer = MyRequests.get(f'/user/{response.json()["user_id"]}')

            Assertions.assert_status_code(answer, 404)
            Assertions.assert_response_text(
                answer,
                'User not found',
                f'Неверный текст ответа {answer.text}')

    @allure.description('Тест на удаление юзера под токеном и куки другого юзера')
    def test_delete_user_with_another_auth(self, create_login_delete_user):
        """
        Тест на удаление юзера под токеном и куки другого юзера
        """
        with allure.step('Удаление юзера'):
            MyRequests.delete(
                f'/user/2',
                headers={'x-csrf-token': create_login_delete_user.headers['x-csrf-token']},
                cookies={'auth_sid': create_login_delete_user.cookies['auth_sid']})

        with allure.step('Проверка, что юзер не удален'):
            answer = MyRequests.get(f'/user/2')
            Assertions.assert_json_value_by_name(
                answer,'username','Vitaliy',
                f'Неверное значение {answer.json()["username"]}')
