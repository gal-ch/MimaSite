from django.db import models
# from .utils import unique_slug_generator
# from django.db.models.signals import pre_save

class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/artists-songs-list/{name}/".format(name=self.name)


class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist')
    # slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/artists-songs-list/{pk}/".format(pk=self.pk)


class Fact(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    message = models.TextField()
    author = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.message}: {self.song.artist.name}"

    def get_song_name(self):
        return self.song.name


# def pre_save_recevier(sender,instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#
# pre_save.connect(pre_save_recevier, sender=Artist)
# pre_save.connect(pre_save_recevier, sender=Song)

# To do: fix the slug!
