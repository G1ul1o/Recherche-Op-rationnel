from lecture_fichier import *


if __name__ == '__main__':
    continuer = True
    choix = 1


    def lire_fichier():
        global nbr_C, nbr_P, matrice

        fichier = input("Entrez le numéro du fichier que vous voulez tester:")

        nbr_C, nbr_P, matrice = lecture_fichier(fichier)

        print("La matrice est :")

        for i in range (nbr_P+1):
            for j in range (nbr_C+1):
                print(matrice[i][j], end=" ")
            print()



    while continuer == True:

        if choix == 1:
            lire_fichier()

        if continuer == True:
            choix = int(input(  "Que souhaitez-vous faire ?\n"
                                "1. Changer de fichier\n"
                                "2. Quitter\n"
                                "Entrez votre choix : "))