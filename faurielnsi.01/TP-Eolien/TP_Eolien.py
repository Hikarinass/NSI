
import csv

def tableFrance(adr):
    listeDico=[]
    f_CSV = open(adr,"r",encoding="utf-8",newline='')
    objCSV=csv.DictReader(f_CSV,delimiter=";") #C'est un objet itérable. 
    #On peut l'utiliser dans une boucle for
    #ATTENTION : Ce n'est ni une liste, ni un dictionnaire!
    for ligne in objCSV:
        listeDico.append(dict(ligne)) #transformer ce contenu en 
        #dictionnaire et l'ajouter à la liste
    f_CSV.close() #Fermer le fichier après l'utilisation de objCSV
    return listeDico

adr="./contours-geographiques-des-communes-2019_COURT.csv"
tableFrancedico=tableFrance(adr)

#def largeurMaxColonne(table,nomCol):
#    maxTemp=len(nomCol)
#    for ligne in table:
#        if ligne[nomCol]!=None:
#            if len(ligne[nomCol])>maxTemp:
#                maxTemp=len(ligne[nomCol])
#    return maxTemp
#
#def afficherTable(table):
#    if table!=[]:
#        listeEnTete=[]
#        for k in table[0]:
#            listeEnTete.append(k)
#        listeTailleCol=[largeurMaxColonne(table,k) for k in table[0]]
#        enTete="|"
#        ligne="|"
#        largeurTable=1
#        for taille in listeTailleCol:
#            enTete+=" {:^"+str(taille)+"} |"
#            ligne+=" {:^"+str(taille)+"} |"
#            largeurTable+=3+taille
#        tt=enTete.format(*listeEnTete)
#        tt+="\n"+"-"*largeurTable+"\n"
#        for i in range(0,len(table)):
#            liste=[v for k,v in table[i].items()]
#            while None in liste:
#                pos=liste.index(None)
#                liste[pos]=""
#            tt+=ligne.format(*liste)+"\n"
#        return tt
#
#print(afficherTable(tableFrancedico))

def tableColonne(table,enTeteCol):
    tableRep=[]
    if enTeteCol in enTete(table):
        for ligne in table:
            dictTemp={enTeteCol : ligne[enTeteCol] }
            tableRep.append(dictTemp)
    return tableRep

print(tableFrancedico)