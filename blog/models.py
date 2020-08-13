from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    para = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='blog-img',verbose_name='img')
    url = models.URLField(blank=True)
    

    def __str__(self):
        return self.title
    

