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

            if proposition_de_transport[j][i] > 0:
                tab_liaison.append("P"+str(j+1))

        sommet = Sommet("C" + str(i+1), tab_liaison)

        graph.append(sommet)

    return graph

def recherche_indice (graph,sommet_a_trouver):

    for i in range(len(graph)):
        if graph[i].nom_sommet == sommet_a_trouver:
            return i
def verif_cycle (graph):

    sommet_parcouru = []
    verif=True
    cycle=[]

    #On récupère C1
    index = recherche_indice(graph,"C1")
    C1 = graph[index]
    sommet_parcouru.append("C1")


    #On passe dans les successeurs de C1
    for liaison in C1.liaison:
        sommet_parcouru.append(liaison)

        index = recherche_indice(graph, liaison)

        verif,sommet_cycle= verif_cycle_recursif(graph[index],"C1",sommet_parcouru,graph,True)

    if verif == False:
        cycle = []

        index = recherche_indice(graph,sommet_cycle)

        for liaison in (graph[index].liaison):
            chemin = []
            chemin.append(sommet_cycle)
            #On cherche la première liaison
            index = recherche_indice(graph,liaison)

            chemin.append(liaison)
            recherche_cycle(graph[index],sommet_cycle,cycle,graph,sommet_cycle,chemin)

            if len(cycle) > 0:
                return verif,cycle

    return  verif,cycle

def verif_cycle_recursif(sommet,sommet_parent,sommet_parcouru,graph,verif):

    sommet_cycle="A"
    for liaison in sommet.liaison:

        if verif == True:

            if liaison != sommet_parent and liaison not in sommet_parcouru:

                index = recherche_indice(graph,liaison)
                sommet_parcouru.append(liaison)

                verif,sommet_cycle = verif_cycle_recursif(graph[index],sommet.nom_sommet,sommet_parcouru,graph,verif)

            elif liaison in sommet_parcouru and liaison != sommet_parent:
                sommet_cycle = liaison
                return False,sommet_cycle
        else:
            return False,sommet_cycle

    #Nous sommes arrivés à un sommet qui n'a pas d'autres successeur que son parent
    return verif,sommet_cycle

def recherche_cycle (sommet,sommet_parent,cycle,graph,sommet_départ,chemin_parcouru):

    if sommet.nom_sommet == sommet_départ:
        for i in range (len(chemin_parcouru)):
            cycle.append(chemin_parcouru[i])
        return

    # On récupère les liaisons dans le graph
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

    indices_P = []
    indices_C = []
    #extraction des données indice 0 lettre et indice 1 chiffre :
    indice_ligne_ajouter = int(ligne_ajouter[0][1])-1
    indice_colonne_ajouter = int(ligne_ajouter[1][1])-1

    composition_cycle = []
    if cycle[0][0]=="C":
        for i in range (len(cycle)):
            ligne = cycle[i]

            if ligne[0]=="P":
                case_cycle = []
                case_cycle.append(int(ligne[1])-1)
                case_cycle.append(int(cycle[i-1][1])-1)
                composition_cycle.append(case_cycle)

                case_cycle = []
                case_cycle.append(int(ligne[1])-1)
                case_cycle.append(int(cycle[i +1][1])-1)
                composition_cycle.append(case_cycle)
    else :
        for i in range(len(cycle)):
            colonne = cycle[i]
            if colonne[0] == "C":
                case_cycle = []
                case_cycle.append(int(cycle[i - 1][1]) - 1)
                case_cycle.append(int(colonne[1]) - 1)
                composition_cycle.append(case_cycle)

                case_cycle = []
                case_cycle.append(int(cycle[i + 1][1]) - 1)
                case_cycle.append(int(colonne[1]) - 1)
                composition_cycle.append(case_cycle)

    for case_cycle in composition_cycle:
        if case_cycle[0] == indice_ligne_ajouter and case_cycle[1]!= indice_colonne_ajouter:
            a_compenser_ligne = propositon_de_transport[indice_ligne_ajouter][case_cycle[1]]
            indice_colonne_a_supprimer = case_cycle[1]

        if case_cycle[0] != indice_ligne_ajouter and case_cycle[1] == indice_colonne_ajouter:
            a_compenser_colonne = propositon_de_transport[case_cycle[0]][indice_colonne_ajouter]
            indice_ligne_a_supprimer = case_cycle[0]


    #on chosi entre les deux
    if  a_compenser_ligne < a_compenser_colonne:
        a_compenser=a_compenser_ligne
        propositon_de_transport[indice_ligne_ajouter][indice_colonne_a_supprimer] = 0
        print("On supprime la liaison:",("P"+ str(indice_ligne_ajouter+1)),("C"+str(indice_colonne_a_supprimer+1)))
    else:
        a_compenser = a_compenser_colonne
        propositon_de_transport[indice_ligne_a_supprimer][indice_colonne_ajouter] = 0
        print("On supprime la liaison:", ("P" + str(indice_ligne_a_supprimer+1)), ("C" + str(indice_colonne_ajouter + 1)))

    if propositon_de_transport[indice_ligne_ajouter][nbr_C] >= a_compenser and propositon_de_transport[nbr_P][indice_colonne_ajouter]>=a_compenser:
        propositon_de_transport[indice_ligne_ajouter][indice_colonne_ajouter] = a_compenser
    else:
        propositon_de_transport[indice_ligne_ajouter][indice_colonne_ajouter]=min(propositon_de_transport[indice_ligne_ajouter][nbr_C],propositon_de_transport[nbr_P][indice_colonne_ajouter])
        a_compenser = a_compenser - propositon_de_transport[indice_ligne_ajouter][indice_colonne_ajouter]

    for case_cycle in composition_cycle:
        if case_cycle[1] == indice_colonne_ajouter and case_cycle[0]!=indice_ligne_ajouter:
            if (propositon_de_transport[case_cycle[0]][indice_colonne_ajouter] - a_compenser) >= 0:
                propositon_de_transport[case_cycle[0]][indice_colonne_ajouter] -= a_compenser
            else:
                propositon_de_transport[case_cycle[0]][indice_colonne_ajouter] = 0

    ligne = False
    colonne = False
    while ligne!=True or colonne!=True:
        ligne = True
        colonne = True
        for i in range (nbr_P):

            provision = 0

            #valeur absolue
            a_compenser = abs(a_compenser)
            for j in range (nbr_C):
                 provision += propositon_de_transport[i][j]
            print("provision:",provision)
            print("max",propositon_de_transport[i][nbr_C])
            print(propositon_de_transport)
            if provision != propositon_de_transport[i][nbr_C]:
                if provision > propositon_de_transport[i][nbr_C]:
                   a_compenser = -a_compenser
                ajustement_proposition_ligne(propositon_de_transport,i,indice_ligne_ajouter,indice_colonne_ajouter,a_compenser,composition_cycle)
                ligne = False

        for indice_colonne in range(nbr_C):

                provision = 0

                # valeur absolue
                a_compenser = abs(a_compenser)
                for j in range(nbr_P):
                    provision += propositon_de_transport[j][indice_colonne]

                if provision != propositon_de_transport[nbr_P][indice_colonne]:
                    if provision > propositon_de_transport[nbr_P][indice_colonne]:
                        a_compenser = -a_compenser
                    ajustement_proposition_colonne(propositon_de_transport, indice_colonne, indice_ligne_ajouter, indice_colonne_ajouter,
                                                 a_compenser, composition_cycle)
                    colonne=False


