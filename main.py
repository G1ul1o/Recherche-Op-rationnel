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

def afficher_penalites():
    global matrice, nbr_P, nbr_C
    global indices_max_ligne, indices_max_colonne  # Déclarer comme variables globales

   # penalites_lignes, penalites_colonnes = calcul_penalites(matrice, nbr_P, nbr_C)
'''    print("Pénalités des lignes (provisions) : ", penalites_lignes)
    print("Pénalités des colonnes (commandes) : ", penalites_colonnes)

    indices_max_ligne, indices_max_colonne = trouver_penalite_maximale(penalites_lignes, penalites_colonnes)
    print("Indices des lignes avec pénalité maximale : ", indices_max_ligne)
    print("Indices des colonnes avec pénalité maximale : ", indices_max_colonne)
'''
def afficher_meilleur_choix():
    global matrice, nbr_P, nbr_C
    global indices_max_ligne, indices_max_colonne  # Assurez-vous que ces variables sont accessibles

    provisions = [int(matrice[i][-1]) for i in range(nbr_P)]
    commandes = [int(matrice[-1][j]) for j in range(nbr_C)]
    meilleur_choix = choisir_case(matrice, indices_max_ligne, indices_max_colonne, provisions, commandes)
    print("Meilleur choix : Ligne", meilleur_choix['ligne'], "Colonne", meilleur_choix['colonne'],
          "avec un coût de", meilleur_choix['cout'], "et une quantité maximale de", meilleur_choix['quantite'])
def afficher_matrice_transport():
    global matrice, nbr_P, nbr_C
    # Assurez-vous que provisions et commandes sont définis correctement
    provisions = [int(matrice[i][-1]) for i in range(nbr_P)]
    commandes = [int(matrice[-1][j]) for j in range(nbr_C)]
    matrice_de_transport = remplir_matrice_transport(matrice, provisions, commandes)

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
            afficher_penalites()
        elif choix == 4:
            afficher_meilleur_choix()
        elif choix == 5:
            afficher_matrice_transport()

        choix = int(input("Que souhaitez-vous faire ?\n"
                          "1. Changer de fichier\n"
                          "2. Quitter\n"
                          "3. Afficher les pénalités et les indices de pénalité maximale\n"
                          "4. Afficher le meilleur choix\n"  
                          "5. Afficher la matrice de transport\n"
                          "Entrez votre choix : "))

        if choix == 2:
            continuer = False
