from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    subscription = models.BooleanField(blank=False, default=False)
    
    def __str__(self):
        return self.user
