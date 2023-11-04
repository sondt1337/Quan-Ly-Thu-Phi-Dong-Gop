from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields you want here
    # Example: profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    pass
