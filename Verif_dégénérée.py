from Class_graph import *
def creation_graphe (proposition_de_transport,nbr_C,nbr_P):

    graph=[]

    #boucle pour former tout les S
    for i in range (nbr_P):
        #on crée une table des liaison pour chaque sommet S
        tab_liaison= []
        for j in range (nbr_C):

            if proposition_de_transport[i][j] > 0:
                tab_liaison.append("C"+str(j+1))

        sommet = Sommet("P"+str(i+1),tab_liaison)

        graph.append(sommet)

    # boucle pour former tout les C
    for i in range(nbr_C):
        # on crée une table des liaison pour chaque sommet C
        tab_liaison = []
        for j in range(nbr_P):
            #On ajoute les liaisons
            if proposition_de_transport[j][i] > 0:
                tab_liaison.append("P"+str(j+1))

        sommet = Sommet("C" + str(i+1), tab_liaison)

        graph.append(sommet)

    return graph

def recherche_indice (graph,sommet_a_trouver):
    #On recherche  l'indice par rapport à son nom
    for i in range(len(graph)):
        if graph[i].nom_sommet == sommet_a_trouver:
            return i
def verif_cycle (graph):
    sommet_parcouru = []
    verif = True
    cycle = []
    nbr_C=0
    verif=True
    #On récuoère le nbr de C
    for element in graph:
        if element.nom_sommet[0] == "C":
            nbr_C += 1
    #On cherche le cycle ici
    for i in range (nbr_C):
        if verif == True:
            index = recherche_indice(graph, "C"+str(i+1))
            C = graph[index]
            # On passe dans les successeurs de C1
            for liaison in C.liaison:
                sommet_parcouru = []
                sommet_parcouru.append("C"+str(i+1))
                sommet_parcouru.append(liaison)
                index = recherche_indice(graph, liaison)
                verif, sommet_cycle = verif_cycle_recursif(graph[index], "C"+str(i+1), sommet_parcouru, graph, True)

    if verif == False:
        cycle = []
        index = recherche_indice(graph, sommet_cycle)
        for liaison in (graph[index].liaison):
            chemin = []
            chemin.append(sommet_cycle)
            # On cherche la première liaison
            index = recherche_indice(graph, liaison)
            chemin.append(liaison)
            recherche_cycle(graph[index], sommet_cycle, cycle, graph, sommet_cycle, chemin)
            if len(cycle) > 0:
                return verif, cycle
    return verif, cycle

def verif_cycle_recursif(sommet,sommet_parent,sommet_parcouru,graph,verif):
    sommet_cycle = "A"
    for liaison in sommet.liaison:
        if verif == True:
            if liaison != sommet_parent and liaison not in sommet_parcouru:
                index = recherche_indice(graph, liaison)
                sommet_parcouru.append(liaison)
                verif, sommet_cycle = verif_cycle_recursif(graph[index], sommet.nom_sommet, sommet_parcouru, graph,
                                                           verif)
            elif liaison in sommet_parcouru and liaison != sommet_parent:
                sommet_cycle = liaison
                return False, sommet_cycle
        else:
            return False, sommet_cycle
    # Nous sommes arrivés à un sommet qui n'a pas d'autres successeur que son parent
    return verif, sommet_cycle

    #Nous sommes arrivés à un sommet qui n'a pas d'autres successeur que son parent
    return nbr_sommet_parcouru,sommet_cycle

def recherche_cycle (sommet,sommet_parent,cycle,graph,sommet_départ,chemin_parcouru):

    if sommet.nom_sommet == sommet_départ:
        for i in range (len(chemin_parcouru)):
            cycle.append(chemin_parcouru[i])
        return
    # On récupère les liaisons dans le graph on veut le cycle donc on ne compare pas avec chemin parcouru
    for liaison in sommet.liaison:

        if liaison != sommet_parent:
            stockage_chemin_intermediaire = []

            for i in range(len(chemin_parcouru)):
                stockage_chemin_intermediaire.append(chemin_parcouru[i])


            stockage_chemin_intermediaire.append(liaison)
            index = recherche_indice(graph,liaison)
            recherche_cycle(graph[index], sommet.nom_sommet, cycle,graph,sommet_départ,stockage_chemin_intermediaire)
    return
