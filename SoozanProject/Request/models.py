from django.db import models
from User.models import User

class Request(models.Model):
    STATUS_TYPES = (('PENDING', 'Pending'), ('DECLINED', 'Declined'), ('ACCEPTED', 'Accepted'))
        
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'fromuser')
    artist = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'touser') 
    caption = models.CharField(max_length = 512)
    status = models.CharField(max_length = 8, choices = STATUS_TYPES, default = 'PENDING')
    pub_date = models.DateTimeField()