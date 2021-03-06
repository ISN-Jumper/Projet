from tkinter import *
from tkinter import font
import random
import time
from timeit import default_timer
from threading import Thread
import os
from PIL import Image, ImageTk

PremiereCollision = False
DeuxiemeCollision = False
TroisiemeCollision = False
LaCollision = False

PremiereChance = True
DeuxiemeChance = True
TrosiemeChance = True

LeJoueurGagne = True

def Haut(evt):
    global Wplan
    global Wfusee
    global UneFoisTouche
    global DeuxFoisTouche
    global TroisFoisTouche



    PositionFusee = Wplan.coords(Wfusee)
    PosY = PositionFusee.pop(1)
    if PosY - 65> 15:  # L'axe des ordonnées est dirigé vers le bas
        Wplan.coords(Wfusee, PositionFusee, PosY - 65)
    else:
        Wplan.coords(Wfusee, PositionFusee, PosY)

def Bas(evt):
    global Wplan
    global Wfusee
    global UneFoisTouche
    global DeuxFoisTouche
    global TroisFoisTouche


    PositionFusee = Wplan.coords(Wfusee)
    PosY = PositionFusee.pop(1)
    if PosY +65 < 705:  # L'axe des ordonnées est dirigé vers le bas
        Wplan.coords(Wfusee, PositionFusee, PosY + 65)
    else:
        Wplan.coords(Wfusee, PositionFusee, PosY)

def Gauche(evt):
    global Wplan
    global Wfusee

    PositionFusee = Wplan.coords(Wfusee)
    PosX = PositionFusee.pop(0)
    if PosX - 30 > 15:  # L'axe des ordonnées est dirigé vers le bas
        Wplan.coords(Wfusee, PosX - 30, PositionFusee)
    else:
        Wplan.coords(Wfusee, PosX, PositionFusee)

def Droite(evt):
    global Wplan
    global Wfusee

    PositionFusee = Wplan.coords(Wfusee)

    PosX = PositionFusee.pop(0)
    if PosX + 30 < 400:  # L'axe des ordonnées est dirigé vers le bas
        Wplan.coords(Wfusee, PosX +30, PositionFusee)
    else:
        Wplan.coords(Wfusee, PosX, PositionFusee)

def Attaque():
    global AsteroX
    global AsteroY
    global Deltax
    global NumImage
    global mesImages
    global Wplan
    global Wasteroide
    global CoordonneesAsteroide

    Wplan.delete(Wasteroide)
    Wasteroide = Wplan.create_image(AsteroX, AsteroY, image=mesImages[NumImage])

    NumImage += 1
    AsteroX -= Deltax
    if NumImage==23:
        NumImage=0
        AsteroX=random.randint(750, 1200)
        AsteroY = random.randint(100, 620)
    #print(Wplan.coords(Wasteroide))
    #print(CoordonneesAsteroide)
    Wplan.after(500 , Attaque)

class Perso:
    def __init__(self, Cordox, Cordoy, Wplan):
        self.Wplan = Wplan
        self.id = self.Wplan.create_image(Cordox, Cordoy, image=Laser)

    def animation(self):
        self.Wplan.move(self.id, 13, 0)

def Create_laser(event):
    Cordo = Wplan.coords(Wfusee)
    LaserX = Cordo.pop(0) + 87.5
    LaserY = Cordo.pop(0)
    personnage = Perso(LaserX, LaserY, Wplan)
    EnsembleLaser.add(personnage)

def animation_laser():
    for personnage in EnsembleLaser:
        personnage.animation()
        x0 = personnage.id
        if x0 > largeur_fenetre:
            Wplan.delete(personnage.id)
            EnsembleLaser.remove(personnage)
    window.after(3, animation_laser)

def Exit(evt):
    window.attributes('-fullscreen', True)
    Wplan.bind_all('<Escape>', Tixe)
def Tixe(evt):
    window.attributes('-fullscreen', False)
    Wplan.bind_all('<Escape>', Exit)

def Collision():
    global Wasteroide
    global AsteroX
    global Wfusee
    Cordo = Wplan.coords(Wfusee)
    fuseeX = Cordo.pop(0)+76
    contactAsteroide=AsteroX-50

    if fuseeX==contactAsteroide :
        Wplan.delete(Wasteroide)
        Wplan.itemconfig(Barre, image=DeuxCarre)

    Wplan.after(50, Collision)

