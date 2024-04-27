from lecture_fichier import lecture_fichier

def calcul_penalites(matrice, nbr_P, nbr_C):
    penalites_lignes = []
    penalites_colonnes = []
    for i in range(nbr_P):
        couts_ligne = sorted([int(matrice[i][j]) for j in range(nbr_C)])
        penalite_ligne = couts_ligne[1] - couts_ligne[0] if len(couts_ligne) > 1 else 0
        penalites_lignes.append(penalite_ligne)
    for j in range(nbr_C):
        couts_colonne = sorted([int(matrice[i][j]) for i in range(nbr_P)])
        penalite_colonne = couts_colonne[1] - couts_colonne[0] if len(couts_colonne) > 1 else 0
        penalites_colonnes.append(penalite_colonne)

    return penalites_lignes, penalites_colonnes


def trouver_penalite_maximale(penalites_lignes, penalites_colonnes):
    max_penalite_ligne = max(penalites_lignes)
    max_penalite_colonne = max(penalites_colonnes)
    max_penalite_globale = max(max_penalite_ligne, max_penalite_colonne)

    indices_max_ligne = [i for i, x in enumerate(penalites_lignes) if x == max_penalite_globale]
    indices_max_colonne = [j for j, x in enumerate(penalites_colonnes) if x == max_penalite_globale]

    return indices_max_ligne, indices_max_colonne

def choisir_case(matrice, indices_max_ligne, indices_max_colonne, provisions, commandes):
    candidats = []  # Liste pour stocker les cases candidates

    # Chercher la case à coût minimum pour chaque ligne à pénalité maximale
    for i in indices_max_ligne:
        cout_minimum_ligne = 1000
        case_choisie_ligne = None
        for j in range(len(matrice[0])):
            cout_actuel = int(matrice[i][j])
            if cout_actuel < cout_minimum_ligne:
                cout_minimum_ligne = cout_actuel
                case_choisie_ligne = {'ligne': i, 'colonne': j, 'cout': cout_actuel, 'quantite': min(provisions[i], commandes[j])}
        if case_choisie_ligne:
            candidats.append(case_choisie_ligne)

    # Chercher la case à coût minimum pour chaque colonne à pénalité maximale
    for j in indices_max_colonne:
        cout_minimum_colonne = 1000
        case_choisie_colonne = None
        for i in range(len(matrice)):
            cout_actuel = int(matrice[i][j])
            if cout_actuel < cout_minimum_colonne:
                cout_minimum_colonne = cout_actuel
                case_choisie_colonne = {'ligne': i, 'colonne': j, 'cout': cout_actuel, 'quantite': min(provisions[i], commandes[j])}
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
