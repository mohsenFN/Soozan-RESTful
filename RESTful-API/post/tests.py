from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient


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
        token = self.register_and_get_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        resp = self.client.post(self.url, {})
        self.assertEqual(400, resp.status_code)
    
    def test_correct_request(self):
        token = self.register_and_get_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        with open('../11228.jpg', 'rb') as f:
            bimage = f.read()
        
        image = SimpleUploadedFile("test_image.jpg", bimage, content_type="image/jpeg")

        resp = self.client.post(self.url, {'caption' : 'test', 'tags' : 1, 'image' : image})
        self.assertEqual(201, resp.status_code)