from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from rest_framework.exceptions import ErrorDetail

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

