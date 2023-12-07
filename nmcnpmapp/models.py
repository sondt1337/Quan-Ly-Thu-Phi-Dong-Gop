from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    is_approved = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    group = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    dongphi = models.BooleanField(default=False)
    donggop = models.PositiveSmallIntegerField(default=0)
    sukien = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username
    
from django.conf import settings

class FamilyMember(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    group = models.CharField(max_length=50, default='')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()


    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='article_images/')
    link = models.URLField()

    def __str__(self):
        return self.title