def Maximisation (graph,cycle,propositon_de_transport,ligne_ajouter,nbr_C,nbr_P):
    #extraction des données indice 0 lettre et indice 1 chiffre :
    indice_ligne_ajouter = int(''.join([caractere for caractere in ligne_ajouter[0] if caractere.isdigit()]))-1
    indice_colonne_ajouter = int(''.join([caractere for caractere in ligne_ajouter[1] if caractere.isdigit()]))-1
    sommet_cycle_C = "C"+str(''.join([caractere for caractere in ligne_ajouter[1] if caractere.isdigit()]))
    sommet_cycle_P = "P"+ str(''.join([caractere for caractere in ligne_ajouter[0] if caractere.isdigit()]))

    # On cherche la première liaison
    index = recherche_indice(graph, sommet_cycle_P)
    composition_cycle = []

     #Organisation du cycle
    indice = 0
    indice_P=0
    indice_C=0
    cycle_organise=[]
    element_predecedent = None

    for element in cycle :
        if element == sommet_cycle_C or element == sommet_cycle_P:
            if element_predecedent == sommet_cycle_P:
                indice_P=indice-1
                indice_C =indice

            elif element_predecedent == sommet_cycle_C:
                indice_C=indice-1
                indice_P=indice

        element_predecedent = element
        indice+=1


    cycle_organise.append(cycle[indice_C])
    cycle_organise.append(cycle[indice_P])


    #On repart du plus petit indice et repartir de là si P est après le C on va vers l'avant sinon on va en arrière dans le tableau cycle
    if indice_C>indice_P:
        #Parcous à l'inverse
        for i in range (indice_P-1,-1,-1):
            cycle_organise.append(cycle[i])

        #On récupére le reste toujours à l'inverse
        for j in range(len(cycle)-1,indice_C-1,-1):

            if cycle_organise[-1] != cycle[j]:
                cycle_organise.append(cycle[j])

    else:
        #Parcous à l'endroit
        for i in range(indice_P, len(cycle)):
            if cycle_organise[-1] != cycle[i]:
                cycle_organise.append(cycle[i])

        for j in range(indice_C+1):

            if cycle_organise[-1]!= cycle[j]:
                cycle_organise.append(cycle[j])


    print("Le cycle est :", cycle_organise)

    if cycle_organise[0][0] == "C":
        for i in range (len(cycle_organise)):
            ligne = cycle_organise[i]

            if ligne[0]=="P":
                case_cycle = []
                case_cycle.append(int(''.join([caractere for caractere in ligne if caractere.isdigit()]))-1)
                case_cycle.append(int(''.join([caractere for caractere in cycle_organise[i-1] if caractere.isdigit()]))-1)
                composition_cycle.append(case_cycle)

                case_cycle = []
                case_cycle.append(int(''.join([caractere for caractere in ligne if caractere.isdigit()]))-1)
                case_cycle.append(int(''.join([caractere for caractere in cycle_organise[i +1] if caractere.isdigit()]))-1)
                composition_cycle.append(case_cycle)

    a_compenser = -1


    pair = 0

    for case_cycle in composition_cycle:

        if pair %2 != 0:   #on récupère les impairs car c'est que nous poupons comparé car -delta
            if a_compenser == -1:
                a_compenser = propositon_de_transport[case_cycle[0]][case_cycle[1]]
            else:
                a_compenser = min(propositon_de_transport[case_cycle[0]][case_cycle[1]], a_compenser)

        pair +=1



    pair = 0
    sommet_a_supprimer = []

    for element in composition_cycle:
        if pair % 2 == 0:
            propositon_de_transport[element[0]][element[1]]+=a_compenser
        else:
            if propositon_de_transport[element[0]][element[1]]- a_compenser == 0:
                sommet_a_supprimer.append(element)
            propositon_de_transport[element[0]][element[1]]-=a_compenser

        pair+=1



    for i in range(len(graph)):
        for indice in sommet_a_supprimer:
            if len(indice)>1 :
                if graph[i].nom_sommet == "P"+str(indice[0]+1):
                    graph[i].liaison.remove("C"+str(indice[1]+1))

                elif graph[i].nom_sommet == "C"+str(indice[1]+1):
                    graph[i].liaison.remove("P"+str(indice[0]+1))

    if a_compenser == 0:
        return True
    else:
        return False

def detection_de_connexe(graph,nbr_sommet):
    sommet_parcouru = []
    verif = True
    nbr_arrete_parcouru=0

    # On récupère C1
    index = recherche_indice(graph, "C1")
    C1 = graph[index]
    sommet_parcouru.append("C1")

    # On passe dans les successeurs de C1
    for liaison in C1.liaison:
        sommet_parcouru.append(liaison)
        nbr_arrete_parcouru+=1

        index = recherche_indice(graph, liaison)

        nbr_arrete_parcouru= detection_de_connexe_recursif(graph,graph[index],nbr_arrete_parcouru, sommet_parcouru)



    if nbr_arrete_parcouru != nbr_sommet - 1:
        verif=False
        print("Ce graphe n'est connexe pas car le nombre d'arrête (",nbr_arrete_parcouru,") n'est pas égal au nombre de sommet (",nbr_sommet,") - 1 soit ici:",nbr_sommet-1)
        print()
    else:
        verif=True
        print("Ce graphe est  connexe car le nombre d'arrête (",nbr_arrete_parcouru,") est égal  au nombre de sommet (",nbr_sommet,") - 1 soit ici:",nbr_sommet-1)
        print()
    return verif
