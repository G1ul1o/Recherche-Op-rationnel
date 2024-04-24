from lecture_fichier import *
from fonction_général import *
from Nord_Ouest import *


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


    def Methode_NO():
        global matrice_NO
        matrice_NO = Nord_Ouest(matrice, nbr_C, nbr_P)

        print("La matrice avec la méthode de Nord-Ouest est :")
        for row in matrice_NO:
            print(row)






    while continuer == True:

        if choix == 1:
            lire_fichier()
            afficher_matrices()
            Methode_NO()


        if continuer == True:
            choix = int(input(  "Que souhaitez-vous faire ?\n"
                                "1. Changer de fichier\n"
                                "2. Quitter\n"
                                "Entrez votre choix : "))