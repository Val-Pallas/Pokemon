from random import shuffle

class Jeu:
    cartes = [
        "As de Coeur", "2 de Coeur", "3 de Coeur", "4 de Coeur", "5 de Coeur", "6 de Coeur", "7 de Coeur", "8 de Coeur",
        "9 de Coeur", "10 de Coeur", "Valet de Coeur", "Dame de Coeur", "Roi de Coeur",
        "As de Pique", "2 de Pique", "3 de Pique", "4 de Pique", "5 de Pique", "6 de Pique", "7 de Pique", "8 de Pique",
        "9 de Pique", "10 de Pique", "Valet de Pique", "Dame de Pique", "Roi de Pique",
        "As de Carreau", "2 de Carreau", "3 de Carreau", "4 de Carreau", "5 de Carreau", "6 de Carreau", "7 de Carreau",
        "8 de Carreau", "9 de Carreau", "10 de Carreau", "Valet de Carreau", "Dame de Carreau", "Roi de Carreau",
        "As de Trèfle", "2 de Trèfle", "3 de Trèfle", "4 de Trèfle", "5 de Trèfle", "6 de Trèfle", "7 de Trèfle",
        "8 de Trèfle", "9 de Trèfle", "10 de Trèfle", "Valet de Trèfle", "Dame de Trèfle", "Roi de Trèfle"
    ]

    def __init__(self):
        self.paquet = list(self.cartes)
        shuffle(self.paquet)
        self.piocher = self.tirer

    def tirer(self):
        return self.paquet.pop()

class Partie:
    def __init__(self, choix_joueur, joueur):
        self.joueur = joueur
        self.main1 = []
        self.main2 = []
        self.talon = []
        self.pioche = []
        for i in range(5):
            self.main1.append(Jeu().tirer())
            self.main2.append(Jeu().tirer())
        self.talon.append(Jeu().tirer())
        self.pioche = Jeu().paquet
        print("Le talon est :", self.talon)

        print("\n\nC'est à", joueur[0], "de jouer")
        s = self.calcul_main(joueur[1])
        while True:
            print("Voulez-vous jouer une carte (1) ou passer (0) ?")
            choix = input()
            if choix == "1":
                print("Quelle carte voulez-vous jouer ?")
                carte = input()
                if carte in s:
                    self.talon.append(carte)
                    s.remove(carte)
                    if len(s) == 0:
                        print("Vous avez gagné !")
                        break
                else:
                    print("Vous ne pouvez pas jouer cette carte")
            else:
                print("Vous passez votre tour")
            print("Le talon est maintenant :", self.talon)
            print("Il reste", len(self.pioche), "cartes dans la pioche")
            input("Appuyez sur entrée pour continuer\n\n")

    #def calcul_main(self, main):
    def calcul_main(main):
        somme = 0
        AS = []
        val = 0
        for item in main:
            if item[0] == '1':
                val = 11
                AS.append(1)
            elif item[0] == '2':
                val = 2
            elif item[0] == '3':
                val = 3
            elif item[0] == '4':
                val = 4
            elif item[0] == '5':
                val = 5
            elif item[0] == '6':
                val = 6
            elif item[0] == '7':
                val = 7
            elif item[0] == '8':
                val = 8
            elif item[0] == '9':
                val = 9
            elif item[0] == '0':
                val = 10
            elif item[0] == 'J':
                val = 10
            elif item[0] == 'Q':
                val = 10
            elif item[0] == 'K':
                val = 10
            somme = somme + val
        if somme == 21 and len(main) == 2:
            print("Black Jack!")
            return (1)
        if somme > 21:
            somme = somme - 10 * len(AS)
        if somme > 21:
            print("Vous avez dépassé 21, vous avez donc perdu.")
            return somme
        print("Votre main a une valeur de :", somme)
        return somme


    def choix_joueur(joueur):
        joueur = Jeu(jeu, joueur).joueur
        return joueur

    # Initialisation des variables
    nom_joueur = []
    pactole_joueur = []
    joueurs = 0

    while joueurs < 2:
        nom = input("Entrez votre nom: ")
        nom_joueur.append(nom)
        pactole = int(input("Entrez votre pactole: "))
        pactole_joueur.append(pactole)
        joueurs += 1

        #Définition de la table de jeu
        #jeu = Jeu(choix_joueur, joueurs)
        jeu = Jeu()

        #Distribution des cartes
        mains_joueurs = []
        for i in range(len(nom_joueur)):
            main = [jeu.piocher(), jeu.piocher()]
        print(nom_joueur[i], "votre main est:", main)
        mains_joueurs.append(main)

        #Jeu des joueurs
        for i in range(len(mains_joueurs)):
            main = mains_joueurs[i]
        # do something with main

        for i in range(len(nom_joueur)):
            print("\nC'est au tour de", nom_joueur[i])
            print("i =", i)
            print("length of mains_joueurs =", len(mains_joueurs))
            
        mains_joueurs = []
        for i in range(len(nom_joueur)):
            main = [jeu.piocher(), jeu.piocher()]
        print(nom_joueur[i], "votre main est:", main)
        mains_joueurs.append(main)

        while True:
                choix = input("Voulez-vous une autre carte? (o/n)")
                if choix == "o":
                    main.append(jeu.piocher())
                    print("Votre main est maintenant:", main)
                valeur_main = calcul_main(main)
                if valeur_main == 21:
                    break
                elif valeur_main > 21:
                    break
                else:
                    break
        n = 4  # define n as the number of players in the game
        mains_joueurs = [[] for _ in range(n)]  # create an empty list for each player's hand

        mains_joueurs = [[] for _ in range(n)]

        mains_joueurs[i] = main
        if i < len(mains_joueurs):
            mains_joueurs[i] = main
        else:
            print("Index out of range") # or handle the error in another way
        print(nom_joueur[i], "votre main est:", main)

        #Détermination du gagnant
        gagnant = ""
        valeur_max = 0
        for i in range(len(nom_joueur)):
            valeur_main = calcul_main(mains_joueurs[i])
        if valeur_main > valeur_max and valeur_main <= 21:
            gagnant = nom_joueur[i]
        valeur_max = valeur_main
        if gagnant == "":
            print("Personne n'a gagné.")
        else:
            print("Le gagnant est", gagnant, "avec une valeur de", valeur_max)

       
