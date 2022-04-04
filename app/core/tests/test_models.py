from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating new user with email is successful"""
        email = 'dianajarenga@gmail.com'
        password = '1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password

        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """tests that new user email is normalised"""
        email = 'test@diana@gmail.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """tests creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_superuser(self):
        """Test Creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'jarengadiana@gmail.com',
            'diana1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_superuser)
