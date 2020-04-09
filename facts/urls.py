from django.urls import include, path
from facts.views import (
    LetterArtistListView,
    HomeTemplateView,
    LetterSongListView,
    ArtistSongsListView,
    SongsFactListView,
    SearchView,

)

app_name = 'facts'
urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('letter-artists-list/<str:letter>/', LetterArtistListView.as_view(), name='letter-artists-list'),
    path('letter-songs-list/<str:letter>/', LetterSongListView.as_view(), name='letter-songs-list'),
    path('artists-songs-list/<str:name>/', ArtistSongsListView.as_view(), name='artists-songs-list'),
    path('song-facts-list/<int:pk>/', SongsFactListView.as_view(), name='song-facts-list'),
    path('search-result/', SearchView.as_view(), name='search-result'),
]


