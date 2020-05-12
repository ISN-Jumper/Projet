from tkinter import *
from tkinter import font
import random
from timeit import default_timer
import os
from PIL import Image, ImageTk
import time
from threading import *
from pygame import mixer

LaCollision = False
EcranTraverse = False
LaCollisionLaser = False

PremiereCollision = False
DeuxiemeCollision = False
TroisiemeCollision = False

mixer.init()
mixer.music.load("DuaLipa.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.2)


def Haut(evt):
    global Wplan
    global Wfusee
    PositionFusee = Wplan.coords(Wfusee)
    PosY = PositionFusee.pop(1)
    if PosY -65 > 35:  # L'axe des ordonnées est dirigé vers le bas
        Wplan.coords(Wfusee, PositionFusee, PosY - 65)
    else:
        Wplan.coords(Wfusee, PositionFusee, PosY)

def Bas(evt):
    global Wplan
    global Wfusee
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

def Exit(evt):
    window.attributes('-fullscreen', True)
    Wplan.bind_all('<Escape>', Tixe)
def Tixe(evt):
    window.attributes('-fullscreen', False)
    Wplan.bind_all('<Escape>', Exit)


class Perso:
    def __init__(self, Cordox, Cordoy, Wplan):
        self.Wplan = Wplan
        self.id = self.Wplan.create_image(Cordox, Cordoy, image=Laser)

    def animation(self):
        global listAstero, Astero, NumImage
        global NbrePoints
        global Wplan
        global NbreTentative

        Wlaser = self.id

        self.Wplan.move(self.id, 6, 0)


NbreTentative = 0


def Create_laser(event):
    global personnage
    Cordo = Wplan.coords(Wfusee)
    LaserX = Cordo.pop(0) + 87.5 + 10
    LaserY = Cordo.pop(0)
    personnage = Perso(LaserX, LaserY, Wplan)
    EnsembleLaser.add(personnage)
    Bruitage = mixer.Sound("BruitageLaserWav.wav")
    Bruitage.set_volume(0.05)
    Bruitage.play()


def animation_laser():
    global NbreTentative
    global Astero
    global NumImage
    global listAstero, listAsteroX, listAsteroY
    global NbrePoints

    for personnage in EnsembleLaser:
        personnage.animation()
        x0 = personnage.id
        if x0 > largeur_fenetre - 1:
            Wplan.delete(personnage.id)
            EnsembleLaser.remove(personnage)

        for Astero in listAstero:
            if (Wplan.coords(personnage.id)[0]) + 20 >= (Wplan.coords(Astero)[0]) - 50 and (
            Wplan.coords(personnage.id)[0]) - 20 <= (Wplan.coords(Astero)[0]) + 50:
                if (Wplan.coords(personnage.id)[1]) + 1.75 >= (Wplan.coords(Astero)[1]) - 50 > (Wplan.coords(personnage.id)[1]) - 1.75 or (Wplan.coords(personnage.id)[1]) - 1.75 <= (Wplan.coords(Astero)[1]) + 50 < (Wplan.coords(personnage.id)[1]) + 1.75 or (Wplan.coords(Astero)[1]) + 50 >= (Wplan.coords(personnage.id)[1]) + 1.75 > (Wplan.coords(personnage.id)[1]) - 1.75 >= (Wplan.coords(Astero)[1]) - 50:
                    Wplan.itemconfig(personnage.id, image=Invisible)
                    Wplan.coords(personnage.id, largeur_fenetre - 10, Wplan.coords(personnage.id)[1])
                    Explosion = mixer.Sound("BruitageCraquement.wav")
                    Explosion.set_volume(0.5)
                    Explosion.play()
                    NbreTentative += 1
                    print(NbreTentative)
                if NbreTentative == 3:
                    AsteroideDetruit = mixer.Sound("AsteroideDetruit.wav")
                    AsteroideDetruit.set_volume(0.5)
                    AsteroideDetruit.play()
                    Wplan.delete(Astero)
                    idastero = listAstero.index(Astero)
                    listAstero.pop(idastero)
                    listAsteroX.pop(idastero)
                    listAsteroY.pop(idastero)
                    NbreTentative = 0
                    NbrePoints += 1
                    Wplan.itemconfig(CanvasPoints, text=('Nombre de Points :', NbrePoints))
    window.after(3, animation_laser)


def chronometre():
    now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    Wplan.itemconfigure(chrono, text=str_time, fill='white', font=Times)
    window.after(1000, chronometre)


class Collision(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        global NombreDeVie
        global LaCollision
        global Wplan
        global AsteroY
        global AsteroX
        global listAsteroX
        global listAsteroY
        global listNumImage
        global Astero
        global listAstero

        for i in range(3):
            time.sleep(1)
            while LaCollision == False:
                x1fusee = Wplan.coords(Wfusee).pop(0) - (0.5 * 152)  # Coordonées du coin en Haut à Gauche de la fusée
                y1fusee = Wplan.coords(Wfusee).pop(1) + (0.5 * 100)  # Coordonnée du coin en Haut à Gauche de la fusée
                x2fusee = Wplan.coords(Wfusee).pop(0) + (0.5 * 152)  # Coordonnée du coin en Bas à Droite de la fusée
                y2fusee = Wplan.coords(Wfusee).pop(1) - (0.5 * 100)  # Coordonnée du coin en Bas à Droite de la fusée
                CoordoneesFusee = [x1fusee, y1fusee, x2fusee, y2fusee]  # Coordonées complète de la fusée

                if len(Wplan.find_overlapping(CoordoneesFusee[0], CoordoneesFusee[1], CoordoneesFusee[2],
                                              CoordoneesFusee[3])) == 3:
                    print("!!!!!!!!!COLLISION11111!!!!!!!!!!")
                    NombreDeVie -= 0.5
                    LaCollision = True
                    print(LaCollision)
            while LaCollision == True:
                if len(Wplan.find_overlapping(CoordoneesFusee[0], CoordoneesFusee[1], CoordoneesFusee[2],
                                              CoordoneesFusee[3])) == 3:
                    print("!!!!!!!!!COLLISION11111!!!!!!!!!!")
                    NombreDeVie -= 0.5
                    LaCollision = False
                    AsteroX = random.randint(750, 1200)
                    AsteroY = random.randint(100, 620)
                    print(LaCollision)
                if NombreDeVie == 2 and LaCollision == False:
                    Wplan.itemconfig(Barre, image=DeuxCarre)
                if NombreDeVie == 1 and LaCollision == False:
                    Wplan.itemconfig(Barre, image=UnCarre)
                if NombreDeVie == 0 and LaCollision == False:
                    Wplan.itemconfig(Barre, image=GameOver)
                if NombreDeVie == 0:
                    os.startfile("GameOverPage.py")
                    window.quit()

NombreDeVie = 3

class GenererAstero(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        global Passe
        global mesImages
        global EcranTraverse
        global listAsteroX
        global listAsteroY
        global listNumImage
        global Astero
        global listAstero
        global personnage
        global Wplan
        global NbrePoints
        global RandomX
        global RandomY
        startTime = time.time()

        while Vivant:
            actualTime = time.time()
            if actualTime >= startTime + 2:
                listAsteroX.append(random.randint(750, 1200))
                listAsteroY.append(random.randint(100, 620))
                listNumImage.append(0)
                startTime = actualTime
            listAstero = []
            for i in range(len(listAsteroX)):
                Astero = Wplan.create_image(listAsteroX[i], listAsteroY[i], image=mesImages[listNumImage[i]])
                listAstero.append(Astero)
                listAsteroX[i] -= Deltax
                if listNumImage[i] == 23:
                    listAsteroX[i] = random.randint(750, 1200)
                    listAsteroY[i] = random.randint(100, 620)
                    listNumImage[i] = 0
            time.sleep(0.5)
            for Astero in listAstero:
                Wplan.delete(Astero)


window = Tk()
window.title("SPACE JUMPER 3000")


# Faire en sorte que la taille de la fenêtre s'adapte à n'importe quel écran :
largeur_fenetre = window.winfo_screenwidth()
hauteur_fenetre = window.winfo_screenheight()

window.geometry("%dx%d+0+0" % (largeur_fenetre, hauteur_fenetre))
window.attributes('-fullscreen', True)

#------- Police -------#

Times = font.Font(family='Times', size=18, weight='bold')

EnsembleLaser=set()
EnsembleAsteroide=set()
Temps_Generer=5000

window.after(10, animation_laser)
#window.after(10, animation_asteroide)
#---------Image-------#

Fusee=PhotoImage(file='Fusées/Fusee0.png')
Laser=PhotoImage(file='Laser.png')
Invisible=PhotoImage(file='invisible.png')

#---Test---#
personnage =""
#------------- Graphique accueil --------#

Wplan=Canvas(window, width=largeur_fenetre, height=hauteur_fenetre)
Wplan.grid()

WCCiel=Image.open('Ciel.png')
WCCiel = WCCiel.resize((largeur_fenetre, hauteur_fenetre), Image.ANTIALIAS)
Ciel=ImageTk.PhotoImage(WCCiel)
WCiel=Wplan.create_image((largeur_fenetre//2)-2, (hauteur_fenetre//2)-2, image=Ciel)

AffichageChrono = Wplan.create_text(largeur_fenetre//2,hauteur_fenetre//2)

Wfusee=Wplan.create_image(100,360, image=Fusee)

Wasteroide=Wplan.create_image(random.randint(750, 1200), random.randint(100, 620))
Astero = Wplan.create_image(random.randint(750, 1200), random.randint(100, 620))

mesImages=[]
for i in range(24):
    nom = "img\Astéroïde" + str(i) + ".png"
    mesImages.append(PhotoImage(file=nom))


#---Affichage Chrono ---#
start = default_timer()
chrono = Wplan.create_text(40, 20)

#---------------#

AsteroX=random.randint(750, 1200)
AsteroY=random.randint(100, 620)
Deltax=50
NumImage=0
temps=2500
"""
AsteroX=random.randint(750, 1200)
AsteroY=random.randint(100, 620)
Deltax=50
NumImage=0
temps=2500
"""
#--- Données importantes pour Astéroïdes qu'on va générer---#
listAstero = []
listAsteroX = [random.randint(750, 1200)]
listAsteroY = [random.randint(100, 620)]
listNumImage = [0]


#--Nombres de Points---#
NbrePoints = 0
CanvasPoints = Wplan.create_text(largeur_fenetre/2, 20, text=('Nombre de Points :', NbrePoints), fill='white', font=Times)

#-----Déplacement fusée -----#
Wplan.bind_all('z', Haut)
Wplan.bind_all('s', Bas)
Wplan.bind_all('d', Droite)
Wplan.bind_all('q', Gauche)

#------Plein écran ----------#
Wplan.bind_all('<Escape>', Exit)

#----Tir laser--------#
window.bind('<space>', Create_laser)


#---Barre de Vie---#
TroisCarre=PhotoImage(file='img/Barre de Progression/3.png')
Barre = Wplan.create_image(largeur_fenetre*0.957, hauteur_fenetre*0.026, image=TroisCarre)
DeuxCarre=PhotoImage(file='img/Barre de Progression/2.png')
UnCarre=PhotoImage(file='img/Barre de Progression/1.png')
GameOver=PhotoImage(file='img/Barre de Progression/Game Over.png')

#---MusiqueDeFond---#
Vivant=True
Passe=True


#CollisionLaserAstero()
Collision()
chronometre()
#Attaque()
GenererAstero()
#Create_asteroide()
#aeiouy()

window.mainloop()