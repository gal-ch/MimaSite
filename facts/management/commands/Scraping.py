from asyncore import read
import soup as soup
from bs4 import BeautifulSoup
import requests
from facts.models import Artist, Song, Fact
from mymima import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        help = 'Closes the specified poll for voting'
        for num in range(1, 1451):
            html = 'https://www.mima.co.il/fact_page.php?song_id={}'.format(num)
            html_content = requests.get(html).text
            soup = BeautifulSoup(html_content, "html.parser")
            infoSongArt = soup.find_all('font', {'size': ['+5', '+2']})
            a = infoSongArt[1].text
            artist, boolA = Artist.objects.get_or_create(name=a)
            artist.save()
            song, boolS = Song.objects.get_or_create(name=infoSongArt[0].text, artist=artist)
            song.save()
            print(Artist.objects.all())
            print(Song.objects.all())
            facts = soup.find_all("tr", {'bgcolor': ['#CCFFCC', '#EDF3FE']})
            print(facts)
            for fact in facts:
                txt = fact.text
                splited_txt = txt.strip().split('נכתב ע"י')
                factData = splited_txt[0]
                try:
                    authorData = splited_txt[1]
                except IndexError:
                    authorData = 'אנונימי'
                fact, boolF = Fact.objects.get_or_create(message=factData, author=authorData, song=song)
                fact.save()












