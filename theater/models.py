from django.db import models
from django.utils import timezone


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Play(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=' ')
    date = models.DateField(default=timezone.now)
    actors = models.ManyToManyField(Actor, related_name='plays')
    poster = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title
