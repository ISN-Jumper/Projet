from tkinter import *
from tkinter import font
import os

def ChangePage():
    os.startfile("Accueil.py")
    window.quit()

window = Tk()
window.title("SPACE JUMPER 3000")

# Faire en sorte que la taille de la fenêtre s'adapte à n'importe quel écran :
largeur_fenetre = window.winfo_screenwidth()
hauteur_fenetre = window.winfo_screenheight()

window.geometry("%dx%d+0+0" % (largeur_fenetre, hauteur_fenetre))
window.attributes('-fullscreen', True)

# ------- Police -------#

Times = font.Font(family='Times', size=16, weight='bold')

Ciel = PhotoImage(file='Ciel.png')
GameOver = PhotoImage(file='img/Barre de Progression/Game Over.png')

# ------------- Graphique accueil --------#

Wplan = Canvas(window, width=largeur_fenetre, height=hauteur_fenetre)
Wplan.grid()
Wplan.create_image(640, 360, image=Ciel)
Wplan.create_image((largeur_fenetre//2),(hauteur_fenetre//2),image=GameOver)

Jouer = Button(window, text='Rejouer', width=5, height=1, font=Times, command=lambda: ChangePage())
Jouer.grid()
Jouer.place(x=(largeur_fenetre // 2.1), y=(hauteur_fenetre // 1.75))

Wquitter = Button(window, text="Quitter", command=window.quit).grid()

window.mainloop()