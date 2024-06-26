import pandas as lecture #bibliothèque de DataFrame
from tabulate import tabulate
from termcolor import colored
def affichage_couts(matrice,nbr_C, nbr_P):
    data = []

    for i in range(nbr_P):
        ligne = []
        ligne.append("P" + str(i + 1))

        for j in range(nbr_C):

            ligne.append(matrice[i][j])
        ligne.append(matrice[i][nbr_C])
        data.append(ligne)

    # Ligne des provisions
    ligne = []
    ligne.append("Commande")
    for j in range(nbr_C):
        ligne.append(matrice[nbr_P][j])
    data.append(ligne)

    headers = [" "]

    for i in range(nbr_C):
        headers.append("C" + str(i + 1))
    headers.append("Provision")

    print(tabulate(data, headers=headers, tablefmt="mixed_outline", numalign="right"))

def affichage_couts_potentiels_marginaux (matrice,nbr_C,nbr_P):
    data = []

    for i in range(nbr_P):
        ligne = []
        ligne.append("P" + str(i + 1))

        for j in range(nbr_C):
            ligne.append(matrice[i][j])
        data.append(ligne)

    headers = [" "]

    for i in range(nbr_C):
        headers.append("C" + str(i + 1))

    print(tabulate(data, headers=headers, tablefmt="mixed_outline", numalign="right"))
def affichage_proposition_de_transport(matrice,matrice_avec_nbr_de_commande,nbr_C, nbr_P):

    data = []

    for i in range(nbr_P):
        ligne = []
        ligne.append("P"+str(i+1))

        for j in range (nbr_C):
            valeurs = []

            valeurs.append(matrice_avec_nbr_de_commande[i][j])
            valeurs.append(matrice[i][j])


            ligne.append(valeurs)
        ligne.append(matrice[i][nbr_C])
        data.append(ligne)


    #Ligne des provisions
    ligne = []
    ligne.append("Commande")
    for j in range (nbr_C+1):
        ligne.append(matrice_avec_nbr_de_commande[nbr_P][j])
    data.append(ligne)

    headers = [" "]

    for i in range (nbr_C):
        headers.append("C"+str(i+1))
    headers.append("Provision")

    print(tabulate(data,headers=headers,tablefmt="mixed_outline",numalign="right"))


