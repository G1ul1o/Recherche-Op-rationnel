from lecture_fichier import lecture_fichier


def calcul_penalites(matrice, nbr_P, nbr_C,ligne_banni,colonne_banni):
    penalites_lignes = []
    penalites_colonnes = []
    for i in range(nbr_P):
        if i not in ligne_banni:
            couts_ligne = sorted([int(matrice[i][j]) for j in range(nbr_C) if j not in colonne_banni])
            penalite_ligne = couts_ligne[1] - couts_ligne[0] if len(couts_ligne) >= 2 else 0
            penalites_lignes.append(penalite_ligne)
        else:
            penalites_lignes.append(-1)
    for j in range(nbr_C):
        if j not in colonne_banni:
            couts_colonne = sorted([int(matrice[i][j]) for i in range(nbr_P) if i not in ligne_banni])
            penalite_colonne = couts_colonne[1] - couts_colonne[0] if len(couts_colonne) >= 2 else 0

            penalites_colonnes.append(penalite_colonne)
        else :
            penalites_colonnes.append(-1)
    print(penalites_colonnes)
    return penalites_lignes, penalites_colonnes


def trouver_penalite_maximale(penalites_lignes, penalites_colonnes):
    max_penalite_ligne = max(penalites_lignes)
    max_penalite_colonne = max(penalites_colonnes)
    max_penalite_globale = max(max_penalite_ligne, max_penalite_colonne)

    indices_max_ligne = [i for i, x in enumerate(penalites_lignes) if x == max_penalite_globale]
    indices_max_colonne = [j for j, x in enumerate(penalites_colonnes) if x == max_penalite_globale]
    print(penalites_colonnes[0])
    print(indices_max_colonne, "ici")
    print(max_penalite_globale,"sisi")
    return indices_max_ligne, indices_max_colonne

def choisir_case(matrice, indices_max_ligne, indices_max_colonne, provisions, commandes, ligne_banni, colonne_banni):
    candidats = []

    for i in indices_max_ligne:
            if i not in ligne_banni:
                cout_minimum_ligne = 1000
                case_choisie_ligne = None
                for j in range(len(matrice[i])-1):
                    cout_actuel = int(matrice[i][j])
                    if cout_actuel < cout_minimum_ligne:
                        cout_minimum_ligne = cout_actuel
                        if provisions[i]< commandes[j]:
                            direction = 'ligne'
                        else:
                            direction = 'colonne'
                        case_choisie_ligne = {'ligne': i, 'colonne': j, 'cout': cout_actuel, 'quantite': min(provisions[i], commandes[j]), 'direction': direction}
                if case_choisie_ligne:
                    candidats.append(case_choisie_ligne)
                    case_choisie_ligne = None

    for j in indices_max_colonne:
        print(j)
        if j not in colonne_banni:
            cout_minimum_colonne = 1000
            case_choisie_colonne = None
            for i in range(len(matrice)-1):
                if i not in ligne_banni:
                    cout_actuel = int(matrice[i][j])
                    if cout_actuel < cout_minimum_colonne:
                        cout_minimum_colonne = cout_actuel
                        if provisions[i]< commandes[j]:
                            direction = 'ligne'
                        else:
                            direction = 'colonne'
                        case_choisie_colonne = {'ligne': i, 'colonne': j, 'cout': cout_actuel, 'quantite': min(provisions[i], commandes[j]), 'direction': direction}
                        print(case_choisie_colonne)

            if case_choisie_colonne:
                candidats.append(case_choisie_colonne)

    # Comparer les candidats pour trouver celui qui permet de transporter la quantité maximale
    meilleur_choix = None
    quantite_maximale = 0
    for candidat in candidats:
        if candidat['quantite'] > quantite_maximale:
            meilleur_choix = candidat
            quantite_maximale = candidat['quantite']

    return meilleur_choix


def remplir_matrice_transport(matrice, provisions, commandes):
    nbr_P = len(provisions)
    nbr_C = len(commandes)
    ligne_banni = []
    colonne_banni = []
    matrice_transport = [[-1] * nbr_C for i in range(nbr_P)]
    copie = []
    for i in range(len(matrice)):
        copie_intermédiaire = []
        for j in range(len(matrice[i])):
            copie_intermédiaire.append(matrice[i][j])
        copie.append(copie_intermédiaire)


    end = False
    while end == False:  # Tant qu'il reste des provisions et des demandes
        end = True
        for i in range(nbr_P):
            for j in range(nbr_C):
                if matrice_transport[i][j] == -1:
                    end=False

        if end == False :
            penalites_lignes, penalites_colonnes = calcul_penalites(copie, nbr_P, nbr_C,ligne_banni,colonne_banni)
            indices_max_ligne, indices_max_colonne = trouver_penalite_maximale(penalites_lignes, penalites_colonnes)
            print("test")
            meilleur_choix = choisir_case(matrice, indices_max_ligne, indices_max_colonne, provisions, commandes, ligne_banni, colonne_banni)
            print("terminer")
            matrice_transport[meilleur_choix['ligne']][meilleur_choix['colonne']] = meilleur_choix['quantite']
            if meilleur_choix['direction'] == 'ligne':
                for i in range(nbr_C):
                    if i != meilleur_choix['colonne']:
                        matrice_transport[meilleur_choix['ligne']][i] = 0
                ligne_banni.append(meilleur_choix['ligne'])
            else:
                for i in range(nbr_P):
                    if i != meilleur_choix['ligne']:
                        matrice_transport[i][meilleur_choix['colonne']] = 0
                colonne_banni.append(meilleur_choix['colonne'])

            provisions[meilleur_choix['ligne']] -= meilleur_choix['quantite']
            print(provisions)
            commandes[meilleur_choix['colonne']] -= meilleur_choix['quantite']
            print(commandes)

            print(matrice_transport)
    return matrice_transport
