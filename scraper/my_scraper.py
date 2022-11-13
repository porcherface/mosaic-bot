# my_scraper.py

import os, requests, lxml, re, json, urllib.request
from bs4 import BeautifulSoup
from serpapi import GoogleSearch
from PIL import Image
import requests
from io import BytesIO

hero_list = [
"Abaddon",
"Alchemist",
"Ancient Apparition",
"Anti Mage",
"Arc Warden",
"Axe",
"Bane",
"Batrider",
"Beastmaster",
"Bloodseeker",
"Bounty Hunter",
"Brewmaster",
"Bristleback",
"Broodmother",
"Centaur Warrunner",
"Chaos Knight",
"Chen",
"Clinkz",
"Clockwerk",
"Crystal Maiden",
"Dark Seer",
"Dazzle",
"Death Prophet",
"Disruptor",
"Doom",
"Dragon Knight",
"Drow Ranger",
"Earth Spirit",
"Earthshaker",
"Elder Titan",
"Ember Spirit",
"Enchantress",
"Enigma",
"Faceless Void",
"Gyrocopter",
"Huskar",
"Invoker",
"Io",
"Jakiro",
"Juggernaut",
"Keeper of the Light",
"Kunkka",
"Legion Commander",
"Leshrac",
"Lich",
"Lifestealer",
"Lina",
"Lion",
"Lone Druid",
"Luna",
"Lycan",
"Magnus",
"Medusa",
"Meepo",
"Mirana",
"Monkey King",
"Morphling",
"Naga Siren",
"Nature Prophet",
"Necrophos",
"Night Stalker",
"Nyx Assassin",
"Ogre Magi",
"Omniknight",
"Oracle",
"Outworld Devourer",
"Phantom Assassin",
"Phantom Lancer",
"Phoenix",
"Puck",
"Pudge",
"Pugna",
"Queen of Pain",
"Razor",
"Riki",
"Rubick",
"Sand King",
"Shadow Demon",
"Shadow Fiend",
"Shadow Shaman",
"Silencer",
"Skywrath Mage",
"Slardar",
"Slark",
"Sniper",
"Spectre",
"Spirit Breaker",
"Storm Spirit",
"Sven",
"Techies",
"Templar Assassin",
"Terrorblade",
"Tidehunter",
"Timbersaw",
"Tinker",
"Tiny",
"Treant Protector",
"Troll Warlord",
"Tusk",
"Underlord",
"Undying",
"Ursa",
"Vengeful Spirit",
"Venomancer",
"Viper",
"Visage",
"Warlock",
"Weaver",
"Windranger",
"Winter Wyvern",
"Witch Doctor",
"Wraith King",
"Zeus",
## i copypasted heroes from a txt, the following were missing from the list
"Marci",
"Mars",
"Grimstroke",
"Hoodwink",
"Primal Beast",
"Void Spirit",
"Snapfire",
"Dawnbreaker",
"Dark Willow",
"Pangolier",
]

hero_list_patchypatch = [
"Void Spirit",
"Snapfire",
"Dawnbreaker",
"Dark Willow",
"Pangolier",
]

headers = {
    "User-Agent": "Chrome/103.0.5060.1142"# Safari/537.36"
}

params = {
    "q": "templar assassin dota", # search query
    "tbm": "isch",                # image results
    "hl": "en",                   # language of the search
    "gl": "us",                   # country where search comes from
    "ijn": "0"                    # page number
}


def get_images_with_request_headers():
    del params["ijn"]
    params["content-type"] = "image/png" # parameter that indicate the original media type

    return [img["src"] for img in soup.select("img")]

def download_from_url(hero, urlist, ijn):

	counter = 0
	for u in urlist:
		response = requests.get(u)
		img = Image.open(BytesIO(response.content))
		img.save("downloads/"+hero+"_"+str(u).split(":")[2][6:16]+"_"+ijn+".png")
		counter += 1
	print("saved "+str(counter)+" images")

if __name__ == "__main__":

	print("heroes: "+str(len(hero_list)))
	print("images per page: 21")
	print("pages: 3")
	print("total number of pics: "+str(len(hero_list)*21*3))

	for ijn in ["0","1","2"]:
		for hero in hero_list_patchypatch:
			print("downloading "+ hero + ", page"+ijn)
			params["q"] = hero + " dota2"
			params["ijn"] =ijn
			html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
			soup = BeautifulSoup(html.text, "lxml")
			download_from_url(hero, get_images_with_request_headers(),ijn)


