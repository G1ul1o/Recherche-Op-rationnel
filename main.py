from lecture_fichier import *
from fonction_général import *


if __name__ == '__main__':
    continuer = True
    choix = 1


    def lire_fichier():
        global nbr_C, nbr_P, matrice

        fichier = input("Entrez le numéro du fichier que vous voulez tester:")

        nbr_C, nbr_P, matrice = lecture_fichier(fichier)

        print("La matrice est :")

    def afficher_matrices():

        affichage_couts(matrice,nbr_C,nbr_P)

    def afficher_proposition_de_transport():

        affichage_proposition_de_transport(matrice,matrice,nbr_C,nbr_P)






    while continuer == True:

        if choix == 1:
            lire_fichier()
            afficher_matrices()


        if continuer == True:
            choix = int(input(  "Que souhaitez-vous faire ?\n"
                                "1. Changer de fichier\n"
                                "2. Quitter\n"
                                "Entrez votre choix : "))