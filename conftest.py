import pytest
import requests
from faker import Faker
import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


@pytest.fixture
def setup():
    with allure.step('Формирование данных'):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
    response1 = requests.post('https://playground.learnqa.ru/api/user/login',
                              data=data)
    auth_sid = BaseCase.get_cookies(response1, 'auth_sid')
    token = BaseCase.get_headers(response1, 'x-csrf-token')
    user_id_from_auth_method = BaseCase.get_json_value(response1, 'user_id')

    return (auth_sid, token, user_id_from_auth_method)


@pytest.fixture
def data():
    with allure.step('Формирование данных'):
        return   {
            'username': f"{Faker().simple_profile()['username']}",
            'firstName': f"{Faker().simple_profile()['name'].split()[0]}",
            'lastName': f"{Faker().simple_profile()['name'].split()[1]}",
            'email': f'{Faker().email()}',
            'password': f'{Faker().password(length=6)}'
        }

@pytest.fixture
def create_login_delete_user(data):
    with allure.step('create user'):
        MyRequests.post('/user/', data=data)

    with allure.step('auth user'):
        response = MyRequests.post('/user/login',
                                   data={'email':data['email'],
                                         "password":data['password']})
    yield response

    with allure.step('delete user'):
        MyRequests.delete(f'/user/{response.json()["user_id"]}',
                                headers={'x-csrf-token':response.headers['x-csrf-token']},
                                cookies={'auth_sid':response.cookies['auth_sid']})

    with allure.step('check delete user'):
        answer = MyRequests.get(f'/user/{response.json()["user_id"]}')


        Assertions.assert_status_code(answer, 404)
        Assertions.assert_response_text(answer, 'User not found', f'Неверный текст ответа'
                                                                    f'{answer.text}')
