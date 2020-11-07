import requests
from bs4 import BeautifulSoup
import urllib

opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'whatever')
save_icon = opener.retrieve

url = "https://pokemondb.net/sprites"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

pokemon = soup.find_all(class_="infocard")




for i in pokemon:
    img = i.find(class_="icon-pkmn")
    href = img.attrs["data-src"]
    name = i.text.strip().lower()
    print(href)
    print(name)
    save_icon(href, f"../images/{name}.png")
