import copy

def Nord_Ouest(matrice, nbr_C, nbr_P):


    matrice_copy = copy.deepcopy(matrice)
    somme_p = 0
    somme_c = 0

    matrice_NO = [([0] * (nbr_C+1)) for z in range(nbr_P+1)] #création de la matrice Nord-Ouest


    #remplissage des valeurs

    for i in range(nbr_P): #on parcourt les lignes
        for j in range(nbr_C): #on parcourt les colonnes
            if matrice_copy[i][nbr_C] > 0 and matrice_copy[nbr_P][j] > 0: #s'il reste des provisions et des commandes
                matrice_NO[i][j] = min(matrice_copy[i][nbr_C], matrice_copy[nbr_P][j]) #on prend le minimum entre les provisions et les commandes et on  met la valeur dans la matrice
                matrice_copy[i][nbr_C] -= matrice_NO[i][j] #on enlève les provisions utilisées
                matrice_copy[nbr_P][j] -= matrice_NO[i][j] #on enlève les commandes utilisées



    #ajout des propositions et des commandes dans la matrice
    for i in range(nbr_P+1):
        matrice_NO[i][nbr_C] = matrice[i][nbr_C]  #ajout des commandes
        somme_c += matrice[i][nbr_C]

    for j in range(nbr_C+1):
        matrice_NO[nbr_P][j] = matrice[nbr_P][j] #ajout des propositions
        somme_p += matrice[nbr_P][j]
    
    if somme_c == somme_p:
        print("Les propositions et les commandes sont équilibrées")
        matrice_NO[nbr_P][nbr_C] = somme_c
        return matrice_NO
    else:
        print("Les propositions et les commandes ne sont pas équilibrées")
        return None




