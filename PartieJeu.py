from tkinter import *
from tkinter import font
import random
import time


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
    global AsteroX1
    global AsteroY1
    global AsteroX2
    global AsteroY2
    global Deltax
    global NumImage
    global mesImages
    global Wplan
    global Wasteroide
    global Wasteroide1
    global Wasteroide2

    Wplan.delete(Wasteroide)
    Wplan.delete(Wasteroide1)
    Wplan.delete(Wasteroide2)

    Wasteroide = Wplan.create_image(AsteroX, AsteroY, image=mesImages[NumImage])
    Wasteroide1 = Wplan.create_image(AsteroX1, AsteroY1, image=mesImages[NumImage])
    Wasteroide2 = Wplan.create_image(AsteroX2, AsteroY2, image=mesImages[NumImage])

    NumImage += 1
    AsteroX -= Deltax
    AsteroX1-=Deltax
    AsteroX2-=Deltax

    if NumImage==23:
        NumImage=0
        AsteroX=random.randint(750, 1200)
        AsteroY = random.randint(100, 620)
        AsteroX1 = random.randint(750, 1200)
        AsteroY1 = random.randint(100, 620)
        AsteroX2 = random.randint(750, 1200)
        AsteroY2 = random.randint(100, 620)
    Wplan.after(600 , Attaque)


window=Tk()
window.title("SPACE JUMPER 3000")
window.geometry("1280x720+40+50")


#------- Police -------#

Times = font.Font(family='Times', size=16, weight='bold')

Ciel=PhotoImage(file='C:/Users/remi1/Desktop/SpaceJUMP/Ciel.png')
Fusee=PhotoImage(file='C:/Users/remi1/Desktop/SpaceJUMP/fusée2.png')
#Asteroide=PhotoImage(file='C:/Users/remi1/Desktop/SpaceJUMP/Astéroïde.png')

#------------- Graphique accueil --------#

Wplan=Canvas(window, width=1280, height=720)
Wplan.grid()
Wplan.create_image(640, 360, image=Ciel)
Wfusee=Wplan.create_image(100,360, image=Fusee)

mesImages=[]
for i in range(24):
    nom = "C:/Users/remi1/Desktop/SpaceJUMP/img/Astéroïde" + str(i) + ".png"
    mesImages.append(PhotoImage(file=nom))

#---------------#

AsteroX=random.randint(750, 1200)
AsteroY=random.randint(100, 620)
AsteroX1=random.randint(750, 1200)
AsteroY1=random.randint(100, 620)
AsteroX2=random.randint(750, 1200)
AsteroY2=random.randint(100, 620)

Deltax=50
NumImage=0
temps=2500

Wasteroide=Wplan.create_image(random.randint(750, 1200), random.randint(100, 620))
Wasteroide1=Wplan.create_image(random.randint(750, 1200), random.randint(100, 620))
Wasteroide2=Wplan.create_image(random.randint(750, 1200), random.randint(100, 620))

#----------
Wplan.bind_all('z', Haut)
Wplan.bind_all('s', Bas)
Wplan.bind_all('d', Droite)
Wplan.bind_all('q', Gauche)

Attaque()

#JOEKPFOJGNREIGNEPOFJKEJFOZE

while True:
    window.update_idletasks()
    window.update()
    time.sleep(0.01)



