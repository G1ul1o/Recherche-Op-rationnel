from lecture_fichier import *
from Balas import *

def lire_fichier():
    global nbr_C, nbr_P, matrice

    fichier = input("Entrez le numéro du fichier que vous voulez tester:")
    nbr_C, nbr_P, matrice = lecture_fichier(fichier)

    print("La matrice est :")
    for i in range(nbr_P + 1):
        for j in range(nbr_C + 1):
            print(matrice[i][j], end=" ")
        print()


def afficher_matrice_transport():
    global matrice, nbr_P, nbr_C, matrice_de_transport
    provisions = [int(matrice[i][-1]) for i in range(nbr_P)]
    commandes = [int(matrice[-1][j]) for j in range(nbr_C)]
    matrice_de_transport = remplir_matrice_transport(matrice, provisions, commandes)
    for i in range(len(matrice_de_transport)):
        matrice_de_transport[i].append(provisions[i])
    ajout_commande = []
    for commande in commandes:
        ajout_commande.append(commande)
    matrice_de_transport.append(ajout_commande)
    print("Matrice de transport:")
    for ligne in matrice_de_transport:
        print(ligne)

if __name__ == '__main__':
    continuer = True
    choix = 1

    while continuer:
        if choix == 1:
            lire_fichier()
        elif choix == 3:
            afficher_matrice_transport()

        choix = int(input("Que souhaitez-vous faire ?\n"
                          "1. Changer de fichier\n"
                          "2. Quitter\n"
                          "3. Afficher la matrice de transport\n"
                          "Entrez votre choix : "))

        if choix == 2:
            continuer = False
