import requests
from bs4 import BeautifulSoup
import urllib
import json

url = "https://pokemondb.net/pokedex/all"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

pokedex = soup.find({id: "pokedex"})
tbody = pokedex.findChild("tbody")
pokemon = tbody.findChildren("tr")

pokemon_list = []

with open(f"../pokemon/name_to_id.json", "w+") as file:
    file.write("{}")

name_table = {}

for i in pokemon:

    if i.select("td.cell-name > small") != []:
        continue

    pkmn_page = requests.get("https://pokemondb.net" + i.select(".ent-name")[0].attrs["href"])
    pkmn_soup = soup = BeautifulSoup(pkmn_page.content, 'html.parser')

    print("https://pokemondb.net" + i.select(".ent-name")[0].attrs["href"])

    id = int(pkmn_soup.select("div > div:nth-child(1) > div:nth-child(2) > table > tbody > tr:nth-child(1) > td > strong")[0].text)
    name = pkmn_soup.select("#main > h1")[0].text
    species = pkmn_soup.select("div > div:nth-child(1) > div:nth-child(2) > table > tbody > tr:nth-child(3) > td")[0].text
    type_div = pkmn_soup.select("div > div:nth-child(1) > div:nth-child(2) > table > tbody > tr:nth-child(2) > td")[0]
    types = [
    type.text.lower() for type in type_div.findChildren(class_="type-icon")
    ]
    height = pkmn_soup.select("div > div:nth-child(1) > div:nth-child(2) > table > tbody > tr:nth-child(4) > td")[0].text
    weight = pkmn_soup.select("div > div:nth-child(1) > div:nth-child(2) > table > tbody > tr:nth-child(5) > td")[0].text
    hp = int(pkmn_soup.select("div > div:nth-child(2) > div.grid-col.span-md-12.span-lg-8 > div.resp-scroll > table > tbody > tr:nth-child(1) > td:nth-child(2)")[0].text)
    attack = int(pkmn_soup.select("div > div:nth-child(2) > div.grid-col.span-md-12.span-lg-8 > div.resp-scroll > table > tbody > tr:nth-child(2) > td:nth-child(2)")[0].text)
    defense = int(pkmn_soup.select("div > div:nth-child(2) > div.grid-col.span-md-12.span-lg-8 > div.resp-scroll > table > tbody > tr:nth-child(3) > td:nth-child(2)")[0].text)
    special_attack = int(pkmn_soup.select("div > div:nth-child(2) > div.grid-col.span-md-12.span-lg-8 > div.resp-scroll > table > tbody > tr:nth-child(4) > td:nth-child(2)")[0].text)
    special_defense = int(pkmn_soup.select("div > div:nth-child(2) > div.grid-col.span-md-12.span-lg-8 > div.resp-scroll > table > tbody > tr:nth-child(5) > td:nth-child(2)")[0].text)
    speed = int(pkmn_soup.select("div > div:nth-child(2) > div.grid-col.span-md-12.span-lg-8 > div.resp-scroll > table > tbody > tr:nth-child(6) > td:nth-child(2)")[0].text)

    pkmn = {
        "id": id,
        "name": name,
        "types": types,
        "hp": hp,
        "attack": attack,
        "defense": defense,
        "special_attack": special_attack,
        "special_defense": special_defense,
        "speed": speed
    }

    name_table[name.lower()] = id

with open(f"../pokemon/name_to_id.json", "w+") as file:
    json.dump(name_table, file)
