import time
from lecture_fichier import *
from Balas import *
from fonction_général import *
from Nord_Ouest import *
from Verif_dégénérée import *
from cout_potentiels_marginaux import *
import random


# time.clock() a été retiré de la bibliothèque Python depuis Python 3.8 on utilise donc time.procces_tim() qui a la même fonction


#Creation matrice aléatoire
def generation_matrice_aleatoire(taille_matrice):

    matrice_prix_unitaire_aleatoire = [([0] * (taille_matrice)) for z in range(taille_matrice)]  #création de la matrice aléatoire
    temp = [([0] * (taille_matrice)) for z in range(taille_matrice)]


    for indice_ligne in range (taille_matrice):
        for indice_colonne in range (taille_matrice):
            matrice_prix_unitaire_aleatoire[indice_ligne][indice_colonne] = nombre_aleatoire = random.randint(1, 100)

    for indice_ligne in range (taille_matrice):
        for indice_colonne in range (taille_matrice):
            temp[indice_ligne][indice_colonne] = nombre_aleatoire = random.randint(1, 100)

    #calcul pour les provisions
    provisions = []
    for indice_ligne in range(taille_matrice):
        somme_provision = 0
        for indice_colonne in range (taille_matrice):
                somme_provision += temp[indice_ligne][indice_colonne]
        provisions.append(somme_provision)

    #calcul pour les commandes
    commandes = []
    for indice_colonne in range(taille_matrice):
        somme_commande = 0
        for indice_ligne in range (taille_matrice):
            somme_commande+= temp[indice_ligne][indice_colonne]
        commandes.append(somme_commande)

    #ajout des provisions dans les lignes
    for indice_ligne in range (taille_matrice):
        matrice_prix_unitaire_aleatoire[indice_ligne].append(provisions[indice_ligne])

    matrice_prix_unitaire_colonne = []
    for indice_colonne in range (taille_matrice):
        #on récupère les commandes
        matrice_prix_unitaire_colonne.append(commandes[indice_colonne])

    #on fait la somme pour le dernier
    somme_commande_provision=0
    for element in provisions :
        somme_commande_provision += element

    #on ajoute la somme puis la ligne à notre matrice
    matrice_prix_unitaire_colonne.append(somme_commande_provision)
    matrice_prix_unitaire_aleatoire.append(matrice_prix_unitaire_colonne)
    return  matrice_prix_unitaire_aleatoire

if __name__ == '__main__':
    #match choix:

    choix = int(input("Que souhaitez-vous faire ?\n"
                      "1. Afficher la matrice de transport avec la méthode de Nord Ouest\n"
                      "2. Afficher la matrice de transport avec Balas\n"
                      "3. Optimisé la méthode de Nord Ouest avec la méthode du marche pieds\n"
                      "4. Optimisé la méthode de Balas avec la méthode du marche pieds\n"
                      "Entrez votre choix : "))

    if choix == 1:
        nuage_de_points = []
        for i in range (100):
            # Creation matrice aléatoire
            taille_matrice = int(input("Quel taille voulez-vous implémenter ?"))
            matrice_prix_unitaire_aleatoire = generation_matrice_aleatoire(taille_matrice)

            #time.clock() a été retiré de la bibliothèque Python depuis Python 3.8 on utilise donc time.procces_tim() qui a la même fonction
            debut = time.process_time()
            matrice_NO = Nord_Ouest(matrice_prix_unitaire_aleatoire, taille_matrice, taille_matrice)
            fin = time.process_time()

            duree = fin - debut
            nuage_de_points.append(duree)
        print(nuage_de_points)

    if choix == 2 :
        nuage_de_points = []
        for i in range(100):
            taille_matrice = int(input("Quel taille voulez-vous implémenter ?"))
            matrice_prix_unitaire_aleatoire = generation_matrice_aleatoire(taille_matrice)
            provisions = [int(matrice_prix_unitaire_aleatoire[i][-1]) for i in range(taille_matrice)]
            commandes = [int(matrice_prix_unitaire_aleatoire[-1][j]) for j in range(taille_matrice)]

            debut = time.process_time()
            matrice_de_transport = remplir_matrice_transport(matrice_prix_unitaire_aleatoire, provisions, commandes)
            fin = time.process_time()

            duree = fin - debut
            nuage_de_points.append(duree)
        print(nuage_de_points)

