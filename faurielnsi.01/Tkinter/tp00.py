import tkinter as tk
import random as rd

def chge_color_alea():
    ind_alea = rd.randint(0,len(liste_couleur)-1)
    color_alea = liste_couleur[ind_alea]
    fen_p['background'] = color_alea
    lbl_bjr["bg"] = color_alea

fen_p = tk . Tk ()

fen_p . title ('titre')
fen_p . geometry ("800x600+100+250")
bg_color = '#{0:02x}{1:02x}{2:02x}'.format (36 ,212 ,16) 
fen_p['background'] = bg_color

liste_couleur = ["black","green","red","purple","blue","yellow","pink"]

bout_quitter = tk.Button(fen_p, text = 'Quitter', command = fen_p.destroy)
bout_quitter.grid(row = 4, column = 0)
bout_color = tk.Button(fen_p, text = 'Changer la couleur', command = chge_color_alea)
bout_color.grid(row = 2, column = 0)

lbl_bjr = tk.Label(fen_p, text = "Bonjour",background = bg_color)
lbl_bjr.grid(row = 1, column = 0)

can01 = tk.Canvas(fen_p,width=800,height=400, background = 'ivory')
can01.grid(row = 3, column = 0, columnspan = 2)
can01.create_rectangle(100,150,200,300, fill = "purple", outline="blue")
can01.create_oval(300,150,400,250,fill="red")



tk . mainloop()

