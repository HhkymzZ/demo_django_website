from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img/%y')
    content = models.TextField()

    def __str__(self):
        return self.content
        return self.title