def detection_de_connexe_recursif(graph,sommet,nbr_sommet_parcouru,sommet_parcouru):
    for liaison in sommet.liaison:
            if liaison not in sommet_parcouru:

                index = recherche_indice(graph, liaison)
                sommet_parcouru.append(liaison)
                nbr_sommet_parcouru+=1

                nbr_sommet_parcouru = detection_de_connexe_recursif(graph,graph[index],nbr_sommet_parcouru, sommet_parcouru)


    # Nous sommes arrivés à un sommet qui n'a pas d'autres successeur que son parent
    return nbr_sommet_parcouru

def recherche_des_sous_graphes_connexes(graph,nbr_P):
    #matrice contenant tout les chemins de sous_graphes_connexes
    sous_graphes_connexes = []
    chemin_parcouru = []
    for indice_ligne in range(nbr_P):
        verif_sous_graphes_présence = False
        nom_sommet_P = ("P"+str(indice_ligne+1))
        for indice_sous_graphes_connexes in range (len(sous_graphes_connexes)):
            if (nom_sommet_P in sous_graphes_connexes[indice_sous_graphes_connexes]):
                verif_sous_graphes_présence = True

        #si le sommet n'est pas présent on continue sinon on ne le commence pas
        if verif_sous_graphes_présence == False:
            index=recherche_indice(graph,nom_sommet_P)
            recherche_des_sous_graphes_connexes_recursif(graph[index],chemin_parcouru,graph)
            sous_graphes_connexes.append(chemin_parcouru)
            chemin_parcouru=[]

    return sous_graphes_connexes

def recherche_des_sous_graphes_connexes_recursif(sommet,chemin_parcouru,graph):
    chemin_parcouru.append(sommet.nom_sommet)
    #On cherche les sous graphes de manière récursif
    for liaison in sommet.liaison:
        if liaison not in chemin_parcouru:
            index = recherche_indice(graph,liaison)
            recherche_des_sous_graphes_connexes_recursif(graph[index],chemin_parcouru,graph)

def graphe_connexe (sous_graphes_connexes,matrice,graph):
    #Ici  nous allons récuperer toutes les liaisons possible tout les sommet de provision P du premier graph avec tout les sommets de commandes C du deuxième et à l'inverse ensuite on les compare
    #Et nous gardons le plus faible
    sommet_ajouter_connexe = []
    indice_ligne_graphe = []
    indice_colonne_graphe_bis=[]

    for sommet in sous_graphes_connexes[0]:
        if sommet[0] == "P":
            indice_ligne_graphe.append(int(''.join([caractere for caractere in sommet if caractere.isdigit()]))-1)

        if sommet[0] == "C":
            indice_colonne_graphe_bis.append(int(''.join([caractere for caractere in sommet if caractere.isdigit()]))-1)


    for i in range (1,len(sous_graphes_connexes)):
        indice_colonne_graphe_connexe = []
        indice_ligne_graphe_connexe_bis = []

        for sommet in sous_graphes_connexes[i]:
            if sommet[0] == "C":
                indice_colonne_graphe_connexe.append(int(''.join([caractere for caractere in sommet if caractere.isdigit()]))-1)

            if sommet[0] == "P":
                indice_ligne_graphe_connexe_bis.append(int(''.join([caractere for caractere in sommet if caractere.isdigit()]))-1)

        cout_case_minimum = 100000000000
        indice_colonne_ajouter = 0
        indice_ligne_ajouter = 0

        for indice_ligne in indice_ligne_graphe:
            for indice_colonne in indice_colonne_graphe_connexe:

                if cout_case_minimum > (matrice[indice_ligne][indice_colonne]):
                    cout_case_minimum = matrice[indice_ligne][indice_colonne]
                    indice_ligne_ajouter = indice_ligne
                    indice_colonne_ajouter = indice_colonne


        for indice_ligne_bis in indice_ligne_graphe_connexe_bis :
            for indice_colonne_bis in indice_colonne_graphe_bis :
                #on prend le minimum de  cout

                if cout_case_minimum > (matrice[indice_ligne_bis][indice_colonne_bis]):

                    cout_case_minimum = matrice[indice_ligne_bis][indice_colonne_bis]
                    indice_ligne_ajouter = indice_ligne_bis
                    indice_colonne_ajouter = indice_colonne_bis




        sommet_ajouter =[]
        for i in range(len(graph)):
                if graph[i].nom_sommet == ("C"+str(indice_colonne_ajouter+1)):
                    graph[i].liaison.append("P"+str(indice_ligne_ajouter+1))
                    print("Ajout de la liaison","C"+str(indice_colonne_ajouter+1),"P"+str(indice_ligne_ajouter+1),"pour rendre notre gaphe connexe")
                    print()
                    sommet_ajouter.append("P"+str(indice_ligne_ajouter+1))
                    sommet_ajouter.append("C"+str(indice_colonne_ajouter+1))

                if graph[i].nom_sommet == ("P"+str(indice_ligne_ajouter+1)):
                    graph[i].liaison.append("C" + str(indice_colonne_ajouter + 1))

        sommet_ajouter_connexe.append(sommet_ajouter)
    return sommet_ajouter_connexe

