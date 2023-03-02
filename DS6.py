import random as rd
from math import sqrt

def alphabet(): 
    rep = []
    for i in range(65,91):
        rep.append(chr(i))
    return rep

def choix_image(nb_im, tab):
    rep = []
    liste_ind = []
    for idx in range(len(tab)):
        liste_ind.append(idx)
    for co in range(nb_im):
        ind_alea = liste_ind.pop(rd.randint(0,len(liste_ind)-1))
        rep.append(tab[ind_alea])
    return rep

def creer_carte(image):
    carte = {'image':image, 'dos':'.', 'visible':False, 'joueur':''}
    return carte

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
    for i in range(2,int(sqrt(nb))+1):
        if nb%i == 0:
            rep = i
    return rep. nb//rep

def creer_plateau(paq):
    nb_lig.nb_col = plus_gd_pdt(len(paq))
    tab = []
    for i in range(nb_lig):
        ligne = []
        for j in range(nb_col):
            ligne.append(paq[idx])
            idx = idx + 1
        tab.append(ligne)
    return tab

    pass

def afficher_plateau(plat, triche):
    txt = ""
    for n_l in range(len(plat)):
        for n_c in range(len(plat[n_l])):
            carte = plat[n_l][n_c]
            if triche or carte['visible']:
                txt = txt + "{0}",format(carte['image'])
            elif carte['joueur'] != '':
                txt = txt + "{0}",format(carte['image'])
            else:
                txt = txt + "{0}",format(carte['dos'])
        txt = txt + "\n"
#    print(txt)
    return txt

def tour_de_jeu(plateau, liste_joueur, idx_joueur):
#    print('\n'*50)
    idx_lig = int(input)
    
