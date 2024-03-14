from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model

from .models import CustomUser


class TestUserModel(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.user = get_user_model().objects.create_user(
            username='testuser',
            password='password',
            email='test@gmail.com',
            name='test1'
        )

    def test_user_model(self):

        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@gmail.com')
        self.assertEqual(self.user.name, 'test1')
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_user_model_permissions(self):

        self.assertEqual(self.user.is_staff, False)
        self.assertEqual(self.user.is_superuser, False)
