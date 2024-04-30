import time
from lecture_fichier import *
from Balas import *
from fonction_général import *
from Nord_Ouest import *
from Verif_dégénérée import *
from cout_potentiels_marginaux import *
import random
import matplotlib.pyplot as plt



'''# Données du tableau
categories = ['A', 'B', 'C', 'D']
valeurs = [10, 20, 15, 25]

# Créer le graphe
plt.bar(categories, valeurs)

# Ajouter des étiquettes et un titre
plt.xlabel('Catégories')
plt.ylabel('Valeurs')
plt.title('Graphe à barres')'''

# Afficher le graphe
plt.show()
# time.clock() a été retiré de la bibliothèque Python depuis Python 3.8 on utilise donc time.procces_tim() qui a la même fonction

#verification si la proposition est non-dégénérée
def verif_degeneree(matrice_transport,taille_matrice):
        global graph
        verif_presence_cycle = False
        verif_connexe= False
        graph = creation_graphe(matrice_transport,taille_matrice,taille_matrice)


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
            nbr_sommet =  taille_matrice + taille_matrice
            verif_connexe = detection_de_connexe(graph, nbr_sommet)

            if verif_connexe == False:
                print("Les sous graphes connexes composant la proposition sont : ")
                print()

                sous_graphes_connexes = recherche_des_sous_graphes_connexes(graph, taille_matrice)
                for indice_print in range (len(sous_graphes_connexes)):
                    print("Le sous graphe numéro",indice_print+1,"est composant des sommets :",sous_graphes_connexes[indice_print])
                print()
                graphe_connexe(sous_graphes_connexes, matrice_transport,graph)

def methode_marche_avec_potentiels(proposition_de_transport,matrice_cout_unitaire_aleatoire,taille_matrice):
    continuer = True
    while continuer==True:
        #creation des matrices de cout potentiel et cout marginaux
        #print("On calcule les matrices de couts potentiels et de couts marginaux")
        graph = creation_graphe(proposition_de_transport, taille_matrice, taille_matrice)
        matrice_cout_potentiel, matrice_cout_marginaux = calcul_matrice_potentiels_marginaux(graph, matrice_cout_unitaire_aleatoire,taille_matrice,taille_matrice)

        '''print("La matrice coûts potentiel:")
        affichage_couts_potentiels_marginaux(matrice_cout_potentiel, taille_matrice, taille_matrice)'''

        '''print("La matrice coûts marginaux:")
        affichage_couts_potentiels_marginaux(matrice_cout_marginaux, taille_matrice, taille_matrice)'''

        absence_de_cycle = False
        verif_connexe = False

        presence_arrete_negative, arrete_a_ajouter = selection_arrete_maximisé(matrice_cout_marginaux, graph)

        '''print("Proposition de transport")
        affichage_proposition_de_transport(matrice_cout_unitaire_aleatoire, proposition_de_transport, taille_matrice, taille_matrice)'''

        if presence_arrete_negative == True:

            while absence_de_cycle == False:

                absence_de_cycle, cycle = verif_cycle(graph)
                if absence_de_cycle == False:
                   # print("Presence d'un cycle")

                    Maximisation(graph, cycle, proposition_de_transport, arrete_a_ajouter, taille_matrice, taille_matrice)
                    graph = creation_graphe(proposition_de_transport, taille_matrice, taille_matrice)
                    '''print("Proposition de transport après maximisation de l'arrête")
                    affichage_proposition_de_transport(matrice_cout_unitaire_aleatoire, proposition_de_transport, taille_matrice, taille_matrice)
                    print()'''



        continuer=False

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

    choix = int(input("Que souhaitez-vous faire ?\n"
                      "1. Afficher la matrice de transport avec la méthode de Nord Ouest\n"
                      "2. Afficher la matrice de transport avec Balas\n"
                      "3. Optimisé la méthode de Nord Ouest avec la méthode du marche pieds\n"
                      "4. Optimisé la méthode de Balas avec la méthode du marche pieds\n"
                      "Entrez votre choix : "))

    if choix== 1:
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

    elif choix ==2 :
            nuage_de_points = []
            for i in range(100):
                taille_matrice = int(input("Quel taille voulez-vous implémenter ?"))
                matrice_prix_unitaire_aleatoire = generation_matrice_aleatoire(taille_matrice)
                provisions = [int(matrice_prix_unitaire_aleatoire[i][-1]) for i in range(taille_matrice)]
                commandes = [int(matrice_prix_unitaire_aleatoire[-1][j]) for j in range(taille_matrice)]

                print("debut")
                debut = time.process_time()
                matrice_de_transport = remplir_matrice_transport(matrice_prix_unitaire_aleatoire, provisions, commandes)
                fin = time.process_time()

                duree = fin - debut
                print(duree)
                nuage_de_points.append(duree)
            print(nuage_de_points)

    elif choix == 3 :
            nuage_de_points = []
            for i in range(100):
                # Creation matrice aléatoire
                taille_matrice = int(input("Quel taille voulez-vous implémenter ?"))
                matrice_cout_unitaire_aleatoire = generation_matrice_aleatoire(taille_matrice)

                # time.clock() a été retiré de la bibliothèque Python depuis Python 3.8 on utilise donc time.procces_tim() qui a la même fonction
                debut = time.process_time()
                matrice_NO = Nord_Ouest(matrice_cout_unitaire_aleatoire, taille_matrice, taille_matrice)
                verif_degeneree(matrice_NO)
                methode_marche_avec_potentiels(matrice_NO,matrice_cout_unitaire_aleatoire,taille_matrice)
                fin = time.process_time()

                duree = fin - debut
                nuage_de_points.append(duree)
            print(nuage_de_points)

    elif choix == 4 :

            nuage_de_points = []
            for i in range(100):
                # Creation matrice aléatoire
                taille_matrice = int(input("Quel taille voulez-vous implémenter ?"))
                matrice_cout_unitaire_aleatoire = generation_matrice_aleatoire(taille_matrice)
                provisions = [int(matrice_cout_unitaire_aleatoire[i][-1]) for i in range(taille_matrice)]
                commandes = [int(matrice_cout_unitaire_aleatoire[-1][j]) for j in range(taille_matrice)]

                # time.clock() a été retiré de la bibliothèque Python depuis Python 3.8 on utilise donc time.procces_tim() qui a la même fonction
                debut = time.process_time()
                proposition_de_transport = remplir_matrice_transport(matrice_cout_unitaire_aleatoire, provisions, commandes)
                verif_degeneree(proposition_de_transport)
                methode_marche_avec_potentiels(proposition_de_transport, matrice_cout_unitaire_aleatoire, taille_matrice)
                fin = time.process_time()

                duree = fin - debut
                nuage_de_points.append(duree)
            print(nuage_de_points)

