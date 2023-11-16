from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from users.models import User
from django.urls import resolve
from users.views import UserCreationApiView


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='test_username',
            email='test@example.com',
            password='password123'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            username='test_username',
            email='admin@example.com',
            password='adminpassword'
        )
        self.assertEqual(superuser.email, 'admin@example.com')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)


class UserViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'email': 'test@example.com',
            'password': 'password123'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.superuser_data = {
            'email': 'admin@example.com',
            'password': 'adminpassword'
        }
        self.superuser = User.objects.create_superuser(**self.superuser_data)


class UserUrlsTest(TestCase):
    def test_user_create_url_resolves(self):
        url = reverse('users:user_create')
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.__name__, UserCreationApiView.as_view().__name__)
        self.assertTrue(callable(UserCreationApiView.as_view()))