NombreDeVie = 3

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
EnsembleLaser=set()
window.after(10, animation_laser)
#---------Image-------#

#Ciel=PhotoImage(file='Ciel.png')
Fusee=PhotoImage(file='fusée2.png')
Laser=PhotoImage(file='Laser.png')

#------------- Graphique accueil --------#

Wplan=Canvas(window, width=largeur_fenetre, height=hauteur_fenetre)
Wplan.grid()

WCCiel=Image.open('Ciel.png')
WCCiel = WCCiel.resize((largeur_fenetre, hauteur_fenetre), Image.ANTIALIAS)
Ciel=ImageTk.PhotoImage(WCCiel)
WCiel=Wplan.create_image((largeur_fenetre//2)-2, (hauteur_fenetre//2)-2, image=Ciel)
#Wplan.create_image(640, 360, image=Ciel)

AffichageChrono = Wplan.create_text(largeur_fenetre//2,hauteur_fenetre//2)

Wfusee=Wplan.create_image(100,360, image=Fusee)

Wasteroide=Wplan.create_image(random.randint(750, 1200), random.randint(100, 620))
mesImages=[]
for i in range(24):
    nom = "img\Astéroïde" + str(i) + ".png"
    mesImages.append(PhotoImage(file=nom))


#---Affichage Chrono ---#
start = default_timer()
chrono = Wplan.create_text(40, 20)

#---------------#
PositionAstero = Wplan.coords(Wasteroide)
AsteroX=random.randint(750, 1200)
AsteroY=random.randint(100, 620)
Deltax=50
NumImage=0
temps=2500
#---Coordonnées Astéroïde---#

x1Astero = AsteroX - (0.5*(Wplan.coords(Wasteroide).pop(0))) #Coordonées du coin en Haut à Gauche de la fusée
y1Astero = AsteroY + (0.5*(Wplan.coords(Wasteroide).pop(1))) #Coordonnée du coin en Haut à Gauche de la fusée
x2Astero = AsteroX + (0.5*(Wplan.coords(Wasteroide).pop(0))) #Coordonées du coin en Haut à Gauche de la fusée
y2Astero = AsteroY - (0.5*(Wplan.coords(Wasteroide).pop(1))) #Coordonnée du coin en Haut à Gauche de la fusée

CoordonneesAsteroide = (x1Astero,y1Astero,x2Astero,y2Astero)


#---Coordonées du centre de la Fusée---#
PositionFusee = Wplan.coords(Wfusee)
print("La fusée est à :" ,PositionFusee)
PosFuseeX = PositionFusee.pop(0)
print("La fusée est à :",PosFuseeX)
PosFuseeY = Wplan.coords(Wfusee).pop(1)

"""
x1fusee = Wplan.coords(Wfusee).pop(0) - (0.5 * 152)  # Coordonées du coin en Haut à Gauche de la fusée
y1fusee = Wplan.coords(Wfusee).pop(1) + (0.5 * 100)  # Coordonnée du coin en Haut à Gauche de la fusée
x2fusee = Wplan.coords(Wfusee).pop(0) + (0.5 * 152)  # Coordonnée du coin en Bas à Droite de la fusée
y2fusee = Wplan.coords(Wfusee).pop(1) - (0.5 * 100)  # Coordonnée du coin en Bas à Droite de la fusée
CoordoneesFusee = [x1fusee, y1fusee, x2fusee, y2fusee]  # Coordonées complète de la fusée
print(CoordoneesFusee)
"""

#-----Déplacement fusée -----#
Wplan.bind_all('z', Haut)
Wplan.bind_all('s', Bas)
Wplan.bind_all('d', Droite)
Wplan.bind_all('q', Gauche)

#------Plein écran ----------#
Wplan.bind_all('<Escape>', Exit)

#----Tir laser--------#
window.bind('<space>', Create_laser)

#---Nombre de vies---#
NombresVie = 3

#---Barre de Vie---#
TroisCarre=PhotoImage(file='img/Barre de Progression/3.png')
Barre = Wplan.create_image(largeur_fenetre*0.957, hauteur_fenetre*0.026, image=TroisCarre)
DeuxCarre=PhotoImage(file='img/Barre de Progression/2.png')
UnCarre=PhotoImage(file='img/Barre de Progression/1.png')
GameOver=PhotoImage(file='img/Barre de Progression/Game Over.png')


Collision()
chronometre()
Attaque()


window.mainloop()