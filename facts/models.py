from django.db import models
from django.db.models import Q
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name




class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Fact(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    message = models.TextField()
    author = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.message}: {self.song.artist.name}"
