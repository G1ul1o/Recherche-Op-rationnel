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
            a_compenser = propositon_de_transport[indice_ligne_ajouter][case_cycle[1]]
            propositon_de_transport[indice_ligne_ajouter][case_cycle[1]] = 0




    propositon_de_transport[indice_ligne_ajouter][indice_colonne_ajouter] = a_compenser

    for case_cycle in composition_cycle:
        if case_cycle[1] == indice_colonne_ajouter and case_cycle[0]!=indice_ligne_ajouter:
            propositon_de_transport[case_cycle[0]][indice_colonne_ajouter] -= a_compenser


    ligne = False
    colonne = False
    while ligne!=True and colonne!=True:
        ligne = True
        colonne = True
        for i in range (nbr_P):

            provision = 0

            #valeur absolue
            a_compenser = abs(a_compenser)
            for j in range (nbr_C):
                 provision += propositon_de_transport[i][j]
            if provision != propositon_de_transport[i][nbr_C]:
                if provision > propositon_de_transport[i][nbr_C]:
                    a_compenser= (-a_compenser)
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
                    a_compenser = (-a_compenser)
                ajustement_proposition_colonne(propositon_de_transport, indice_colonne, indice_ligne_ajouter, indice_colonne_ajouter,
                                             a_compenser, composition_cycle)
                colonne=False


def ajustement_proposition_ligne(propositon_de_transport,ligne_a_modifier,indice_ligne_ajouter,indice_colonne_ajouter,a_ajouter,composition_cycle):

   for cycle in composition_cycle:

       if cycle[1] != indice_colonne_ajouter :
           #on exclu la case que nous avons ajouter et on garde la ligne qu'on veut modifier
           if cycle[0] != indice_ligne_ajouter and cycle[0]==ligne_a_modifier:

                propositon_de_transport[cycle[0]][cycle[1]] += a_ajouter


def ajustement_proposition_colonne (propositon_de_transport,colonne_a_modifer,indice_ligne_ajouter,indice_colonne_ajouter,a_ajouter,composition_cycle):
    for cycle in composition_cycle:

        if cycle[0] != indice_ligne_ajouter:
            # on exclu la case que nous avons ajouter et on garde la colonne qu'on veut modifier
            if cycle[1] != indice_colonne_ajouter and cycle[1] == colonne_a_modifer:

                propositon_de_transport[cycle[0]][cycle[1]] += a_ajouter


proposition_de_transport1 = [[5,5,30,25,60],[0,30,0,0,30],[45,45,0,0,90],[50,75,30,25,180]]
proposition_de_transport2 = [[35,0,0,25,60],[0,4,30,0,30],[15,75,0,0,90],[50,75,30,25,180]]
nbr_C = 4
nbr_P = 3

graph1 = creation_graphe(proposition_de_transport1,nbr_C,nbr_P)
graph2 = creation_graphe(proposition_de_transport2,nbr_C,nbr_P)

for i in range(len(graph1)):
    print(graph1[i].nom_sommet ,",", graph1[i].liaison)
    if graph1[i].nom_sommet=="C1":
        liaison = graph1[i].liaison

verif,cycle = verif_cycle(graph1)

print(verif)
print(cycle)

Maximisation(graph1,cycle,proposition_de_transport1,["P1","C2"],nbr_C,nbr_P)

print(proposition_de_transport1)
print("fini")

for i in range(len(graph2)):
    print(graph2[i].nom_sommet ,",", graph2[i].liaison)
    if graph2[i].nom_sommet=="C3":
        graph2[i].liaison.append("P1")

verif,cycle = verif_cycle(graph2)
print(verif)
print(cycle)

if verif == False :
    Maximisation(graph2,cycle,proposition_de_transport2,["P2","C2"],nbr_C,nbr_P)

print(proposition_de_transport2)
print("fini")


