from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set', blank=True, related_query_name='customuser')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set', blank=True, related_query_name='customuser')
