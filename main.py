import random
import os
import tkinter as tk
play = tk.Tk()
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
import json

class Pokedex():
    def __init__(self):
        self.pokemons = []

        # Charger les Pokemons depuis le fichier pokedex.json
        if os.path.exists("pokedex.json"):
            with open("pokedex.json", "r") as f:
                data = json.load(f)
            for pokemon_data in data:
                pokemon = Pokemon(pokemon_data["nom"], pokemon_data["vie"], pokemon_data["puissance_attaque"],
                                  pokemon_data["defense"], pokemon_data["types"])
                self.ajouter_pokemon(pokemon)

    def ajouter_pokemon(self, pokemon):
        # Vérifier si le Pokemon est déjà dans le Pokedex
        if pokemon in self.pokemons:
            print(f"{pokemon.nom} est déjà dans le Pokedex !")
        else:
            self.pokemons.append(pokemon)
            print(f"{pokemon.nom} a été ajouté au Pokedex !")

    def afficher_pokemons(self):
        # Afficher la liste des Pokemons et leur nombre
        pokemon_counts = {}
        for pokemon in self.pokemons:
            if pokemon.nom in pokemon_counts:
                pokemon_counts[pokemon.nom] += 1
            else:
                pokemon_counts[pokemon.nom] = 1
        for nom, count in pokemon_counts.items():
            print(f"{nom} : {count} rencontre(s)")

    def sauvegarder(self):
        # Sauvegarder les Pokemons dans le fichier pokedex.json
        data = []
        for pokemon in self.pokemons:
            pokemon_data = {"nom": pokemon.nom, "vie": pokemon.vie, "puissance_attaque": pokemon.puissance_attaque,
                            "defense": pokemon.defense, "types": pokemon.types}
            data.append(pokemon_data)
        with open("pokedex.json", "w") as f:
            json.dump(data, f)

class Combat():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def lancer_combat(self):
        print(f"{self.p1.nom} ({self.p1.vie} PV) VS {self.p2.nom} ({self.p2.vie} PV)")

        while True:
            # Tour de p1
            self.p1.attaquer(self.p2)
            if self.p2.vie == 0:
                print(f"{self.p1.nom} gagne le combat !")
                break

            # Tour de p2
            self.p2.attaquer(self.p1)
            if self.p1.vie == 0:
                print(f"{self.p2.nom} gagne le combat !")
                break
# Create two Pokemons
p1 = Pokemon("Pikachu", 100, 10, 5, ["electric"])
p2 = Pokemon("Salamèche", 120, 8, 7, ["fire"])

# Create a Combat instance and launch the battle
combat = Combat(p1, p2)
combat.lancer_combat()
play.mainloop()