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
    affichage_couts(matrice, nbr_C, nbr_P)



def Methode_Balas():
    global matrice_de_transport
    provisions = [int(matrice[i][-1]) for i in range(nbr_P)]
    commandes = [int(matrice[-1][j]) for j in range(nbr_C)]
    print("On va donc remplir la proposition choisi avec la méthode de balas-Hammer :\n")
    matrice_de_transport = remplir_matrice_transport(matrice, provisions, commandes)
    ajout_commande = []
    for commande in commandes:
        ajout_commande.append(commande)
    matrice_de_transport.append(ajout_commande)
    '''print("Matrice de transport:")
    for ligne in matrice_de_transport:
        print(ligne)'''
    affichage_proposition_de_transport(matrice,matrice_de_transport,nbr_C,nbr_P)

def afficher_matrices():

        affichage_couts(matrice,nbr_C,nbr_P)

def afficher_proposition_de_transport():

      affichage_proposition_de_transport(matrice,matrice,nbr_C,nbr_P)


def Methode_NO():
        global matrice_NO
        matrice_NO = Nord_Ouest(matrice, nbr_C, nbr_P)

        print("La matrice avec la méthode de Nord-Ouest est :")

        affichage_proposition_de_transport(matrice,matrice_NO,nbr_C,nbr_P)

def verif_degeneree(matrice_transport):
        global graph
        verif_presence_cycle = False
        verif_connexe= False
        graph = creation_graphe(matrice_transport,nbr_C,nbr_P)


        while verif_presence_cycle == False or verif_connexe == False:

            #vérification présence cycle
            verif_presence_cycle,cycle = verif_cycle(graph)

            if verif_presence_cycle == True :
                print("Cette proposition de transport est acyclique")
                print()

            else:
                print("Ce graphe contient un cycle", cycle)
                print()

            #vérification connexe
            nbr_sommet =  nbr_C + nbr_P
            verif_connexe = detection_de_connexe(graph, nbr_sommet)

            if verif_connexe == False:
                print("Les sous graphes connexes composant la proposition sont : ")
                print()

                sous_graphes_connexes = recherche_des_sous_graphes_connexes(graph, nbr_P)
                for indice_print in range (len(sous_graphes_connexes)):
                    print("Le sous graphe numéro",indice_print+1,"est composant des sommets :",sous_graphes_connexes[indice_print])
                print()
                graphe_connexe(sous_graphes_connexes, matrice_transport,graph)

                for i in range(len(graph)):
                    print(graph[i].nom_sommet, ",", graph[i].liaison)
                print()

if __name__ == '__main__':
    continuer = True
    choix = 1

    while continuer:
        if choix == 1:
            lire_fichier()
        elif choix == 2:
            continuer = False
        elif choix == 3:
            afficher_matrices()
            Methode_NO()
            verif_degeneree(matrice_NO)

        elif choix ==4:
            afficher_matrices()
            Methode_Balas()
            verif_degeneree(matrice_de_transport)

        choix = int(input("Que souhaitez-vous faire ?\n"
                          "1. Changer de fichier\n"
                          "2. Quitter\n"
                          "3. Afficher la matrice de transport avec la méthode de Nord Ouest\n"
                          "4. Afficher la matrice de transport avec Balas\n"
                          "Entrez votre choix : "))