from django.urls import include, path
from facts.views import LetterArtistListView, HomeTemplateView, LetterSongListView

app_name = 'facts'
urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('letter-artists-list/<str:letter>/', LetterArtistListView.as_view(), name='letter-artists-list'),
    path('letter-songs-list/<str:letter>/', LetterSongListView.as_view(), name='letter-songs-list'),

]
