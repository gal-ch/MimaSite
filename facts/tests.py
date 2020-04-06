from django.test import TestCase
from .models import Artist, Song, Fact


class ArtistModelTests(TestCase):
    def test_models(self):
        artist1 = Artist(name="gal")
        artist1.save()
        artist2 = Artist(name="adi")
        artist2.save()
        artist3 = Artist(name="Beyonce")
        artist3.save()
        self.assertEqual(len(Artist.objects.all()) == 3, True)


class SongModelTests(TestCase):
    def test_models(self):
        artist1 = Artist(name="gal")
        artist1.save()
        song1 = Song(name="impossible", artist=artist1)
        song1.save()
        artist2 = Artist(name="adi")
        artist2.save()
        song2 = Song(name="dadada", artist=artist2)
        song2.save()
        artist3 = Artist(name="Beyonce")
        artist3.save()
        song3 = Song(name="love on top", artist=artist3)
        song3.save()
        self.assertEqual(len(Song.objects.all()) == 3, True)


class FactsModelTests(TestCase):
    def test_models(self):
        artist1 = Artist(name="gal")
        artist1.save()
        song1 = Song(name="impossible", artist=artist1)
        song1.save()
        fact1 = Fact(song=song1, message="Dani's Facts")
        fact1.save()
        artist2 = Artist(name="adi")
        artist2.save()
        song2 = Song(name="dadada", artist=artist2)
        song2.save()
        fact2 = Fact(song=song2, message="Dana's Facts")
        fact2.save()
        artist3 = Artist(name="Beyonce")
        artist3.save()
        song3 = Song(name="love on top", artist=artist3)
        song3.save()
        fact3 = Fact(song=song3, message="Gal's Facts")
        fact3.save()
        self.assertEqual(len(Song.objects.all()) == 3, True)