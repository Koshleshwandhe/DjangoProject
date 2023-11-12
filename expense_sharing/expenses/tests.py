# expenses/tests.py

from django.test import TestCase
from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name='Test User', email='test@example.com', mobile_number='9372924160')

    def test_user_creation(self):
        user = User.objects.get(name='Test User')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.mobile_number, '9372924160')
