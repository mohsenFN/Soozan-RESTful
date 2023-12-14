from django.db import models
from User.models import User
from Request.models import Request
from django.core.validators import MinValueValidator, MaxValueValidator

class DerivedArtist(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 32)
    location = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(32)]) # BASED ON docs.md
    requests = models.ForeignKey(Request, on_delete = models.CASCADE)
