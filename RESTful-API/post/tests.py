from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from utils.tests import register_and_get_token, test_image, upload_test_post

class PostTagsViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('get-tags')

    def test_get_tags(self):
        resp = self.client.get(self.url, {})
        self.assertGreater(len(resp.json()), 0)


class NewPostViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-register')
        self.login_url = reverse('get-token')
        self.url = reverse('post-new')

    def test_unauth_request(self):
        resp = self.client.post(self.url, {})
        self.assertEqual(401, resp.status_code)
     
    def test_authed_empty_request(self):
        token = register_and_get_token(self.client, self.register_url, self.login_url)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        resp = self.client.post(self.url, {})
        self.assertEqual(400, resp.status_code)
    
    def test_correct_request(self):
        token = register_and_get_token(self.client, self.register_url, self.login_url)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        resp = upload_test_post(self.client, self.url)
        self.assertEqual(201, resp.status_code)


class UpdatePostViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-register')
        self.login_url = reverse('get-token')
        self.new_post_url = reverse('post-new')
        self.url = reverse('post-update', args=[1])

    
    def test_valid_update(self):
        token = register_and_get_token(self.client, self.register_url, self.login_url)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        upload_test_post(self.client, self.new_post_url)
        resp = self.client.patch(self.url, {'caption' : 'Updated caption'})
        self.assertEqual(200, resp.status_code)

    def test_valid_update(self):
        token = register_and_get_token(self.client, self.register_url, self.login_url)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        image = test_image()
        # Upload a post :
        self.client.post(self.new_post_url, {'caption' : 'test', 'tags' : 2, 'image' : image})
        resp = self.client.patch(self.url, {'invalid_arg' : 0})
        self.assertEqual(400, resp.status_code)
