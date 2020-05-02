from tkinter import *
from tkinter import font
import random
from timeit import default_timer
import os
from PIL import Image, ImageTk
import time
from threading import *

LaCollision = False
EcranTraverse = False
LaCollisionLaser = False

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

def Attaque():
    global AsteroX
    global AsteroY
    global Deltax
    global NumImage
    global mesImages
    global Wplan
    global Wasteroide
    global CoordonneesAsteroide
    global Vivant
    global Passe
    global EcranTraverse

    if Vivant ==True :
        Passe=True
        Wplan.delete(Wasteroide)
        Wasteroide = Wplan.create_image(AsteroX, AsteroY, image=mesImages[NumImage])
        NumImage += 1
        AsteroX -= Deltax

        if NumImage == 23:
            NumImage = 0
            AsteroX = random.randint(750, 1200)
            AsteroY = random.randint(100, 620)
        Wplan.after(500, Attaque)

    elif Vivant==False :
        NumImage=0
        AsteroX=random.randint(750, 1200)
        AsteroY = random.randint(100, 620)
        Vivant=True
        Wplan.after(500,Attaque)


class Attaque_asteroide :
    def __init__(self, Asterix, Obely, Wplan):

        self.Wplan = Wplan
        self.id = self.Wplan.create_image(Asterix, Obely, image=mesImages[NumImage])
        self.tour=0
    def animation_2(self):
        global Wfusee
        global Barre
        global Wplan
        global AsteroX, AsteroY
        global Vivant, Passe
        global PremiereCollision, DeuxiemeCollision, TroisiemeCollision
        global NumImage, mesImages, Wplan, tour

        if Wplan.coords(self.id)[0] > -50 :
            self.Wplan.move(self.id, -23, 0)
            self.tour+=23
            NumImage += 1
            self.Wplan.itemconfig(self.id, image=mesImages[NumImage])
            if self.tour >= largeur_fenetre :
                self.tour=0
                self.Wplan.delete(self.id)

            if NumImage == 23:
                NumImage = 0

            if (Wplan.coords(Wfusee)[0]) + 72.5 >= (Wplan.coords(self.id)[0]) - 50 and (Wplan.coords(Wfusee)[0]) - 72.5 <= (Wplan.coords(self.id)[0]) + 50 :
                if (Wplan.coords(Wfusee)[1]) + 25 >= (Wplan.coords(self.id)[1]) - 50 > (Wplan.coords(Wfusee)[1]) - 25 or (Wplan.coords(Wfusee)[1]) - 25 <= (Wplan.coords(self.id)[1]) + 50 < (Wplan.coords(Wfusee)[1]) + 25 or(Wplan.coords(self.id)[1]) + 50 >= (Wplan.coords(Wfusee)[1]) + 25 > (Wplan.coords(Wfusee)[1]) - 25 >= (Wplan.coords(self.id)[1]) - 50:
                    Wplan.itemconfig(self.id, image=Invisible)
                    Wplan.coords(self.id, Wplan.coords(self.id)[0] -400, Wplan.coords(self.id)[1])
                    if PremiereCollision == False:
                        Wplan.itemconfig(Barre, image=DeuxCarre)
                        PremiereCollision = True
                    elif DeuxiemeCollision == False:
                        Wplan.itemconfig(Barre, image=UnCarre)
                        DeuxiemeCollision = True
                    elif DeuxiemeCollision == True:
                        os.startfile("C:/Users/remi1/PycharmProjects/SpaceJumper3000/GameOverPage.py")
                        window.quit()


def Create_asteroide():
    global Temps_Generer, NumImage, mesImages

    if Temps_Generer > 800 :
        Temps_Generer-=100
    Asterix = random.randint(900, 1200)
    Obely = random.randint(100, 620)
    lasteroide = Attaque_asteroide(Asterix, Obely, Wplan)
    EnsembleAsteroide.add(lasteroide)

    window.after(Temps_Generer, Create_asteroide)

def animation_asteroide():
    for lasteroide in EnsembleAsteroide:
        lasteroide.animation_2()
    window.after(300, animation_asteroide)

class Perso:
    def __init__(self, Cordox, Cordoy, Wplan):
        self.Wplan = Wplan
        self.id = self.Wplan.create_image(Cordox, Cordoy, image=Laser)

    def animation(self):
        self.Wplan.move(self.id, 6, 0)

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
        if x0 > largeur_fenetre - 1:
            Wplan.delete(personnage.id)
            EnsembleLaser.remove(personnage)
    window.after(3, animation_laser)

