from asyncore import read
import soup as soup
from bs4 import BeautifulSoup
import requests
from facts.models import Artist, Song, Fact
from mymima import settings
html = 'https://www.mima.co.il/fact_page.php?song_id=969'
html_content=requests.get(html).text
soup = BeautifulSoup(html_content, "html.parser")
infoSongArt = soup.find_all('font', {'size': ['+5', '+2']})
#artist_name = infoSongArt[0]
artist_name = Artist(name=infoSongArt[0])
artist_name.save()
#song_name = infoSongArt[1]
song_name = Song(name=infoSongArt[1], Artist=infoSongArt[0])
song_name.save()
print(Artist.objects.all())
print(Song.objects.all())
infoFactAut = [element.text for element in soup.find_all('tr', {'bgcolor': ['#CCFFCC', '#EDF3FE']})]
factim = []
print(infoFactAut)
for f in infoFactAut:
    temp = f.strip().replace('\r\n', '').split('נכתב ע"י')
    factim.append(temp)
print(factim)
#print(type(text))
print(soup.prettify())

