import tkinter as tk
import pypokedex
import PIL.Image, PIL.ImageTk
import json
import requests
from io import BytesIO


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
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
   
    response = http.get(pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.content))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())

label_id_name = tk.Label(combat, text="ID or Name")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(combat, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(combat, text="Load Pokemon", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

combat.mainloop()
import random

class Pokemon():
    def __init__(self, nom, vie, puissance_attaque, defense, types):
        self.nom = nom
        self.vie = vie
        self.niveau = 0
        self.puissance_attaque = puissance_attaque
        self.defense = defense
        self.types = types

    def attaquer(self, cible):
        # Calculer les dégâts infligés à la cible
        # en fonction de la puissance d'attaque
        # et de la défense de l'attaquant et de la cible
        degats = int(self.puissance_attaque * (1 + random.uniform(-0.2, 0.2)) - cible.defense)
        if degats < 1:
            degats = 1

        # Réduire la vie de la cible en fonction des dégâts infligés
        cible.vie -= degats
        print(f"{self.nom} inflige {degats} dégâts à {cible.nom}")

        # Vérifier si la cible est KO
        if cible.vie <= 0:
            cible.vie = 0
            print(f"{cible.nom} est KO")

    def soigner(self, points_de_vie):
        # Ajouter des points de vie au Pokemon
        self.vie += points_de_vie
        print(f"{self.nom} récupère {points_de_vie} points de vie")

# Create two Pokemon
pikachu = Pokemon("Pikachu", 100, 50, 20, ["Electric"])
bulbasaur = Pokemon("Bulbasaur", 120, 40, 30, ["Grass", "Poison"])
def start_game():
    # Create two Pokemon
    pikachu = Pokemon("Pikachu", 100, 50, 20, ["Electric"])
    bulbasaur = Pokemon("Bulbasaur", 120, 40, 30, ["Grass", "Poison"])

    # Make them attack each other until one faints
    while pikachu.vie > 0 and bulbasaur.vie > 0:
        pikachu.attaquer(bulbasaur)
        if bulbasaur.vie <= 0:
            print(f"{bulbasaur.nom} a été vaincu !")
            break
        bulbasaur.attaquer(pikachu)
        if pikachu.vie <= 0:
            print(f"{pikachu.nom} a été vaincu !")
            break

    print("Combat terminé !")

btn_play = tk.Button(combat, text="Play", command=start_game)

# Make them attack each other until one faints
def battle(pokemon1, pokemon2):
    # Print the names of the two Pokemons
    print(f"{pokemon1.nom} vs {pokemon2.nom}!")

    # Start the battle until one Pokemon faints
    while pokemon1.vie > 0 and pokemon2.vie > 0:
        # Pokemon 1 attacks Pokemon 2
        pokemon1.attaquer(pokemon2)
        if pokemon2.vie <= 0:
            print(f"{pokemon2.nom} a été vaincu !")
            break

        # Pokemon 2 attacks Pokemon 1
        pokemon2.attaquer(pokemon1)
        if pokemon1.vie <= 0:
            print(f"{pokemon1.nom} a été vaincu !")
            break

    print("Combat terminé !")


print("Combat terminé !")
btn_load = tk.Button(combat, text="Play", command=Pokemon)
