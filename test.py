import tkinter as tk
import pypokedex
import PIL.Image, PIL.ImageTk
import json
import requests
from io import BytesIO
import random


class Pokemon():
    def __init__(self, name, dex, types, sprite):
        self.name = name
        self.dex = dex
        self.types = types
        self.sprite = sprite
        self.hp = random.randint(50, 100)
        self.attack = random.randint(10, 30)
        self.defense = random.randint(10, 30)

    def attack_pokemon(self, other_pokemon):
        damage = (self.attack - other_pokemon.defense) + random.randint(-5, 5)
        other_pokemon.hp = max(0, other_pokemon.hp - damage)
        print(f"{self.name} attacked {other_pokemon.name} for {damage} damage!")

class Pokedex():
    def __init__(self):
        self.pokemon_data = {}
        self.pokemons = []

        # Load Pokemon data from file
        try:
            with open("pokemon_data.json", "r") as f:
                self.pokemon_data = json.load(f)
        except:
            print("Could not load Pokemon data.")

    def get_pokemon(self, name_or_id):
        # Check if we already have the Pokemon in memory
        if name_or_id in self.pokemon_data:
            data = self.pokemon_data[name_or_id]
        else:
            # Download the Pokemon data
            try:
                pokemon = pypokedex.get(name=name_or_id)
                data = {
                    "name": pokemon.name,
                    "dex": pokemon.dex,
                    "types": pokemon.types,
                    "sprite": pokemon.sprites.front.get("default")
                }
                self.pokemon_data[name_or_id] = data
            except:
                print(f"Could not find Pokemon {name_or_id}.")
                return None

        # Create a new Pokemon object from the data
        return Pokemon(data["name"], data["dex"], data["types"], data["sprite"])

    def save_pokemon_data(self):
        with open("pokemon_data.json", "w") as f:
            json.dump(self.pokemon_data, f)

class PokemonGame():
    def __init__(self):
        self.pokedex = Pokedex()

        # Create the main window
        self.window = tk.Tk()
        self.window.geometry("600x500")
        self.window.title("Pokemon Game")

        # Create the title label
        self.title_label = tk.Label(self.window, text="Pokemon Game")
        self.title_label.config(font=("Arial", 32))
        self.title_label.pack(padx=10, pady=10)

        # Create the Pokemon image label
        self.pokemon_image = tk.Label(self.window)
        self.pokemon_image.pack()

        # Create the Pokemon information label
        self.pokemon_information = tk.Label(self.window)
        self.pokemon_information.config(font=("Arial", 20))
        self.pokemon_information.pack(padx=10, pady=10)

        # Create the Pokemon types label
        self.pokemon_types = tk.Label(self.window)
        self.pokemon_types.config(font=("Arial", 20))
        self.pokemon_types.pack(ppadx=10, pady=10)

pokedex = Pokedex()
combat = tk.Tk()
combat.geometry("600x500")
combat.title("Pokedex")
combat.config(padx=10, pady=10)

title_label = tk.Label(combat, text="Pokedex")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(combat)
pokemon_image.pack()

pokemon_information = tk.Label(combat)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(combat)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

http = requests.Session()



def load_pokemon():
    name = text_id_name.get(1.0, "end-1c")
    pokemon = pokedex.get_pokemon(name)
    if pokemon:
        response = http.get(pokemon.sprite)
        image = PIL.Image.open(BytesIO(response.content))
        img = PIL.ImageTk.PhotoImage(image)
        pokemon_image.config(image=img)
        pokemon_image.image = img
        pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
        pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())
    else:
        # Display an error message if the Pokemon is not found
        pokemon_information.config(text=f"Could not find Pokemon {name}.")
        pokemon_types.config(text="")
        pokemon_image.config(image="")

    pokemon_information.config(text=f"{pokemon.nom} - HP: {pokemon.vie} - Attack: {pokemon.puissance_attaque} - Defense: {pokemon.defense}")
    pokemon_types.config(text=" - ".join(pokemon.types).title())
btn_load = tk.Button(combat, text="Play", command=PokemonGame)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)
combat.mainloop()