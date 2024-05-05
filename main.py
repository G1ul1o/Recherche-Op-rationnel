from lecture_fichier import *
from Balas import *
from fonction_général import *
from Nord_Ouest import *
from Verif_dégénérée import *
from cout_potentiels_marginaux import *
import time

def lire_fichier():
    global nbr_C, nbr_P, matrice

    fichier = input("Entrez le numéro du fichier que vous voulez tester:")
    nbr_C, nbr_P, matrice = lecture_fichier(fichier)

    print("La matrice des couts est :")
    affichage_couts(matrice, nbr_C, nbr_P)



def Methode_Balas():
    global matrice_de_transport
    provisions = [int(matrice[i][-1]) for i in range(nbr_P)]
    commandes = [int(matrice[-1][j]) for j in range(nbr_C)]
    print("On va créer une proposition de transport de la proposition selectionné avec la méthode de Balas-Hammer :\n")
    matrice_de_transport = remplir_matrice_transport(matrice, provisions, commandes)
    for i in range (nbr_P):
        matrice_de_transport[i].append(provisions[i])

    ajout_commande = []
    somme = 0
    for commande in commandes:
        ajout_commande.append(commande)
        somme+=commande
    ajout_commande.append(somme)
    matrice_de_transport.append(ajout_commande)
    affichage_proposition_de_transport(matrice,matrice_de_transport,nbr_C,nbr_P)

def afficher_matrices():

        affichage_couts(matrice,nbr_C,nbr_P)

def afficher_proposition_de_transport():

      affichage_proposition_de_transport(matrice,matrice,nbr_C,nbr_P)


def Methode_NO():
        global matrice_NO

        print("On va créer une proposition de transport de la proposition selectionné avec la méthode de Nord-Ouest :\n")
        #Lancement de la méthode Nord-Ouest
        matrice_NO = Nord_Ouest(matrice, nbr_C, nbr_P)
        print("La matrice avec la méthode de Nord-Ouest est :")

        affichage_proposition_de_transport(matrice,matrice_NO,nbr_C,nbr_P)
        print()

#verification si la proposition est non-dégénérée
def verif_degeneree(matrice_transport):
        global graph, sous_graphes_connexes, sommet_ajouter_connexe
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
                    print("Le sous graphe numéro",indice_print+1,"est composé des sommets :",sous_graphes_connexes[indice_print])
                print()
                sommet_ajouter_connexe = graphe_connexe(sous_graphes_connexes, matrice,graph)


            else:
                print("Le graph est connexe")

#methode du marche pieds avec potentiels
def methode_marche_avec_potentiels(proposition_de_transport):
    global graph
    continuer = True
    while continuer==True:




        print("Proposition de transport")
        affichage_proposition_de_transport(matrice, proposition_de_transport, nbr_C, nbr_P)

        verif_connexe = False
        presence_arrete_negative = True
        sigma_0 = False
        while presence_arrete_negative == True:
            # creation des matrices de cout potentiel et cout marginaux
            print("On calcule les matrices de couts potentiels et de couts marginaux")

            matrice_cout_potentiel, matrice_cout_marginaux = calcul_matrice_potentiels_marginaux(graph, matrice, nbr_P,nbr_C)

            print("La matrice coûts potentiel:")
            affichage_couts_potentiels_marginaux(matrice_cout_potentiel, nbr_C, nbr_P)

            print("La matrice coûts marginaux:")
            affichage_couts_potentiels_marginaux(matrice_cout_marginaux, nbr_C, nbr_P)

            presence_arrete_negative, arrete_a_ajouter = selection_arrete_maximisé(matrice_cout_marginaux, graph)
            if presence_arrete_negative == True:
                print("Nous avons l'arrête",arrete_a_ajouter, "qui a un coût marginal on l'ajoute comme arrête fictive")
            absence_de_cycle = False
            while absence_de_cycle == False:

                absence_de_cycle, cycle = verif_cycle(graph)
                if absence_de_cycle == False:
                    print("Presence d'un cycle")
                    sigma_0=Maximisation(graph,cycle, proposition_de_transport, arrete_a_ajouter, nbr_C, nbr_P)
                    print("Proposition de transport après maximisation de l'arrête")
                    affichage_proposition_de_transport(matrice, proposition_de_transport, nbr_C, nbr_P)
                    nbr_sommet = nbr_C + nbr_P
                    verif_connexe = detection_de_connexe(graph, nbr_sommet)

                    if verif_connexe == False:
                        print("Les sous graphes connexes composant la proposition sont : ")
                        print()

                        sous_graphes_connexes = recherche_des_sous_graphes_connexes(graph, nbr_P)
                        for indice_print in range(len(sous_graphes_connexes)):
                            print("Le sous graphe numéro", indice_print + 1, "est composé des sommets :",
                                  sous_graphes_connexes[indice_print])
                        print()
                        sommet_ajouter_connexe = graphe_connexe(sous_graphes_connexes, matrice, graph)

                    if sigma_0 == True :
                        presence_arrete_negative = False  #si la valeur de delta est égal à 0 alors on ne peut rien faire

                    #Test sigma
                    '''if sigma_0 == True:
                        print("sigma")
                        sigma_0_connexe(sommet_ajouter_connexe,graph)
                        print("Les sous graphes connexes composant la proposition sont : ")
                        print()

                        sous_graphes_connexes = recherche_des_sous_graphes_connexes(graph, nbr_P)
                        for indice_print in range(len(sous_graphes_connexes)):
                            print("Le sous graphe numéro", indice_print + 1, "est composant des sommets :",
                                  sous_graphes_connexes[indice_print])
                        print()
                        sommet_ajouter_connexe_sigma = graphe_connexe(sous_graphes_connexes, matrice, graph)
                        print(sommet_ajouter_connexe_sigma)
                        for i in range (len(graph)):
                            print(graph[i].nom_sommet,graph[i].liaison)'''

                '''if sigma_0==True:
                    print("sigma")
                    sigma_0_connexe(sommet_ajouter_connexe_sigma, graph)
                    sous_graphes_connexes = recherche_des_sous_graphes_connexes(graph, nbr_P)
                    for indice_print in range(len(sous_graphes_connexes)):
                        print("Le sous graphe numéro", indice_print + 1, "est composant des sommets :",
                              sous_graphes_connexes[indice_print])
                    sommet_ajouter_connexe_sigma = graphe_connexe_sigma(sous_graphes_connexes, proposition_de_transport,graph,sommet_ajouter_connexe_sigma)
                    input()
                    print(sommet_ajouter_connexe_sigma)
                    for i in range(len(graph)):
                        print(graph[i].nom_sommet, graph[i].liaison)'''



        continuer=False





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

            if matrice_NO!=None:
                verif_degeneree(matrice_NO)
                methode_marche_avec_potentiels(matrice_NO)
                print("Proposotion finale:")
                affichage_proposition_de_transport(matrice, matrice_NO, nbr_C, nbr_P)


        elif choix ==4:
            afficher_matrices()
            Methode_Balas()
            verif_degeneree(matrice_de_transport)
            methode_marche_avec_potentiels(matrice_de_transport)
            print("Proposotion finale:")
            affichage_proposition_de_transport(matrice, matrice_de_transport, nbr_C, nbr_P)

        if continuer == True:
            choix = int(input("Que souhaitez-vous faire ?\n"
                          "1. Changer de fichier\n"
                          "2. Quitter\n"
                          "3. Afficher la matrice de transport avec la méthode de Nord Ouest\n"
                          "4. Afficher la matrice de transport avec Balas\n"
                          "Entrez votre choix : "))