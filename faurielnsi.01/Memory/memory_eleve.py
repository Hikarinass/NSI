import random as rd
from math import sqrt

def alphabet():
    """
    Retourne la liste des lettres majuscules :
    ce seront les images du jeu
    """
    rep = []
    for i in range(65,91):
        rep.append(chr(i))
    return rep

def choix_image(nb_im, tab):
    """
    Choisis aleatoirement nb_im elements d'un tableau tab
    Melange aussi les images
    """
    rep = []
    liste_ind=[]
    for idx in range(len(tab)):
        liste_ind.append(idx)
    for co in range(nb_im):
        ind_alea = liste_ind.pop(rd.randint(0,len(liste_ind)-1))
        rep.append(tab[ind_alea])
    return rep

def creer_carte(image):
    """
    retourne un dictionnaire correspndant a une carte. Les cles sont :
    - 'image' : str
    - 'dos' : str
    - 'visible' : bool
    - 'joueur' : str
    """
    return {'image' : image, 'dos' : '.', 'visible' : False, 'joueur' : ''}

def creer_paquet(liste_image):
    rep = []
    for image in liste_image:
        rep.append(creer_carte(image))
        rep.append(creer_carte(image))
    return rep

def melange_paquet(paq):
    rd.shuffle(paq)

def plus_gd_pdt(nb):
    rep = 1
    for i in range(2,int(sqrt(nb)) + 1):
        if nb%i == 0:
            rep = i
    return rep, nb//rep

def creer_plateau(paq):
    nb_lig, nb_col = plus_gd_pdt(len(paq))
    tab = []
    idx = 0
    for i in range(nb_lig):
        ligne = []
        for j in range(nb_col):
            ligne.append(paq[idx])
            idx = idx + 1
        tab.append(ligne)
    return tab

def affiche_plateau(plat, triche):
    txt = ""
    for i in range(len(plat)):
        for j in range(len(plat[i])):
            carte = plat[i][j]
            if triche or carte['visible']:
                txt = txt + " {0} ".format(carte['image'])
            elif carte['joueur'] != '':
                txt = txt + " {0} ".format(' ')
            else:
                txt = txt + " {0} ".format(carte['dos'])
        txt = txt + "\n"
    return txt

def tour_de_jeu(plateau, liste_joueur, idx_joueur):
    #print('\n'*50)
    idx_lig = int(input("{0} : choisissez une ligne : ".format(liste_joueur[idx_joueur])))
    idx_col = int(input("{0} : choisissez une colonne : ".format(liste_joueur[idx_joueur])))
    while not(0 <= idx_lig < len(plateau) and 0 <= idx_col < len(plateau[0])) and plateau[idx_lig][idx_col]['trouve']:
        idx_lig = int(input("{0} : choisissez une ligne : ".format(liste_joueur[idx_joueur])))
        idx_col = int(input("{0} : choisissez une colonne : ".format(liste_joueur[idx_joueur])))
    plateau[idx_lig][idx_col]['visible'] = True
    print(affiche_plateau(plateau, False))
    idx_lig2 = int(input("{0} : choisissez une ligne : ".format(liste_joueur[idx_joueur])))
    idx_col2 = int(input("{0} : choisissez une colonne : ".format(liste_joueur[idx_joueur])))
    while not(0 <= idx_lig2 < len(plateau) and 0 <= idx_col2 < len(plateau[0])) and plateau[idx_lig2][idx_col2]['trouve']:
        idx_lig2 = int(input("{0} : choisissez une ligne : ".format(liste_joueur[idx_joueur])))
        idx_col2 = int(input("{0} : choisissez une colonne : ".format(liste_joueur[idx_joueur])))
    plateau[idx_lig2][idx_col2]['visible'] = True
    print(affiche_plateau(plateau, False))
    if plateau[idx_lig][idx_col]['image'] == plateau[idx_lig2][idx_col2]['image']:
        plateau[idx_lig][idx_col]['joueur'] = liste_joueur[idx_joueur]
        plateau[idx_lig2][idx_col2]['joueur'] = liste_joueur[idx_joueur]
        plateau[idx_lig][idx_col]['visible'] = False
        plateau[idx_lig2][idx_col2]['visible'] = False
        return idx_joueur
    else:
        plateau[idx_lig][idx_col]['visible'] = False
        plateau[idx_lig2][idx_col2]['visible'] = False
        return (idx_joueur + 1)%len(liste_joueur)

# Test fonction
alph = alphabet()
print(alph)

nb_im = 10

liste_image = choix_image(nb_im,alph)
print(liste_image)

carte01 = creer_carte(liste_image[0])
print(carte01)

un_paquet = creer_paquet(liste_image)
print(un_paquet)

print()
melange_paquet(un_paquet)
print(un_paquet)

print(plus_gd_pdt(12))
print(plus_gd_pdt(25))

plateau = creer_plateau(un_paquet)
print(plateau)

print(affiche_plateau(plateau,True))
print(affiche_plateau(plateau,False))

liste_joueur = ['Luke', 'Yoda', 'Vador']
idx_joueur = 0

print(affiche_plateau(plateau,False))
idx_joueur = tour_de_jeu(plateau, liste_joueur, idx_joueur)
print(liste_joueur[idx_joueur])
idx_joueur = tour_de_jeu(plateau, liste_joueur, idx_joueur)
print(liste_joueur[idx_joueur])
idx_joueur = tour_de_jeu(plateau, liste_joueur, idx_joueur)
print(liste_joueur[idx_joueur])
