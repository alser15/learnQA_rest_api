import pytest
from faker import Faker
from lib.my_requests import MyRequests

@pytest.fixture
def data():
    return   {
        'username': f"{Faker().simple_profile()['username']}",
        'firstName': f"{Faker().simple_profile()['name'].split()[0]}",
        'lastName': f"{Faker().simple_profile()['name'].split()[1]}",
        'email': f'{Faker().email()}',
        'password': f'{Faker().password(length=6)}'
    }

@pytest.fixture
def create_login_delete_user(data):
    #Регистрация юзера
    MyRequests.post('/user/', data=data)
    #Авторизация юзера
    response = MyRequests.post('/user/login', data={'email':data['email'],
                                                    "password":data['password']})
    yield response

    #Удаление юзера
    MyRequests.delete(f'/user/{response.json()["user_id"]}',
                            headers={'x-csrf-token':response.headers['x-csrf-token']},
                            cookies={'auth_sid':response.cookies['auth_sid']})