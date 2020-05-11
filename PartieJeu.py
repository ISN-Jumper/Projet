from tkinter import *
from tkinter import font
import random
from timeit import default_timer
import os
from PIL import Image, ImageTk

#-------------Fonctions-----------#

#---- Mouvement fusée ---#
def Haut(evt):
    global Wplan
    global Wfusee
    PosY = Wplan.coords(Wfusee)[1]  #PosY devient la variable contenant les coordonées en Y de la fusée
    if PosY -50 > 50: #On empêche la fusée de sortir du cadre
            # Si la position de la fusée en Y -50 ( on retire 50 car la fusée à une largeur de 100 ) est plus grande que 50 alors :
        Wplan.coords(Wfusee, Wplan.coords(Wfusee)[0], PosY -50)
    else:
        Wplan.coords(Wfusee, Wplan.coords(Wfusee)[0], PosY)
def Bas(evt):
    global Wplan
    global Wfusee
    PosY = Wplan.coords(Wfusee)[1]
    if PosY +83 < hauteur_fenetre:  # la fusée a une largeur de 175 pixel, d'où le + 83 (175//2)
                            #Si sa position en Y est inférieur à la hauteur de la fenêtre alors :
        Wplan.coords(Wfusee, Wplan.coords(Wfusee)[0], PosY + 65)
    else:
        Wplan.coords(Wfusee, Wplan.coords(Wfusee)[0], PosY) # Sinon la fusée ne descend pas plus bas
def Gauche(evt):
    global Wplan
    global Wfusee
    PosX = Wplan.coords(Wfusee)[0] #PosX devient la variable contenant les coordonées en X de la fusée
    if PosX - 83 > 0:
        Wplan.coords(Wfusee, PosX - 30, Wplan.coords(Wfusee)[1])
    else:
        Wplan.coords(Wfusee, PosX, Wplan.coords(Wfusee)[1])
def Droite(evt):
    global Wplan
    global Wfusee

    PosX=Wplan.coords(Wfusee)[0]
    if PosX + 30 < 400:  #Délimitation en X à 400 de manière à ce que la fusée ne se déplace pas là où les astéroides spawn

        Wplan.coords(Wfusee, PosX +30, Wplan.coords(Wfusee)[1])
    else:
        Wplan.coords(Wfusee, PosX, Wplan.coords(Wfusee)[1])

#-----Generer Asteroide------#
class Attaque_asteroide :
    def __init__(self, AsteroX,AsteroY, Wplan):

        self.Wplan = Wplan
        self.id = self.Wplan.create_image(AsteroX, AsteroY, image=mesImages[NumImage]) #grâce à cette class, chaque asteroide est identifiable avec self.id
        self.tour=0
    def animation_2(self):
        global Wfusee
        global Barre
        global Wplan
        global PremiereCollision, DeuxiemeCollision
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
                    Wplan.coords(self.id, Wplan.coords(self.id)[0] -460, Wplan.coords(self.id)[1])
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

    if Temps_Generer > 900 : #Si le temps de génération entre deux asteroides est supérieur à 900
        Temps_Generer-=100  #Alors le temps diminue de 100 ms
    AsteroX = random.randint(1000, largeur_fenetre-50) #Coordonées en X de l'asteroide générés aléatoirement entre 1000 et la largeur de la fenêtre -50 car la largeur de l'asteroide est de 100
    AsteroY = random.randint(50, hauteur_fenetre-50) #Pareillement pour les coordonées en Y
    Wasteroide = Attaque_asteroide(AsteroX, AsteroY, Wplan) #Creation de l'asteroide grâce à la class Attaque_asteroide
    EnsembleAsteroide.add(Wasteroide)   #On repertorie l'asteroide dans le set EnsembleAsteroide

    window.after(Temps_Generer, Create_asteroide) #Après le temps de generation entre deux asteroide on recréer un nouvel asteroide
