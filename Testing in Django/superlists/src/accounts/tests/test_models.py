from django.test import TestCase
from accounts.models import User
from django.contrib import auth

class UserModelTest(TestCase):
    def test_model_is_configured_for_django_auth(self):
        self.assertEqual(auth.get_user_model(), User)

    def test_user_is_valid_with_email_only(self):
        user = User(email="a@b.com")
        user.full_clean()
    
    def test_email_is_primary_key(self):
        user = User(email="a@b.com")
        self.assertEqual(user.pk, "a@b.com")