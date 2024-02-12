from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from rest_framework.exceptions import ErrorDetail

from user.models import User
from artist.models import Artist

class UserRegisterViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('user-register')

    def test_empty_request(self):
        resp = self.client.post(self.url, {})
        self.assertEqual(resp.data['detail'], 'No phone number is specified.')

    def test_request_with_only_password(self):
        resp = self.client.post(self.url, {'password' : '11228'})
        self.assertEqual(resp.data['detail'], 'No phone number is specified.')

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