def animation_asteroide():
    for Wasteroide in EnsembleAsteroide: #Pour les asteroides dans le set EnsembleAsteroide
        Wasteroide.animation_2() #on utilise la fonction animation_2 dans la class Attaque_asteroide pour les animer
    window.after(350, animation_asteroide)

#--------Generer Laser -------#
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

#-------FullScreen-------#
def Exit(evt): #Même fonctions utilisées pour l'accueil
    window.attributes('-fullscreen', True)
    Wplan.bind_all('<Escape>', Exit_inverse)
def Exit_inverse(evt):
    window.attributes('-fullscreen', False)
    Wplan.bind_all('<Escape>', Exit)
#----

def chronometre():
    now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    Wplan.itemconfigure(chrono, text=str_time, fill='white', font=Times)
    window.after(1000, chronometre)

#---------------------------------#

window = Tk()
window.title("SPACE JUMPER 3000")

# Faire en sorte que la taille de la fenêtre s'adapte à n'importe quel écran :
largeur_fenetre = window.winfo_screenwidth()
hauteur_fenetre = window.winfo_screenheight()

window.geometry("%dx%d+0+0" % (largeur_fenetre, hauteur_fenetre))
window.attributes('-fullscreen', True)

#------- Police -------#
Times = font.Font(family='Times', size=18, weight='bold')

#------ Variable fonction create_laser et animation_laser -------#

EnsembleLaser=set() #Initialisation d'un set contenant les lasers créés par l'utilisateur

#------ Variables fonction create_asteroide et animation_asteroide -------#

EnsembleAsteroide=set() #Initialisation d'un set contenant les astéroides créés par le programme
Temps_Generer=5000 # Temps de génération entre les deux premiers asteroides de  5 secondes (diminue dans le temps)

# --------- #
animation_laser()
animation_asteroide()

#---------Image-------#
Fusee=PhotoImage(file='Fusées/Fusee0.png')
Laser=PhotoImage(file='Laser.png')
Invisible=PhotoImage(file='invisible.png')

#------------- Graphique accueil --------#
Wplan=Canvas(window, width=largeur_fenetre, height=hauteur_fenetre)
Wplan.grid()

#------ Fond --------- #
WCCiel=Image.open('Ciel.png')
WCCiel = WCCiel.resize((largeur_fenetre, hauteur_fenetre), Image.ANTIALIAS) # La taille du fond s'adapte à la taille de l'ecran grâce à la bibliothèque PIL
Ciel=ImageTk.PhotoImage(WCCiel)   #Configuration de l'image pour tkinter
WCiel=Wplan.create_image((largeur_fenetre//2)-2, (hauteur_fenetre//2)-2, image=Ciel) #Creation de l'image dans le canvas

#-------#
AffichageChrono = Wplan.create_text(largeur_fenetre//2,hauteur_fenetre//2)

#------#
Wfusee=Wplan.create_image(100,360, image=Fusee) # Affichage de la fusée

#---- Variables pour animation des astéroides ---#
mesImages=[] # Liste qui contient les positions de l'asteroide et servira a animer l'asteroide
for i in range(24):
    nom = "img\Astéroïde" + str(i) + ".png"
    mesImages.append(PhotoImage(file=nom))
NumImage=0

#---Affichage Chrono ---#
start = default_timer()
chrono = Wplan.create_text(40, 20)

#--Nombres de Points---#
NbrePoints = 0
CanvasPoints = Wplan.create_text(largeur_fenetre/2, 20, text=('Nombre de Points :', NbrePoints), fill='white', font=Times)

#-----Déplacement fusée -----#
Wplan.bind_all('z', Haut) # Lorsque l'utilisateur appuie sur la touche z (minuscule) la fonction Haut s'active, la fusée monte
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

#--- Variables pour collision, fonction animation_asteroide
PremiereCollision = False #--- Variables booleennes qui serviront à faire baisser la barre de vie du joueur lors d'une collision avec un asteroide
DeuxiemeCollision = False

#------
chronometre()
Create_asteroide()

window.mainloop()