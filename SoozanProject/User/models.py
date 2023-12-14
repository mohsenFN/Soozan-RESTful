from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .Manager import UserManager



class User(AbstractBaseUser):
    USER_TYPES =(('USER', 'User'), ('ARTIST', 'Artist'))

    number = models.CharField(max_length = 11, unique = True)
    user_type = models.CharField(max_length = 6, choices = USER_TYPES, default = 'USER')
    date_joined = models.DateTimeField()

    objects = UserManager()
    
    def __str__(self):
        return self.number