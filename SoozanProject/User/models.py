from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
from django.core.validators import MinLengthValidator


class User(AbstractBaseUser, PermissionsMixin):

    number = models.CharField(max_length = 11, unique = True)
    password = models.CharField(max_length=88)
    is_artist = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # try removing some of useless fields

    objects = UserManager()
    
    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.number