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
def Maximisation (graph,cycle):
    print()


proposition_de_transport1 = [[5,5,0,0],[0,30,2,3],[0,0,10,10]]
proposition_de_transport2 = [[0,2000,3000,0],[0,1000,2000,3000],[5000,0,0,1000]]
nbr_C = 4
nbr_S = 3

graph1 = creation_graphe(proposition_de_transport1,nbr_C,nbr_S)
graph2 = creation_graphe(proposition_de_transport2,nbr_C,nbr_S)

for i in range(len(graph1)):
    print(graph1[i].nom_sommet ,",", graph1[i].liaison)
    if graph1[i].nom_sommet=="C1":
        liaison = graph1[i].liaison

verif = verif_cycle(graph1)

print(verif)
'''
for i in range(len(graph2)):
    print(graph2[i].nom_sommet ,",", graph2[i].liaison)
    if graph2[i].nom_sommet=="C1":
        liaison = graph2[i].liaison

verif = verif_cycle(graph2)

print (verif)'''


