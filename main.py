from lecture_fichier import *
from Balas import *
from fonction_général import *
from Nord_Ouest import *
from Verif_dégénérée import *


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
    print("On va donc remplir la proposition choisi avec la méthode de balas-Hammer :\n")
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

def afficher_matrices():

        affichage_couts(matrice,nbr_C,nbr_P)

def afficher_proposition_de_transport():

      affichage_proposition_de_transport(matrice,matrice,nbr_C,nbr_P)


def Methode_NO():
        global matrice_NO
        matrice_NO = Nord_Ouest(matrice, nbr_C, nbr_P)

        print("La matrice avec la méthode de Nord-Ouest est :")

        affichage_proposition_de_transport(matrice,matrice_NO,nbr_C,nbr_P)

def verif_degeneree():
        global gaph
        graph = creation_graphe(matrice_NO,nbr_C,nbr_P)
        for i in range(len(graph)):
            print(graph[i].nom_sommet, ",", graph[i].liaison)


        verif = verif_cycle(graph)
        print(verif)


if __name__ == '__main__':
    continuer = True
    choix = 1

    while continuer:
        if choix == 1:
            lire_fichier()
        elif choix == 3:
            afficher_matrice_transport()

        
            afficher_matrices()
            Methode_NO()
            verif_degeneree()


        elif choix == 2:
            continuer = False

            
        choix = int(input("Que souhaitez-vous faire ?\n"
                          "1. Changer de fichier\n"
                          "2. Quitter\n"
                          "3. Afficher la matrice de transport\n"
                          "Entrez votre choix : "))