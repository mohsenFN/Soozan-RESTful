from django.db import models
from User.models import User

class Tag(models.Model):
    name_en = models.CharField(max_length=50, unique=True)
    name_fa = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name_en}/{self.name_fa}"


class Post(models.Model):
    artist = models.ForeignKey(User, on_delete = models.CASCADE, related_name='posts')
    caption =models.CharField(max_length = 512, blank = False)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='post_images/', null = False, blank = False)
    pub_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.artist.number}'s Post - {self.caption[:20]}..."



