from tkinter import *
from tkinter import font
import random
from timeit import default_timer
import os
from PIL import Image, ImageTk
import time
from threading import *
from pygame import mixer
import csv


Nb_Collision = 0
JeuTermine = False

<<<<<<< HEAD
LaCollision = False
Nb_Collision = 0
EcranTraverse = False
LaCollisionLaser = False
=======
>>>>>>> b74c7aee8529bbd3f5af513e079b646fd53156d4

PremiereCollision = False
DeuxiemeCollision = False
TroisiemeCollision = False

mixer.init()
mixer.music.load("DuaLipa.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.2)


# Generate timing
generateTime = time.time()
refreshTime = time.time()
laserTime = time.time()

# New Laser
new_Laser = False


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
    if PosX - 30 > 100:  # L'axe des ordonnées est dirigé vers le bas
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
        global NbrePoints
        global Wplan
        global NbreTentative

        self.Wplan.move(self.id, 6, 0)


NbreTentative = 0


def Create_laser(event):
    global personnage, new_Laser
    new_Laser = True
<<<<<<< HEAD



def animation_laser():
=======
    MusiqueLaser = mixer.Sound("BruitageLaserWav.wav")
    MusiqueLaser.set_volume(0.1)
    MusiqueLaser.play()




def animation_collsion_laser():
>>>>>>> b74c7aee8529bbd3f5af513e079b646fd53156d4
    global NbreTentative
    global NumImage
    global NbrePoints
    global laserTime, new_Laser
    actualTime = time.time()
<<<<<<< HEAD
=======

>>>>>>> b74c7aee8529bbd3f5af513e079b646fd53156d4
    if actualTime >= laserTime +.003:
        laserTime = actualTime

        if new_Laser:
            Cordo = Wplan.coords(Wfusee)
            LaserX = Cordo.pop(0) + 87.5 + 10
            LaserY = Cordo.pop(0)
            personnage = Perso(LaserX, LaserY, Wplan)
            EnsembleLaser.append(personnage)
            Bruitage = mixer.Sound("BruitageLaserWav.wav")
<<<<<<< HEAD
            Bruitage.set_volume(0.05)
=======
            Bruitage.set_volume(0.1)
>>>>>>> b74c7aee8529bbd3f5af513e079b646fd53156d4
            Bruitage.play()
            new_Laser = False

        toPopPerso = []
        for personnage in EnsembleLaser:
            personnage.animation()
            x0 = personnage.id
            x0 = Wplan.coords(personnage.id)[0]
            if x0 > largeur_fenetre - 1:
                toPopPerso.append(personnage)

            toPopAstero = []
            for Astero in dicoAstero:
                if (Wplan.coords(personnage.id)[0]) + 20 >= (Wplan.coords(Astero)[0]) - 50 and (
                Wplan.coords(personnage.id)[0]) - 20 <= (Wplan.coords(Astero)[0]) + 50:
                    if (Wplan.coords(personnage.id)[1]) + 1.75 >= (Wplan.coords(Astero)[1]) - 50 > (Wplan.coords(personnage.id)[1]) - 1.75 or (Wplan.coords(personnage.id)[1]) - 1.75 <= (Wplan.coords(Astero)[1]) + 50 < (Wplan.coords(personnage.id)[1]) + 1.75 or (Wplan.coords(Astero)[1]) + 50 >= (Wplan.coords(personnage.id)[1]) + 1.75 > (Wplan.coords(personnage.id)[1]) - 1.75 >= (Wplan.coords(Astero)[1]) - 50:
<<<<<<< HEAD
                        Wplan.itemconfig(personnage.id, image=Invisible)
                        # Wplan.coords(personnage.id, largeur_fenetre - 10, Wplan.coords(personnage.id)[1])
                        Explosion = mixer.Sound("BruitageCraquement.wav")
                        Explosion.set_volume(0.5)
                        Explosion.play()
                        NbreTentative += 1
                        # print(NbreTentative)


                    if NbreTentative == 3:
                        AsteroideDetruit = mixer.Sound("AsteroideDetruit.wav")
                        AsteroideDetruit.set_volume(0.5)
                        AsteroideDetruit.play()

                        toPopAstero.append(Astero)
                        NbreTentative = 0
                        NbrePoints += 1
                        Wplan.itemconfig(CanvasPoints, text=('Nombre de Points :', NbrePoints))
            for Astero in toPopAstero:
                print(toPopAstero)
=======
                        # Wplan.coords(personnage.id, largeur_fenetre - 10, Wplan.coords(personnage.id)[1])
                        Explosion = mixer.Sound("BruitageCraquement.wav")
                        Explosion.set_volume(0.1)
                        Explosion.play()
                        NbreTentative += 1
                        Wplan.itemconfig(personnage.id, image=Invisible)
                        Wplan.coords(personnage.id, largeur_fenetre - 10, Wplan.coords(personnage.id)[1])
                        print("NbreTentative",NbreTentative)
                        if NbreTentative >= 3:
                            AsteroideDetruit = mixer.Sound("AsteroideDetruit.wav")
                            AsteroideDetruit.set_volume(0.1)
                            AsteroideDetruit.play()
                            Wplan.itemconfig(personnage.id, image=Invisible)
                            Wplan.coords(personnage.id, largeur_fenetre - 10, Wplan.coords(personnage.id)[1])
                            toPopAstero.append(Astero)
                            NbreTentative = 0
                            NbrePoints += 1
                            listeScore.append(NbrePoints)
                            Wplan.itemconfig(CanvasPoints, text=('Nombre de Points :', NbrePoints))
            for Astero in toPopAstero:
>>>>>>> b74c7aee8529bbd3f5af513e079b646fd53156d4
                Wplan.delete(Astero)
                dicoAstero.pop(Astero)
        for personnage in toPopPerso:
            Wplan.delete(personnage.id)
            EnsembleLaser.remove(personnage)


def chronometre():
    now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    Wplan.itemconfigure(chrono, text=str_time, fill='white', font=Times)
    window.after(1000, chronometre)


class Principale(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        global NombreDeVie
<<<<<<< HEAD
        global LaCollision
        global Wplan
=======
        global Wplan
        global Wfusee, Astero, dicoAstero
        global DetectionCollision
>>>>>>> b74c7aee8529bbd3f5af513e079b646fd53156d4

        Vivant = True
        while Vivant:
            GenererAstero()
<<<<<<< HEAD
            animation_laser()
            if LaCollision == False:
                x1fusee = Wplan.coords(Wfusee).pop(0) - (0.5 * 152)  # Coordonées du coin en Haut à Gauche de la fusée
                y1fusee = Wplan.coords(Wfusee).pop(1) + (0.5 * 100)  # Coordonnée du coin en Haut à Gauche de la fusée
                x2fusee = Wplan.coords(Wfusee).pop(0) + (0.5 * 152)  # Coordonnée du coin en Bas à Droite de la fusée
                y2fusee = Wplan.coords(Wfusee).pop(1) - (0.5 * 100)  # Coordonnée du coin en Bas à Droite de la fusée
                CoordoneesFusee = [x1fusee, y1fusee, x2fusee, y2fusee]  # Coordonées complète de la fusée

                if len(Wplan.find_overlapping(CoordoneesFusee[0], CoordoneesFusee[1], CoordoneesFusee[2],
                                              CoordoneesFusee[3])) == 3:
                    print("!!!!!!!!!COLLISION11111!!!!!!!!!!")
                    NombreDeVie -= 1
                    LaCollision = True
                    print(LaCollision)

            if LaCollision == True and len(Wplan.find_overlapping(CoordoneesFusee[0], CoordoneesFusee[1], CoordoneesFusee[2],
                                          CoordoneesFusee[3])) == 3:
                print("!!!!!!!!!COLLISION11111!!!!!!!!!!")
                NombreDeVie -= 0.5
                LaCollision = False
                print(LaCollision)
            if NombreDeVie == 2 and LaCollision == False:
                Wplan.itemconfig(Barre, image=DeuxCarre)
            elif NombreDeVie == 1 and LaCollision == False:
                Wplan.itemconfig(Barre, image=UnCarre)
            elif NombreDeVie == 0 and LaCollision == False:
                Wplan.itemconfig(Barre, image=GameOver)
            elif NombreDeVie == 0:
                # os.startfile("GameOverPage.py")
                Vivant = False
                window.quit()

NombreDeVie = 3

=======
            animation_collsion_laser()
            DetectionCollision()
            SuppressionAstero()
        time.sleep(1)


>>>>>>> b74c7aee8529bbd3f5af513e079b646fd53156d4
def GenererAstero():
    global mesImages
    global Wplan
    global generateTime, refreshTime
<<<<<<< HEAD
    if Vivant:
        actualTime = time.time()
        if actualTime >= generateTime + 2:
            generateTime = actualTime
            AsteroX = random.randint(750, 1200)
            AsteroY = random.randint(100, 620)
            Astero = Wplan.create_image(AsteroX, AsteroY, image=mesImages[0])
            dicoAstero[Astero] = [AsteroX, AsteroY, 0]
        if actualTime >= refreshTime +.5:
=======


    if Vivant:
        actualTime = time.time()
        if actualTime >= generateTime + 1:
            generateTime = actualTime
            AsteroX = random.randint(800, 1200)
            AsteroY = random.randint(100, 620)
            Astero = Wplan.create_image(AsteroX, AsteroY, image=mesImages[0])
            dicoAstero[Astero] = [AsteroX, AsteroY, 0]

        if actualTime >= refreshTime +0.35:
>>>>>>> b74c7aee8529bbd3f5af513e079b646fd53156d4
            refreshTime = actualTime
            for Astero in dicoAstero:
                if dicoAstero[Astero][2] == 23:
                    AsteroX = random.randint(750, 1200)
                    AsteroY = random.randint(100, 620)
                    dicoAstero[Astero] = [AsteroX, AsteroY, 0]

                Wplan.move(Astero, -Deltax, 0)
                Wplan.itemconfigure(Astero, image=mesImages[dicoAstero[Astero][2]])
                dicoAstero[Astero][2] += 1
                dicoAstero[Astero][0] -= Deltax

<<<<<<< HEAD
=======
def SuppressionAstero():
    global Astero, dicoAstero

    listSuppressionAstero = []
    for Astero in dicoAstero:
        if dicoAstero[Astero][0] <= 0:
            listSuppressionAstero.append(Astero)
    for Astero in listSuppressionAstero:
        Wplan.delete(Astero)
        dicoAstero.pop(Astero)
        print("Astéroide Supprimé")




def DetectionCollision():
    global Astero, Wfusee, dicoAstero
    global Wplan
    global Vivant
    global mesImages, NumImage
    global listeScore
    global NbrePoints
    global JeuTermine

    global PremiereCollision, DeuxiemeCollision, TroisiemeCollision

    toPopAsteroDetruit = []

    if Vivant == True:
        for Astero in dicoAstero:
            if (Wplan.coords(Wfusee)[0]) + 87.5 >= (Wplan.coords(Astero)[0]) - 50 and (Wplan.coords(Wfusee)[0]) - 87.5 <= (Wplan.coords(Astero)[0]) + 50 :
                if (Wplan.coords(Wfusee)[1]) + 25 >= (Wplan.coords(Astero)[1]) - 50 > (Wplan.coords(Wfusee)[1]) - 25 or (Wplan.coords(Wfusee)[1]) - 25 <= (Wplan.coords(Astero)[1]) + 50 < (Wplan.coords(Wfusee)[1]) + 25 or(Wplan.coords(Astero)[1]) + 50 >= (Wplan.coords(Wfusee)[1]) + 25 > (Wplan.coords(Wfusee)[1]) - 25 >= (Wplan.coords(Astero)[1]) - 50:

                    print("Coordonnées Astéro : ", Wplan.coords(Astero))
                    print("Coordonnées Fusée : ", Wplan.coords(Wfusee))
                    toPopAsteroDetruit.append(Astero)
                    if PremiereCollision == False:
                        Wplan.itemconfig(Barre, image=DeuxCarre)
                        PremiereCollision = True
                        time.sleep(0.1)
                    elif DeuxiemeCollision == False:
                        Wplan.itemconfig(Barre, image=UnCarre)
                        DeuxiemeCollision = True
                        time.sleep(0.1)
                    elif DeuxiemeCollision == True:
                        Wplan.itemconfig(Barre, image=GameOver)
                        print("ListeScore = ", listeScore)
                        os.startfile("GameOverPage.py")
                        window.quit()
        for Astero in toPopAsteroDetruit:
            Wplan.delete(Astero)
            dicoAstero.pop(Astero)


>>>>>>> b74c7aee8529bbd3f5af513e079b646fd53156d4

window = Tk()
window.title("SPACE JUMPER 3000")


# Faire en sorte que la taille de la fenêtre s'adapte à n'importe quel écran :
largeur_fenetre = window.winfo_screenwidth()
hauteur_fenetre = window.winfo_screenheight()

window.geometry("%dx%d+0+0" % (largeur_fenetre, hauteur_fenetre))
window.attributes('-fullscreen', True)

#------- Police -------#

Times = font.Font(family='Times', size=18, weight='bold')

EnsembleLaser=[]
EnsembleAsteroide=[]
Temps_Generer=5000

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

Astero = Wplan.create_image(random.randint(750, 1200), random.randint(100, 620))

mesImages=[]
for i in range(24):
    nom = "img/Asteroide" + str(i) + ".png"
    mesImages.append(PhotoImage(file=nom))


#---Affichage Chrono ---#
start = default_timer()
chrono = Wplan.create_text(40, 20)

#---------------#

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
dicoAstero = {}
<<<<<<< HEAD
#listAsteroX = []
#listAsteroY = []
#listNumImage = []
=======
>>>>>>> b74c7aee8529bbd3f5af513e079b646fd53156d4


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

#Traitement du meilleur Score avec le CSV---#
listeScore = []


Principale()
chronometre()
#Attaque()
#Create_asteroide()
#aeiouy()
print(f'{dicoAstero}')
window.mainloop()