from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AccountsTests(TestCase):

    def test_signup_creates_user(self):
        # RED: Test will fail if signup not implemented
        response = self.client.post(reverse('signup'), {
            'username': 'michelle',
            'email': 'michelle@example.com',
            'password': 'password123'
        })
        # Test that user now exists
        self.assertTrue(User.objects.filter(username='michelle').exists())
        # Test that it redirects to login page
        self.assertEqual(response.status_code, 302)
