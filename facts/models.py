from django.db import models
from django.db.models import Q
# from .utils import unique_slug_generator
# from django.db.models.signals import pre_save


class ArtistManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            lookup = name__icontains=query
            qs = qs.filter(lookup)
        return qs


class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(blank=True, unique=True)
    objects = ArtistManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/artists-songs-list/{name}/".format(name=self.name)


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
    # slug = models.SlugField(blank=True, unique=True)
    objects = SongManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/artists-songs-list/{pk}/".format(pk=self.pk)


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


# def pre_save_recevier(sender,instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#
# pre_save.connect(pre_save_recevier, sender=Artist)
# pre_save.connect(pre_save_recevier, sender=Song)

# To do: fix the slug!
