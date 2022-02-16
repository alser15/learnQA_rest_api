import string
import random
import pytest
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from faker import Faker
import allure


@allure.epic('Case user register')
class TestUserRegister:
    @allure.description('Проверка возможности зарегистрировать пользователя с некорректным '
                        'почтой (без @)')
    def test_user_register_invalid_email(self, data):
        """
        Проверка возможности зарегистрировать пользователя с некорректным
        почтой (без @)
        """
        data['email'] = f'{Faker().email().replace("@", "")}'
        with allure.step(f'send POST request with invalid email {data["email"]}'):
            response = MyRequests.post('/user/', data=data)

        with allure.step('check response'):
            Assertions.assert_response_text(response, 'Invalid email format',
                                        f'Неверный текст {response.text}')

    @allure.description('Параметризированный тест на проверку возможности зарегистрировать '
                        'пользователя без одного из обязательного поля.)')
    @pytest.mark.parametrize('del_input', ['username',
                                           'firstName',
                                           'lastName',
                                           'email',
                                           'password'])
    def test_user_register_invalid_input(self, del_input, data):
        """
        Параметризированный тест на проверку возможности зарегистрировать
        пользователя без одного из обязательного поля.
        """
        with allure.step(f'Del input {del_input}'):
            data.pop(del_input)

        with allure.step('send POST request'):
            response = MyRequests.post('/user/', data=data)

        with allure.step('check response'):
            Assertions.assert_response_text(
                response, f'The following required params are missed: {del_input}',
                f'Неверный текст {response.text}')

    @allure.description('Проверка возможности зарегистрировать '
                        'пользователя с очень коротким именем')
    def test_user_register_with_short_name(self, data):
        """
        Проверка возможности зарегистрировать пользователя с очень коротким
        именем
        """
        data['firstName'] = random.choice(string.ascii_uppercase)

        with allure.step(f'send POST request with invalid firstName {data["firstName"]}'):
            response = MyRequests.post('/user/', data=data)

        with allure.step('check response'):
            Assertions.assert_response_text(
                response, f'The value of \'firstName\' field is too short',
                f'Неверный текст {response.text}')

    @allure.description('Проверка возможности зарегистрировать пользователя '
                        'с очень длинным именем')
    def test_user_register_with_long_name(self, data):
        """
        Проверка возможности зарегистрировать пользователя с очень длинным
        именем
        """
        data['firstName'] = \
            ''.join(random.choice(string.ascii_letters) for _ in range(252))
        with allure.step('send POST request with invalid firstName'):
            response = MyRequests.post('/user/', data=data)

        with allure.step('check response'):
            Assertions.assert_response_text(
                response, f'The value of \'firstName\' field is too long',
                f'Неверный текст {response.text}')

