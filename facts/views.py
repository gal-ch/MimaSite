from django.views.generic import ListView, TemplateView, DetailView
from .models import Artist, Song, Fact
from itertools import chain
letters = [chr(x) for x in range(1488, 1515) if x != 1498 and x != 1503 and x != 1507 and x != 1509 and x != 1501]


class HomeTemplateView(TemplateView):
    template_name = "facts/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context["letters"] = letters
        return context


class LetterArtistListView(ListView):
    template_name = 'facts/artists.html'
    model = Artist

    def get_queryset(self):
        qs = super(LetterArtistListView, self).get_queryset().filter(name__startswith=self.kwargs['letter'])
        return qs


class LetterSongListView(ListView):
    template_name = 'facts/songs.html'
    model = Song

    def get_queryset(self):
        qs = super(LetterSongListView, self).get_queryset().filter(name__startswith=self.kwargs['letter'])
        return qs


class ArtistSongsListView(ListView):
    template_name = 'facts/songs.html'
    model = Song

    def get_queryset(self):
        qs = super(ArtistSongsListView, self).get_queryset().filter(artist__name=self.kwargs['name'])
        return qs


class SongsFactListView(ListView):
    template_name = 'facts/fact.html'
    model = Fact

    def get_queryset(self):
        qs = super(SongsFactListView, self).get_queryset().filter(song__id=self.kwargs['pk'])
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['song'] = Song.objects.get(id=self.kwargs['pk'])
        return context

