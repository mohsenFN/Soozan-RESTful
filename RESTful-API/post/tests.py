from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient

class PostTagsViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('get-tags')

    def test_get_tags(self):
        resp = self.client.get(self.url, {'x' : 'z'})
        self.assertGreater(len(resp.json()), 0)


class NewPostViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('post-new')

    def test_unauth_request(self):
        resp = self.client.post(self.url, {})
        self.assertEqual(401, resp.status_code)