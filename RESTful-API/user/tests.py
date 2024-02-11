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
        self.assertIn('No phone number is specified.', resp.data['detail'])

    def test_request_with_only_phonenumber(self):
        resp = self.client.post(self.url, {'number' : '09148387871'})
        self.assertIsInstance(resp.data['errors']['password'][0], ErrorDetail)