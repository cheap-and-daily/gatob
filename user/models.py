from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    subscription = models.BooleanField(blank=False, default=False)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    phone_regex = RegexValidator(regex=r'^\+7-\d{3}-\d{3}-\d{2}-\d{2}$',
                                 message="Формат номера телефона должен быть +7-XXX-XXX-XX-XX")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.user.username
