#Sauvegarde
# ["Luke", "Yoda", "Vador"]

L = ['Luck', 'Yoda', 'Vador']
txt = ""
for idx in range(len(L)):
    txt = txt + str(L[idx]) + ";"
txt = txt[0:len(txt)-1]
print(txt)
file = open("./sauvegarde.txt","w",encoding="utf-8")
file.write(txt)
file.close()