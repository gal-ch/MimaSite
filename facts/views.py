from django.views.generic import ListView, TemplateView, DetailView
from .models import Artist, Song, Fact
letters = [chr(x) for x in range(1488, 1515) if x != 1498 and x != 1503 and x != 1507 and x != 1509 and x != 1501]


class HomeTemplateView(TemplateView):
    template_name = "facts/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context["letters"] = letters
        return context


class LetterArtistListView(ListView):
    template_name = 'facts/artist.html'
    model = Artist

    def get_queryset(self):
        qs = super(LetterArtistListView, self).get_queryset().filter(name__startswith=self.kwargs['letter'])
        return qs


class LetterSongListView(ListView):
    template_name = 'facts/song.html'
    model = Song

    def get_queryset(self):
        qs = super(LetterSongListView, self).get_queryset().filter(name__startswith=self.kwargs['letter'])
        return qs
