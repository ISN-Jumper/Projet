from tkinter import *
from tkinter import font
import os

def ChangePage():
    os.startfile("PartieJeu.py")
    window.quit()

if __name__ == '__main__':
#pourrr teesssssteeeeeer
    window=Tk()
    window.title("SPACE JUMPER 3000")

    #Faire en sorte que la taille de la fenêtre s'adapte à n'importe quel écran :
    largeur_fenetre = window.winfo_screenwidth()
    hauteur_fenetre = window.winfo_screenheight()

    window.geometry("%dx%d+0+0" % (largeur_fenetre,hauteur_fenetre))
    #window.geometry("1280x720+40+50")

    #------- Police -------#

    Times = font.Font(family='Times', size=16, weight='bold')

    Ciel=PhotoImage(file='CielAccueil.png')

    #------------- Graphique accueil --------#

    Wplan=Canvas(window, width=largeur_fenetre, height=hauteur_fenetre)
    Wplan.grid()
    Wplan.create_image(640, 360, image=Ciel)


    Jouer=Button(window, text='Jouer', width=5, height=1, font =Times, command = lambda : ChangePage())
    Jouer.grid()
    Jouer.place(x=(largeur_fenetre//2), y=(hauteur_fenetre//1.5))

    Wquitter = Button(window, text="Quitter", command=window.quit).grid()

    window.mainloop()