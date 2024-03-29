"""
Module containing the custom User model
Manager.
For more info, consult:
https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username
"""

from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    User model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """

        if not email:
            raise ValueError(_("Email is mandatory"))

        if not first_name:
            raise ValueError(_("First name is mandatory"))

        if not last_name:
            raise ValueError(_("Last name is mandatory"))

        if not password:
            raise ValueError(_("Password is mandatory"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, first_name, last_name, password, **extra_fields)
