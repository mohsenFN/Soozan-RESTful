from django.db import models
from User.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 32)
    location = models.IntegerField(validators = [MinValueValidator(0),
                                                    MaxValueValidator(32)],
                                                    default = 0) # BASED ON docs.md

