def creer_plateau(nb_lig, nb_col):
    rep = []
    for num_lig in range (nb_lig):
        ligne = []
    for num_col in range (nb_col):
        ligne.append(' ')
    rep.append(ligne)

    return rep

un_plateau = creer_plateau(6, 7)
print(un_plateau)

def afficher_plateau(plateau):
    rep = ""
    for num_lig in range (len(plateau)):
        for num_col in range (len(plateau[num_lig])):
            rep=rep+"| "+str(plateau[num_lig][num_col])+" "
        rep=rep+"|\n"
    return rep 

def placer_jeton(plateau, num_col, jeton):
    plateau[0][num_col] = jeton

un_plateau = creer_plateau(6, 7)
print(afficher_plateau(un_plateau))
placer_jeton(un_plateau, "jaune", 'bleu')
print(afficher_plateau(un_plateau))

text_rep=afficher_plateau(un_plateau)
print(text_rep)
