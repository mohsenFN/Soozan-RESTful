from django.db import models
from User.models import User

from django.core.validators import MinValueValidator, MaxValueValidator


class DerivedArtist(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 32)
    art_name = models.CharField(max_length = 32)
    location = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(32)]) # BASED ON docs.md
    posts = None # probably should delete
    requests = None # probably should delete


