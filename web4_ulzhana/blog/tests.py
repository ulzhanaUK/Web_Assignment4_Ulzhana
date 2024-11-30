from rest_framework.test import APIClient
from django.test import TestCase
from .models import Post

class PostAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.post = Post.objects.create(title="Test Post", content="Test Content", author="Author")

    def test_list_posts(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        data = {"title": "New Post", "content": "Content", "author": "Author"}
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, 201)