class CollisionLaserAstero(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        global Wplan
        global AsteroX
        global AsteroY
        global LaCollisionLaser
        global NbrePoints
        global Astero
        global listAstero
        global Wasteroide
        while LaCollisionLaser == False:
            Cordo = Wplan.coords(Wfusee)
            LaserX = Cordo.pop(0) + 87.5 + 10
            LaserY = Cordo.pop(0) + 1

            for Astero in listAstero:
                if LaserX + 15 >= (Wplan.coords(Wasteroide)[0]) - 50:
                    if LaserY + 2.5 >= (Wplan.coords(Astero)[1]) - 50 > (LaserY) - 2.5 or (LaserY) - 2.5 <= (
                            Wplan.coords(Astero)[1]) + 50 < (LaserY) + 2.5 or (Wplan.coords(Astero)[1]) + 50 >= (
                            LaserY) + 2.5 > (LaserY) - 2.5 >= (Wplan.coords(Astero)[1]) - 50:
                        Wplan.delete(Astero)
                        for i in listAsteroX:
                            listAsteroX[i] = random.randint(750, 1200)
                        for i in listAsteroY:
                            listAsteroY[i] = random.randint(750, 1200)
                        print("!!!!!!!!!COLLISIONAVECLELASER!!!!!!!!!!")
                        NbrePoints += 1
                        time.sleep(0.3)
                        Wplan.itemconfig(CanvasPoints, text=('Nombre de Points :', NbrePoints))

def Exit(evt):
    window.attributes('-fullscreen', True)
    Wplan.bind_all('<Escape>', Tixe)
def Tixe(evt):
    window.attributes('-fullscreen', False)
    Wplan.bind_all('<Escape>', Exit)

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
                    AsteroX = random.randint(750, 1200)
                    AsteroY = random.randint(100, 620)
                    listAsteroX = [random.randint(750, 1200)]
                    listAsteroY = [random.randint(100, 620)]
                    print(LaCollision)
            while LaCollision == True:
                if len(Wplan.find_overlapping(CoordoneesFusee[0], CoordoneesFusee[1], CoordoneesFusee[2],
                                              CoordoneesFusee[3])) == 3:
                    print("!!!!!!!!!COLLISION11111!!!!!!!!!!")
                    NombreDeVie -= 0.5
                    LaCollision = False
                    AsteroX = random.randint(750, 1200)
                    AsteroY = random.randint(100, 620)
                    listAsteroX = [random.randint(750, 1200)]
                    listAsteroY = [random.randint(100, 620)]
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

def chronometre():
    now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    Wplan.itemconfigure(chrono, text=str_time, fill='white', font=Times)
    window.after(1000, chronometre)

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
        startTime = time.time()

        while Vivant:
            actualTime = time.time()
            if actualTime >= startTime + 2:
                listAsteroX.append(random.randint(750,1200))
                listAsteroY.append(random.randint(100,620))
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

'''

def AutoAstero():
    global Passe
    global mesImages
    global NumImage
    AsteroX = random.randint(750, 1200)
    AsteroY = random.randint(100, 620)
    while Vivant == True:
        Passe = True
        Wplan.create_image(AsteroX, AsteroY, image=mesImages[NumImage])
        NumImage += 1
        AsteroX -= Deltax
        time.sleep(1)
        if NumImage == 23:
            NumImage = 0
            AsteroX = random.randint(750, 1200)
            AsteroY = random.randint(100, 620)
            Wplan.create_image(AsteroX, AsteroY, image=mesImages[NumImage])
        Wplan.after(100, Attaque)
'''

window = Tk()
window.title("SPACE JUMPER 3000")

# Faire en sorte que la taille de la fenêtre s'adapte à n'importe quel écran :
largeur_fenetre = window.winfo_screenwidth()
hauteur_fenetre = window.winfo_screenheight()

window.geometry("%dx%d+0+0" % (largeur_fenetre, hauteur_fenetre))
#window.geometry("1280x720+40+50")

#------- Police -------#

Times = font.Font(family='Times', size=18, weight='bold')

EnsembleLaser=set()
EnsembleAsteroide=set()
Temps_Generer=5000

window.after(10, animation_laser)
window.after(10, animation_asteroide)
#---------Image-------#

Fusee=PhotoImage(file='fusée2.png')
Laser=PhotoImage(file='Laser.png')
Invisible=PhotoImage(file='invisible.png')


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
PositionAstero = Wplan.coords(Wasteroide)
AsteroX=random.randint(750, 1200)
AsteroY=random.randint(100, 620)
Deltax=50
NumImage=0
temps=2500

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

#---Nombre de vies---#
NombresVie = 3

#---Barre de Vie---#
TroisCarre=PhotoImage(file='img/Barre de Progression/3.png')
Barre = Wplan.create_image(largeur_fenetre*0.957, hauteur_fenetre*0.026, image=TroisCarre)
DeuxCarre=PhotoImage(file='img/Barre de Progression/2.png')
UnCarre=PhotoImage(file='img/Barre de Progression/1.png')
GameOver=PhotoImage(file='img/Barre de Progression/Game Over.png')

Vivant=True
Passe=True

PremiereCollision = False
DeuxiemeCollision = False

#CollisionLaserAstero()
#Collision()
chronometre()
#Attaque()
#GenererAstero()
Create_asteroide()
#aeiouy()

window.mainloop()