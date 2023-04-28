import tkinter as tk
import pypokedex
import PIL.Image, PIL.ImageTk
import urllib3
import json
import requests
from io import BytesIO
from PIL import Image, ImageTk

class Pokemon:
    def __init__(self, nom, type_pokemon, niveau=1, pv=100, attaque=0, defense=0):
        self.__nom = nom
        self.type = type_pokemon
        self.niveau = niveau
        self.pv = pv
        self.attaque = attaque
        self.defense = defense

    def afficher_infos(self):
        print(f"{self.__nom}, niveau {self.niveau}")
        print(f"Type: {self.type}")
        print(f"PV: {self.pv}")
        print(f"Attaque: {self.attaque}")
        print(f"Défense: {self.defense}")

pokemon = pypokedex.get(name="charmander")
#print(pokemon.dex)
#print(pokemon.name)
#print(pokemon.abilities)
#print(pokemon.type)
print(pokemon.sprites.front.get("default"))
pokemon

combat = tk.Tk()
combat.geometry("600x500")
combat.title("NeuralNine Pokedex Tutorial")
combat.config(padx=10, pady=10)

title_label = tk.Label(combat, text="NeuralNine Pokedex")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(combat)
pokemon_image.pack()

pokemon_abilities = [ability.name for ability in pokemon.abilities]
pokemon_information = tk.Label(combat, text=f"#{pokemon.dex} {pokemon.name}\nAbilities: {', '.join(pokemon_abilities)}")
pokemon_information.pack()

http = requests.Session()

def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    response = http.get(pokemon.sprites.front.get('default'))

    image = Image.open(BytesIO(response.content))
    sprite_image = ImageTk.PhotoImage(image)

    pokemon_image.config(image=sprite_image)
    pokemon_image.image = sprite_image

    label_id_name = tk.Label(combat, text="ID or Name")
    label_id_name.config(font=("Arial", 20))
    label_id_name.pack(padx=10, pady=10)

    text_id_name = tk.Text(combat, height=1)
    text_id_name.config(font=("Arial", 20))
    text_id_name.pack(padx=10, pady=10)

    btn_load = tk.Button(combat, text="Load Pokemon", command=load_pokemon)
    btn_load.config(font=("Arial", 20))
    btn_load.pack(padx=10, pady=10)

    # Initialize an empty list to store the Pokemon data
import json
pokedex = []

    # Load existing Pokemon data from the JSON file (if it exists)
try:
    with open('pokedex.json', 'r') as file:
        pokedex = json.load(file)
except FileNotFoundError:
    pass

# Define a function to add a new Pokemon to the pokedex
def add_pokemon(pokemon):
    # Check if the Pokemon already exists in the pokedex
    for existing_pokemon in pokedex:
        if existing_pokemon['name'] == pokemon['name']:
            # Pokemon already exists, do not add it again
            return
    
    # Pokemon does not exist in the pokedex, add it
    pokedex.append(pokemon)
    
    # Write the updated pokedex to the JSON file
    with open('pokedex.json', 'w') as file:
        json.dump(pokedex, file, indent=4)

