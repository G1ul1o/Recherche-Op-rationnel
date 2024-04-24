import pandas as lecture #bibliothèque de DataFrame
def affichage_couts(matrice,nbr_C, nbr_P):
    nom_C= []
    nom_P = []

    # On crée les légendes des tableaux (C)
    for i in range(nbr_C):
        nom_C.append("C"+str(i+1))

    # on ajoute toutes les nom d'état dans une seul liste (P)
    for i in range(nbr_P):
        nom_P.append("P"+str(i+1))

    L2 = []
    for i in range(nbr_P):
        L=[]
        for j in range(nbr_C):
            L.append(matrice[i][j])
        L2.append(L)

    df = lecture.DataFrame(L2,index=nom_C,columns=nom_P)
    print(df)

def affichage_proposition_de_transport(matrice,matrice_avec_nbr_de_commande,nbr_C, nbr_P):

    nom_C = []
    nom_P = []

    # On crée les légendes des tableaux (C)
    for i in range(nbr_C):
        nom_C.append("C" + str(i + 1))

    # on ajoute toutes les nom d'état dans une seul liste (P)
    for i in range(nbr_P):
        nom_P.append("P" + str(i + 1))

    L2 = []
    for i in range(nbr_P):
        L = []
        for j in range(nbr_C):
            L3=[]

            L3.append(matrice[i][j])
            L3.append(matrice_avec_nbr_de_commande[i][j])
            L.append(L3)

        L2.append(L)

    df = lecture.DataFrame(L2, index=nom_C, columns=nom_P)
    print(df)

