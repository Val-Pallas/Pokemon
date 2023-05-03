import random


class Pokemon:

    def __init__(self, attack_choice):

        self.__attack_choice = attack_choice

    def attack(self):

        if self.__attack_choice == 1:
            attack_points = random.randint(18, 25)
            return attack_points

        elif self.__attack_choice == 2:
            attack_points = random.randint(10, 35)
            return attack_points

        else:
            print("That is not a selection. You lost your turn!")

    def heal(self):

        heal_points = random.randint(18, 25)
        return heal_points


user_health = 100
player_health = 100
battle_continue = True

while battle_continue == True:
    print("\nATTACK CHOICES\n1. Close range attack\n2. Far range attack\n3. Heal")
    attack_choice = eval(input("\nSelect an attack: "))

    if player_health == 100:
        player_choice = random.randint(1, 2)

    else:
        player_choice = random.randint(1, 3)

    player = Pokemon(player_choice)
    user_pokemon = Pokemon(attack_choice)

    if attack_choice == 1 or attack_choice == 2:
        damage_to_player = user_pokemon.attack()
        heal_self = 0
        print("You dealt", damage_to_player, "damage.")

    if player_choice == 1 or player_choice == 2:
        damage_to_user = player.attack()
        heal_player = 0
        print("player dealt", damage_to_user, "damage.")

    if attack_choice == 3:
        heal_self = user_pokemon.heal()
        damage_to_player = 0
        print("You healed", heal_self, "health points.")

    if player_choice == 3:
        heal_mew = player.heal()
        damage_to_user = 0
        print("player healed", heal_player, "health points.")

    user_health = user_health - damage_to_user + heal_self
    player_health = player_health - damage_to_player + heal_player

    if user_health > 100:
        user_health = 100

    elif user_health <= 0:
        user_health = 0
        battle_continue = False

    if player_health > 100:
        player_health = 100

    elif player_health <= 0:
        player_health = 0
        battle_continue = False

    print("Your current health is", user_health)
    print("player's current health is", player_health)

print("Your final health is", user_health)
print("player's final health is", player_health)

if user_health < player_health:

    print("\nYou lost! Better luck next time!")

else:

    print("\nYou won against!")