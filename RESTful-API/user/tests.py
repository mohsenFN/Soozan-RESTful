from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from rest_framework.exceptions import ErrorDetail

from user.models import User
from artist.models import Artist

from utils.user_respones import RESPONSE_MESSAGES as MSG
from utils.tests import register_and_get_token

class UserRegisterViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('user-register')

    def test_empty_request(self):
        resp = self.client.post(self.url, {})
        self.assertEqual(resp.data['detail'], MSG['NO_PHONE_NUMBER'])

    def test_request_with_only_password(self):
        resp = self.client.post(self.url, {'password' : '11228'})
        self.assertEqual(resp.data['detail'], MSG['NO_PHONE_NUMBER'])

    def test_request_with_only_phonenumber(self):
        resp = self.client.post(self.url, {'number' : '09148387871'})
        self.assertIsInstance(resp.data['errors']['password'][0], ErrorDetail)

    def test_request_with_short_password(self):
        resp = self.client.post(self.url, {'number':'09148387871', 'password' : '11228'})
        self.assertIn('This password is too short.', resp.data['detail'][0])

    def test_request_with_numeric_password(self):
        resp = self.client.post(self.url, {'number' : '09148387871', 'password' : '54586566'})
        self.assertEqual('This password is entirely numeric.', resp.data['detail'][0])


    def test_proper_artist_request(self):
        resp = self.client.post(self.url, {'number' : '09148387871', 'password' : 'VeryG00dPassword', 'is_artist' : True})
        self.assertEqual(200, resp.status_code)


    def test_duplicate_number(self):
        resp = self.client.post(self.url, {'number' : '09148387871', 'password' : 'VeryG00dPassword', 'is_artist' : True})
        resp = self.client.post(self.url, {'number' : '09148387871', 'password' : 'VeryG00dPassword', 'is_artist' : True})
        self.assertEqual(409, resp.status_code)


    def test_artist_derived_model_creation(self):
        resp = self.client.post(self.url, {'number' : '09148387871', 'password' : 'VeryG00dPassword', 'is_artist' : True})
        user = User.objects.get(id = resp.data['user_id'])
        derived_model = Artist.objects.get(user=user)
        
        self.assertIsNotNone(derived_model)


class UserLoginViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('get-token')
        self.register_url = reverse('user-register')
    
    def test_login_with_invalid_creds(self):
        resp = self.client.post(self.url, {})
        self.assertEqual(401, resp.status_code)

    def test_login_with_valid_creds(self):
        self.client.post(self.register_url, {'number' : '09148387871', 'password' : 'VeryG00dPassword', 'is_artist' : True})
        resp = self.client.post(self.url, {'number' : '09148387871', 'password' : 'VeryG00dPassword'})
        self.assertIn('access_token', resp.data)

# AKA refresh-token
class RefreshTokenViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('refresh-token')
        self.register_url = reverse('user-register')
        self.get_token_url = reverse('get-token')

    def test_empty_request(self):
        resp = self.client.post(self.url, {})
        self.assertEqual(MSG['REFRESH_TOKEN_REQ'], resp.json()['detail'])

    def test_invalid_refresh_token(self):
        resp = self.client.post(self.url, {'refresh_token' : 'KOSSSHER'})
        self.assertEqual(MSG['INVALID_REFRESH_TOKEN'], resp.json()['detail'])

    def test_valid_refresh_token(self):
        self.client.post(self.register_url, {'number' : '09148387871', 'password' : 'VeryG00dPassw0rd', 'is_artist' : True})

        resp = self.client.post(self.get_token_url, {'number' : '09148387871', 'password' : 'VeryG00dPassw0rd'})
        refresh_token = resp.json()['refresh_token']

        resp = self.client.post(self.url, {'refresh_token' : refresh_token})
        self.assertIn('access_token', resp.data)



class DeleteUserViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-register')
        self.login_url = reverse('get-token')
        self.url = reverse('user-delete')

    def test_correct_user_deletion(self):
        token = register_and_get_token(self.client, self.register_url, self.login_url)
        resp = self.client.delete(self.url, HTTP_AUTHORIZATION=f'Bearer {token}')

        self.assertEqual(204, resp.status_code)
    
    def test_invalid_user_deletion(self):
        invalid_access_token = 'Kossherrrrrr'
        resp = self.client.delete(self.url, HTTP_AUTHORIZATION=f'Bearer {invalid_access_token}')
        self.assertEqual(401, resp.status_code)


class UserLogOutViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-register')
        self.login_url = reverse('get-token')
        self.logout_url = reverse('user-logout')

    def test_user_logout(self):
        token = register_and_get_token(self.client, self.register_url, self.login_url)

        self.client.post(self.logout_url, HTTP_AUTHORIZATION=f'Bearer {token}')
        # trying to delete the same user with the same token we should get an 401 error
        resp = self.client.post(self.logout_url, HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(401, resp.status_code)