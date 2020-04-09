from django.db import models
from django.db.models import Q
from django.urls import reverse

from .utils import song_unique_slug_generator, artist_unique_slug_generator

from django.db.models.signals import pre_save, post_save


class ArtistManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            lookup = name__icontains=query
            qs = qs.filter(lookup)
        return qs


class Artist(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    objects = ArtistManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/artists-songs-list/{name}/".format(name=self.name)


def artist_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = artist_unique_slug_generator(instance)


pre_save.connect(artist_pre_save_receiver, sender=Artist)


class SongManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            lookup = name__icontains=query
            qs = qs.filter(lookup)
        return qs


class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist')
    slug = models.SlugField(blank=True, unique=True)
    objects = SongManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("facts:artists-songs-list", kwargs={"pk": self.pk})


def song_pre_save_receiver(sender, instance, *args, **kwargs):
     if not instance.slug:
         instance.slug = song_unique_slug_generator(instance)


pre_save.connect(song_pre_save_receiver, sender=Song)


class FactManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(message__icontains=query) |
                         Q(author__icontains=query))
            qs = qs.filter(or_lookup).distinct()
        return qs


class Fact(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    message = models.TextField()
    author = models.CharField(max_length=200, blank=True, null=True)
    objects = FactManager()

    def __str__(self):
        return f"{self.message}: {self.song.artist.name}"

    def get_song_name(self):
        return self.song.name

    def get_absolute_url(self):
        return "/song-facts-list/{pk}/".format(pk=self.pk)



# pre_save.connect(pre_save_recevier, sender=Song)

# To do: fix the slug!




