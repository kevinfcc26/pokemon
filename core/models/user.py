from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.managers.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead od username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
