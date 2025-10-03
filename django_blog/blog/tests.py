from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthTests(TestCase):
    def test_registration_and_login(self):
        resp = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'ComplexPass123',
            'password2': 'ComplexPass123'
        })
        self.assertEqual(resp.status_code, 302)  # redirect to profile
        user_exists = User.objects.filter(username='testuser').exists()
        self.assertTrue(user_exists)

        # Test login
        login = self.client.login(username='testuser', password='ComplexPass123')
        self.assertTrue(login)

