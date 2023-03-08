from django.test import TestCase
from usermap.models import CustomUser


"""
Primary tests are included in this file
"""

class UsersManagersTests(TestCase):
    """
    Tests for the user creation system
    """

    def test_create_user(self):
        """
        Tests the creaton of a regular user
        :return:
        """

        user = CustomUser.objects.create_user(
            username="user",
            email="normal@user.com",
            password="foo"
        )
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNotNone(user)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            CustomUser.objects.create_user()
        with self.assertRaises(TypeError):
            CustomUser.objects.create_user(username="")
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(username="", password="foo")

    def test_create_superuser(self):
        """
        Tests the creation of an admin user
        :return:
        """

        admin_user = CustomUser.objects.create_superuser(
            username="superfoo",
            email="super@user.com",
            password="foo"
        )
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNotNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                username="super@user.com", password="foo", is_superuser=False)
