from django.db import models
from user.models import User

from django.core.validators import MinValueValidator, MaxValueValidator


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 32)
    art_name = models.CharField(max_length = 32)
    validity = models.BooleanField(default = False)

    location = models.IntegerField(validators    = [MinValueValidator(0),
                                                        MaxValueValidator(32)],
                                                        default = 0) 

    soozan_score = models.IntegerField(validators = [MinValueValidator(1),
                                                        MaxValueValidator(5)],
                                                        default = 1)  # MORE INFO docs.md