#point d'amélioration non  réussi
def graphe_connexe_sigma (sous_graphes_connexes,matrice,graph,sous_graphe_deja_ajoute):
    sommet_ajouter_connexe = []
    indice_ligne_graphe = []
    indice_colonne_graphe_bis = []
    for sommet in sous_graphes_connexes[0]:
        if sommet[0] == "P":
            indice_ligne_graphe.append(int(sommet[1]) - 1)
        if sommet[0] == "C":
            indice_colonne_graphe_bis.append(int(sommet[1]) - 1)

    for i in range(1, len(sous_graphes_connexes)):
        indice_colonne_graphe_connexe = []
        indice_ligne_graphe_connexe_bis = []

        for sommet in sous_graphes_connexes[i]:
            if sommet[0] == "C":
                indice_colonne_graphe_connexe.append(int(sommet[1]) - 1)
            if sommet[0] == "P":
                indice_ligne_graphe_connexe_bis.append(int(sommet[1]) - 1)

        cout_case_minimum = 100000000000
        cout_case_minimum_min = 1000000000000
        indice_colonne_ajouter = 0
        indice_ligne_ajouter = 0

        for indice_ligne in indice_ligne_graphe:
            for indice_colonne in indice_colonne_graphe_connexe:

                if cout_case_minimum > (matrice[indice_ligne][indice_colonne]):
                    cout_case_minimum = matrice[indice_ligne][indice_colonne]
                    indice_ligne_ajouter = indice_ligne
                    indice_colonne_ajouter = indice_colonne

        for indice_ligne_bis in indice_ligne_graphe_connexe_bis:
            for indice_colonne_bis in indice_colonne_graphe_bis:
                # on prend le minimum de  cout
                if cout_case_minimum > (matrice[indice_ligne_bis][indice_colonne_bis]):

                    cout_case_minimum = matrice[indice_ligne_bis][indice_colonne_bis]
                    indice_ligne_ajouter = indice_ligne_bis
                    indice_colonne_ajouter = indice_colonne_bis


        sommet_ajouter = []
        for i in range(len(graph)):
            if graph[i].nom_sommet == ("C" + str(indice_colonne_ajouter + 1)):
                graph[i].liaison.append("P" + str(indice_ligne_ajouter + 1))
                print("Ajout de la liaison", "C" + str(indice_colonne_ajouter + 1), "P" + str(indice_ligne_ajouter + 1)) #pour rendre notre gaphe connexe
                print()
                sommet_ajouter.append("P" + str(indice_ligne_ajouter + 1))
                sommet_ajouter.append("C" + str(indice_colonne_ajouter + 1))

            if graph[i].nom_sommet == ("P" + str(indice_ligne_ajouter + 1)):
                graph[i].liaison.append("C" + str(indice_colonne_ajouter + 1))

        sommet_ajouter_connexe.append(sommet_ajouter)
    return sommet_ajouter_connexe

#Point d'amélioration non réussi
def sigma_0_connexe (sous_graphes_connexes,graph):


    for indice_graphe_connexes in range (len(sous_graphes_connexes)):
       for sommet_parent in sous_graphes_connexes[indice_graphe_connexes]:
           for indice_graphe in range (len(graph)):
                if graph[indice_graphe].nom_sommet == sommet_parent and sommet_parent[0]== "P":
                    for sommet_fils in sous_graphes_connexes[indice_graphe_connexes]:
                        if sommet_fils[0] == "C" and sommet_fils in graph[indice_graphe].liaison:
                            graph[indice_graphe].liaison.remove(sommet_fils)

                elif graph[indice_graphe].nom_sommet == sommet_parent and sommet_parent[0]== "C":
                    for sommet_fils in sous_graphes_connexes[indice_graphe_connexes]:
                        if sommet_fils[0] == "P" and sommet_fils in graph[indice_graphe].liaison:
                            graph[indice_graphe].liaison.remove(sommet_fils)




