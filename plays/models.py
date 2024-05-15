from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Performance(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.IntegerField()
    description = models.TextField()
    poster = models.FileField(upload_to='posters/')

    def __str__(self):
        return self.title


class Opera(Performance):
    composer = models.CharField(max_length=100)
    librettist = models.CharField(max_length=100)

    def __str__(self):
        return self.title
