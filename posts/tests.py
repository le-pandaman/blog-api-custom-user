from datetime import datetime

from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model


from rest_framework.test import APIClient

from .models import Posts

# Create your tests here.


class PostTestCase(APIClient):

    @classmethod
    def setUpTestData(cls):

        cls.user = get_user_model().objects.create(
            username='testuser',
            email='test@gmail.com',
            password='test',
        )

        cls.post = Posts.objects.create(title="test_title",
                                        body="test_body",
                                        created_at=datetime.now(),
                                        author='test_author'
                                        )

    def test_user_model(self):

        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.title, 'test_title')
        self.assertEqual(self.post.body, 'test_body')
        self.assertEqual(self.post.created_at, datetime.now())
        self.assertEqual(self.post.author, self.user.username)

    def test_list_api_view(self):

        response = self.client.get(reverse('post_list_api'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response.content, 'test_title')
