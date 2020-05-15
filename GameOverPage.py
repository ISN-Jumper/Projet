from tkinter import *
from tkinter import font
import os
import csv

def ChangePage():
    os.startfile("PartieJeu.py")
    window.quit()

window = Tk()
window.title("SPACE JUMPER 3000")

# Faire en sorte que la taille de la fenêtre s'adapte à n'importe quel écran :
largeur_fenetre = window.winfo_screenwidth()
hauteur_fenetre = window.winfo_screenheight()

window.geometry("%dx%d+0+0" % (largeur_fenetre, hauteur_fenetre))
window.attributes('-fullscreen', True)

#---Gestion Meilleur Score ---#
with open("CSV_Score.csv", "r") as ScoreCSV:
    meilleur_score = eval(ScoreCSV.read())

# ------- Police -------#

Times = font.Font(family='Times', size=16, weight='bold')

Ciel = PhotoImage(file='Ciel.png')
GameOver = PhotoImage(file='img/Barre de Progression/Game Over.png')

# ------------- Graphique accueil --------#

Wplan = Canvas(window, width=largeur_fenetre, height=hauteur_fenetre)
Wplan.grid()
Wplan.create_image(640, 360, image=Ciel)
Wplan.create_image((largeur_fenetre//2),(hauteur_fenetre//2),image=GameOver)

#---Frame Score---#
FrameScore = Frame(window, relief='flat')
FrameScore.place(x=360, y=100)

WScore = Label(window, text='Meilleur Score : ', font=Times)
WScore.grid(row=1, column=0)


#---Frame Boutons---#
FrameButtons = Frame(window, relief='flat')
FrameButtons.place(x=(largeur_fenetre//2.25), y=(hauteur_fenetre//1.85))

Jouer = Button(FrameButtons, text='Rejouer', width=5, height=1, font=Times, command=lambda: ChangePage())
Jouer.grid(row=1,column=0)

Wquitter = Button(FrameButtons, text="Quitter", font=Times, command=window.quit)
Wquitter.grid(row=1,column=1)

window.mainloop()