from Class_graph import *
from Verif_dégénérée import *
def recherche_indice (graph,sommet_a_trouver):

    for i in range(len(graph)):
        if graph[i].nom_sommet == sommet_a_trouver:
            return i

def calcul_matrice_potentiels_marginaux (graph,matrice,nbr_P,nbr_C):


    for indice_ligne in range(nbr_P):
        nom_sommet = "P"+str(indice_ligne+1)
        index= recherche_indice(graph,nom_sommet)

        for indice_colonne in range (len(matrice[indice_ligne])):
            graph[index].cout_unitaire.append(matrice[indice_ligne][indice_colonne])

    indices_potentiels = []

    for indice_ligne in range (nbr_P):
        nom_sommet = "P" + str(indice_ligne + 1)
        index = recherche_indice(graph, nom_sommet)

        indices_potentiel = []
        for liaison in graph[index].liaison:
            indices_potentiel.append(int(''.join([caractere for caractere in liaison if caractere.isdigit()]))) #récupère uniquement les chiffres pas les lettres
        indices_potentiels.append(indices_potentiel)




    #On pose E(P(X)) =0
    for i in range (len(graph)):
        for liaison in graph[i].liaison:
            if liaison[0] == "P":
                sommet_nul = liaison

    indexP = recherche_indice(graph,sommet_nul)
    graph[indexP].cout_potentiel = 0 #E(P(X) = 0

    for indices_potentiel in indices_potentiels[indexP]:
        index = recherche_indice(graph,("C"+str(indices_potentiel)))
        graph[index].cout_potentiel = - (graph[indexP].cout_unitaire[indices_potentiel-1])
    rempli = False

    while rempli==False:
        rempli = True
        for sommet in graph:
            print(sommet.nom_sommet,sommet.cout_potentiel)
            if sommet.cout_potentiel == None :
                rempli = False
        if rempli==False:

            for i in range(len(indices_potentiels)):
                index_P = recherche_indice(graph, "P" + str(i + 1))
                for indices_potentiel in indices_potentiels[i]:
                    index_C = recherche_indice(graph,"C"+str(indices_potentiel)) #ici l'indice correxpond vraiment à la lettre


                    if graph[index_C].cout_potentiel != None and  graph[index_P].cout_potentiel==None:
                        graph[index_P].cout_potentiel = (graph[index_P].cout_unitaire[indices_potentiel - 1]) + graph[index_C].cout_potentiel

                    elif graph[index_C].cout_potentiel == None and graph[index_P].cout_potentiel !=None :
                        graph[index_C].cout_potentiel = - ((graph[index_P].cout_unitaire[indices_potentiel - 1]) - graph[index_P].cout_potentiel)



    matrice_cout_potentiels = []

    for i in range (nbr_P):
        matrice_cout_potentiels_ligne = []
        for j in range (nbr_C):
            matrice_cout_potentiels_ligne.append(graph[i].cout_potentiel - graph[j+(nbr_P)].cout_potentiel) #l'indice ne change pas parce qu'on part toujours de 0 donc on peut ajouter un nombre constant
        matrice_cout_potentiels.append(matrice_cout_potentiels_ligne)

    matrice_couts_marginaux = []
    for i in range (nbr_P):
        matrice_couts_marginaux_ligne = []
        for j in range (nbr_C):
            matrice_couts_marginaux_ligne.append(graph[i].cout_unitaire[j] - matrice_cout_potentiels[i][j])
        matrice_couts_marginaux.append(matrice_couts_marginaux_ligne)

    return matrice_cout_potentiels, matrice_couts_marginaux

def selection_arrete_maximisé(matrice_cout_marginaux,graph):
    min_valeur_arretee = 0
    presence_arrete_negative = False
    for i in range (len(matrice_cout_marginaux)):
        for j in range (len(matrice_cout_marginaux[i])):
            if matrice_cout_marginaux[i][j] < min_valeur_arretee :
                min_valeur_arretee = matrice_cout_marginaux[i][j]
                indice_arrete_ajouter_ligne = i
                indice_arrete_ajouter_colonne = j
                presence_arrete_negative=True

    arrete_a_ajouter = []
    if presence_arrete_negative == True:
        arrete_a_ajouter.append("P"+str(indice_arrete_ajouter_ligne+1))
        arrete_a_ajouter.append("C"+str(indice_arrete_ajouter_colonne+1))
        index_P = recherche_indice(graph,"P"+str(indice_arrete_ajouter_ligne+1))
        graph[index_P].liaison.append("C"+str(indice_arrete_ajouter_colonne+1))
        index_C = recherche_indice(graph,"C"+str(indice_arrete_ajouter_colonne+1))
        graph[index_C].liaison.append("P"+str(indice_arrete_ajouter_ligne+1))

        #print("L'arrête",arrete_a_ajouter,"a un coût marginal négatif on l'ajoute donc a notre graphe")

    else:
        d=1 #a retirer
        #print("La solution proposé est optimale")

    return presence_arrete_negative,arrete_a_ajouter

