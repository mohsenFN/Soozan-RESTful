from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class UserRegisterViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('user-register')

    def empty_request(self):
        resp = self.client.post(self.url, {})
        self.assertIn('Invalid Data', resp.data['detail'])