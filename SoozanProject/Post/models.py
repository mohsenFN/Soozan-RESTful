from django.db import models
from User.models import User

class Post(models.Model):
    artist = models.ForeignKey(User, on_delete = models.CASCADE)
    caption =models.CharField(max_length = 512)
    tags = None # Figure out smt later
    pub_date = models.DateTimeField()
    