def ajustement_proposition_ligne(propositon_de_transport,ligne_a_modifier,indice_ligne_ajouter,indice_colonne_ajouter,a_ajouter,composition_cycle):

    for cycle in composition_cycle:

       if cycle[1] != indice_colonne_ajouter or cycle[0] != indice_ligne_ajouter:
           #on exclu la case que nous avons ajouter et on garde la ligne qu'on veut modifier
           if  cycle[0] == ligne_a_modifier:
                propositon_de_transport[cycle[0]][cycle[1]] += a_ajouter
                return


def ajustement_proposition_colonne (propositon_de_transport,colonne_a_modifer,indice_ligne_ajouter,indice_colonne_ajouter,a_ajouter,composition_cycle):
    print(propositon_de_transport)
    for cycle in composition_cycle:

        if cycle[0] != indice_ligne_ajouter and cycle[1] != indice_colonne_ajouter:
            # on exclu la case que nous avons ajouter et on garde la colonne qu'on veut modifier
            if  cycle[1] == colonne_a_modifer:
                propositon_de_transport[cycle[0]][cycle[1]] += a_ajouter

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
        print("Ce graphe est  connexe car le nombre d'arrête (",nbr_arrete_parcouru,") est égal  au nombre de sommet (",nbr_sommet,") - 1 soit ici:",nbr_sommet-1)

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

    for liaison in sommet.liaison:
        if liaison not in chemin_parcouru:
            index = recherche_indice(graph,liaison)
            recherche_des_sous_graphes_connexes_recursif(graph[index],chemin_parcouru,graph)

def graphe_connexe (sous_graphes_connexes,matrice,graph):

    indice_ligne_graphe = []
    for sommet in sous_graphes_connexes[0]:
        if sommet[0] == "P":
            indice_ligne_graphe.append(int(sommet[1])-1)

    for i in range (1,len(sous_graphes_connexes)):
        indice_colonne_graphe = []

        for sommet in sous_graphes_connexes[i]:
            if sommet[0] == "C":
                indice_colonne_graphe.append(int(sommet[1])-1)

        cout_case_minimum = 100000000000
        indice_colonne_ajouter = 0
        indice_ligne_ajouter = 0

        for indice_ligne in indice_ligne_graphe:
            for indice_colonne in indice_colonne_graphe:

                if cout_case_minimum > (matrice[indice_ligne][indice_colonne]):
                    cout_case_minimum = matrice[indice_ligne][indice_colonne]
                    indice_ligne_ajouter = indice_ligne
                    indice_colonne_ajouter = indice_colonne

        for i in range(len(graph)):

            if graph[i].nom_sommet == ("C"+str(indice_colonne_ajouter+1)):
                graph[i].liaison.append("P"+str(indice_ligne_ajouter+1))
                print("Ajout de la liaison","C"+str(indice_colonne_ajouter+1),"P"+str(indice_ligne_ajouter+1),"pour rendre notre gaphe connexe")
                print()

            if graph[i].nom_sommet == ("P"+str(indice_ligne_ajouter+1)):
                graph[i].liaison.append("C" + str(indice_colonne_ajouter + 1))

