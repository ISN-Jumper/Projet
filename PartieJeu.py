from tkinter import *
from tkinter import font
import random
import time
from timeit import default_timer


def Haut(evt):
    global Wplan
    global Wfusee

    Position = Wplan.coords(Wfusee)
    PosY = Position.pop(1)
    if PosY - 65> 15:  # L'axe des ordonnées est dirigé vers le bas
        Wplan.coords(Wfusee, Position, PosY - 65)
    else:
        Wplan.coords(Wfusee, Position, PosY)

def Bas(evt):
    global Wplan
    global Wfusee

    Position = Wplan.coords(Wfusee)
    PosY = Position.pop(1)
    if PosY +65 < 705:  # L'axe des ordonnées est dirigé vers le bas
        Wplan.coords(Wfusee, Position, PosY + 65)
    else:
        Wplan.coords(Wfusee, Position, PosY)

def Gauche(evt):
    global Wplan
    global Wfusee

    Position = Wplan.coords(Wfusee)
    PosX = Position.pop(0)
    if PosX - 30 > 15:  # L'axe des ordonnées est dirigé vers le bas
        Wplan.coords(Wfusee, PosX - 30, Position)
    else:
        Wplan.coords(Wfusee, PosX, Position)

def Droite(evt):
    global Wplan
    global Wfusee

    Position = Wplan.coords(Wfusee)
    PosX = Position.pop(0)
    if PosX + 30 < 400:  # L'axe des ordonnées est dirigé vers le bas
        Wplan.coords(Wfusee, PosX +30, Position)
    else:
        Wplan.coords(Wfusee, PosX, Position)


def Attaque():
    global AsteroX
    global AsteroY
    global Deltax
    global NumImage
    global mesImages
    global Wplan
    global Wasteroide

    Wplan.delete(Wasteroide)
    Wasteroide = Wplan.create_image(AsteroX, AsteroY, image=mesImages[NumImage])

    NumImage += 1
    AsteroX -= Deltax
    if NumImage==23:
        NumImage=0
        AsteroX=random.randint(750, 1200)
        AsteroY = random.randint(100, 620)
    Wplan.after(600 , Attaque)


def Bouge(Wimage,letemps):
    global Wplan
    Position = Wplan.coords(Wimage)
    PosX = Position.pop(0)
    Wplan.coords(Wimage, PosX - 80, Position)
    time.sleep(1)
    #    if letemps >500:
     #       letemps-=10
  #  Wplan.after(letemps, Attaque)

def chronometre():
    now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    Wplan.itemconfigure(chrono, text=str_time, fill='white', font=Times)
    window.after(1000, chronometre)


window=Tk()
window.title("SPACE JUMPER 3000")

# Faire en sorte que la taille de la fenêtre s'adapte à n'importe quel écran :
largeur_fenetre = window.winfo_screenwidth()
hauteur_fenetre = window.winfo_screenheight()

window.geometry("%dx%d+0+0" % (largeur_fenetre, hauteur_fenetre))
#window.geometry("1280x720+40+50")

#------- Police -------#


Times = font.Font(family='Times', size=18, weight='bold')

Ciel=PhotoImage(file='Ciel.png')
Fusee=PhotoImage(file='fusée2.png')
#Asteroide=PhotoImage(file='C:/Users/remi1/Desktop/SpaceJUMP/Astéroïde.png')

#------------- Graphique accueil --------#

Wplan=Canvas(window, width=largeur_fenetre, height=hauteur_fenetre)
Wplan.grid()
Wplan.create_image(640, 360, image=Ciel)
AffichageChrono = Wplan.create_text(largeur_fenetre//2,hauteur_fenetre//2)
Wfusee=Wplan.create_image(100,360, image=Fusee)

#---Affichage Chrono ---#
start = default_timer()
chrono = Wplan.create_text(40, 20)


mesImages=[]
for i in range(24):
    nom = "img\Astéroïde" + str(i) + ".png"
    mesImages.append(PhotoImage(file=nom))

#---------------#
AsteroX=random.randint(750, 1200)
AsteroY=random.randint(100, 620)
Deltax=50
NumImage=0
temps=2500

Wasteroide=Wplan.create_image(random.randint(750, 1200), random.randint(100, 620))


#----------
Wplan.bind_all('z', Haut)
Wplan.bind_all('s', Bas)
Wplan.bind_all('d', Droite)
Wplan.bind_all('q', Gauche)



chronometre()
Attaque()

window.mainloop()