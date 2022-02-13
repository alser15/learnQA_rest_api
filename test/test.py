from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserPut:


    def test_(self, create_login_delete_user):
        response = MyRequests.put(f'/user/2',
            data={'username': 'Vanay'},
            headers={'x-csrf-token':create_login_delete_user.headers['x-csrf-token']},
            cookies={'auth_sid':dict(create_login_delete_user.cookies)['auth_sid']})

        print(response.text)
        response = MyRequests.get(f'/user/2',
                                  headers={'x-csrf-token': create_login_delete_user.headers['x-csrf-token']},
                                  cookies={'auth_sid': dict(create_login_delete_user.cookies)['auth_sid']})
        print(response.text)