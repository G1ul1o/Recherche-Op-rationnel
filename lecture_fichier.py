
def lecture_fichier(fichier):
    nbr_C = 0
    nbr_P = 0
    nbr_C_P_bool=True
    remplissage_prix_unitaire=False
    extraction_commandes=False

    with open("./proposition_de_transport/proposition " + fichier + ".txt", "r") as f:

        # extraction des données
        for line in f:

            data = line.strip().split()

            #extraction de la première ligne
            if nbr_C_P_bool==True :
                nbr_C= int(data[1])
                nbr_P = int(data[0])
                nbr_C_P_bool = False

                #création de la matrice (+1 car on a les provisions et les commandes
                matrice = [[0] * (nbr_C+1) for z in range(nbr_P+1)]

                indice = 0
                remplissage_prix_unitaire=True

            elif remplissage_prix_unitaire==True:

                #On rempli la matrice des prix unitaires + provision
                for i in range (nbr_C+1):
                    print(indice)
                    print(data[i])
                    matrice[indice][i]= data[i]
                indice+=1

                if indice == nbr_P:
                    remplissage_prix_unitaire=False
                    extraction_commandes=True

            elif extraction_commandes==True:


                for i in range (nbr_C):

                    matrice[indice][i]=data[i]


    return nbr_C, nbr_P, matrice