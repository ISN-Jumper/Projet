from tkinter import *
from tkinter import font
import os

def ChangePage():
    os.startfile("C:/Users/remi1/PycharmProjects/SpaceJumper3000/PartieJeu.py")
    window.quit()

if __name__ == '__main__':

    window=Tk()
    window.title("SPACE JUMPER 3000")
    window.geometry("1280x720+40+50")

    #------- Police -------#

    Times = font.Font(family='Times', size=16, weight='bold')

    Ciel=PhotoImage(file='C:/Users/remi1/Desktop/SpaceJUMP/Ciel.png')

    #------------- Graphique accueil --------#

    Wplan=Canvas(window, width=1280, height=720)
    Wplan.grid()
    Wplan.create_image(640, 360, image=Ciel)

#hjklmhjkl

    Jouer=Button(window, text='Jouer', width=5, height=1, font =Times, command = lambda : ChangePage())
    Jouer.grid()
    Jouer.place(x=400, y=560)

    window.mainloop()