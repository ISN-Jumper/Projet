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

def Hub(evt):
    global Laser
    global LaserX
    global LaserY
    global LaserX2
    global LaserY2
    global LaserX3
    global LaserY3
    global LaserX4
    global LaserY4
    global LaserX5
    global LaserY5
    global LaserX6
    global LaserY6
    global LaserX7
    global LaserY7
    global LaserX8
    global LaserY8
    global LaserX9
    global LaserY9
    global LaserX10
    global LaserY10
    global Perso1
    global Perso2
    global Perso3
    global Perso4
    global Perso5
    global Perso6
    global Perso7
    global Perso8
    global Perso9
    global Perso10
    global tour

    Cordo = Wplan.coords(Wfusee)
    tour+=1

    if tour ==1:
        LaserX = Cordo.pop(0) + 87.5
        LaserY = Cordo.pop(0)
        Perso1 = Wplan.create_image(LaserX, LaserY, image=Laser)
        Tir()

    if tour==2:
        LaserX2 = Cordo.pop(0) + 87.5
        LaserY2 = Cordo.pop(0)
        Perso2 = Wplan.create_image(LaserX, LaserY, image=Laser)
        Tir2()

    if tour==3:
        LaserX3 = Cordo.pop(0) + 87.5
        LaserY3 = Cordo.pop(0)
        Perso3 = Wplan.create_image(LaserX, LaserY, image=Laser)
        Tir3()

    if tour==4:
        LaserX4 = Cordo.pop(0) + 87.5
        LaserY4 = Cordo.pop(0)
        Perso4 = Wplan.create_image(LaserX, LaserY, image=Laser)
        Tir4()

    if tour==5:
        LaserX5 = Cordo.pop(0) + 87.5
        LaserY5 = Cordo.pop(0)
        Perso5 = Wplan.create_image(LaserX, LaserY, image=Laser)
        Tir5()

    if tour ==6:
        LaserX6 = Cordo.pop(0) + 87.5
        LaserY6 = Cordo.pop(0)
        Perso6 = Wplan.create_image(LaserX, LaserY, image=Laser)
        Tir6()

    if tour==7:
        LaserX7 = Cordo.pop(0) + 87.5
        LaserY7 = Cordo.pop(0)
        Perso7 = Wplan.create_image(LaserX, LaserY, image=Laser)
        Tir7()

    if tour==8:
        LaserX8 = Cordo.pop(0) + 87.5
        LaserY8 = Cordo.pop(0)
        Perso8 = Wplan.create_image(LaserX, LaserY, image=Laser)
        Tir8()

    if tour==9:
        LaserX9 = Cordo.pop(0) + 87.5
        LaserY9 = Cordo.pop(0)
        Perso9 = Wplan.create_image(LaserX, LaserY, image=Laser)
        Tir9()

    if tour==10:
        LaserX10 = Cordo.pop(0) + 87.5
        LaserY10 = Cordo.pop(0)
        Perso10 = Wplan.create_image(LaserX, LaserY, image=Laser)
        tour=0
        Tir10()

def Tir():
    global LaserX
    global LaserY
    global Perso1

    xf = LaserX + Mvt[0][0]
    if xf==1900:
        Wplan.delete(Perso1)

    if 100 < xf <1900 :
        LaserX= xf
        Wplan.coords(Perso1, xf, LaserY)
        Wplan.after(3, Tir)

def Tir2():
    global LaserX2
    global LaserY2
    global perso2

    xf = LaserX2 + Mvt[0][0]
    if xf==1900:
        Wplan.delete(Perso2)

    if 100 < xf <1900 :
        LaserX2= xf
        Wplan.coords(Perso2, xf, LaserY2)
        Wplan.after(3, Tir2)

def Tir3():
    global LaserX3
    global LaserY3
    global Perso3

    xf = LaserX3 + Mvt[0][0]
    if xf==1900:
        Wplan.delete(Perso3)

    if 100 < xf <1900 :
        LaserX3= xf
        Wplan.coords(Perso3, xf, LaserY3)
        Wplan.after(3, Tir3)

def Tir4():
    global LaserX4
    global LaserY4
    global Perso4

    xf = LaserX4 + Mvt[0][0]
    if xf==1900:
        Wplan.delete(Perso4)

    if 100 < xf <1900 :
        LaserX4= xf
        Wplan.coords(Perso4, xf, LaserY4)
        Wplan.after(3, Tir4)

def Tir5():
    global LaserX5
    global LaserY5
    global Perso5

    xf = LaserX5 + Mvt[0][0]
    if xf==1900:
        Wplan.delete(Perso5)

    if 100 < xf <1900 :
        LaserX5= xf
        Wplan.coords(Perso5, xf, LaserY5)
        Wplan.after(3, Tir5)

def Tir6():
    global LaserX6
    global LaserY6
    global Perso6

    xf = LaserX6 + Mvt[0][0]
    if xf==1900:
        Wplan.delete(Perso6)

    if 100 < xf <1900 :
        LaserX6= xf
        Wplan.coords(Perso6, xf, LaserY6)
        Wplan.after(3, Tir6)

def Tir7():
    global LaserX7
    global LaserY7
    global perso7

    xf = LaserX7 + Mvt[0][0]
    if xf==1900:
        Wplan.delete(Perso7)

    if 100 < xf <1900 :
        LaserX7= xf
        Wplan.coords(Perso7, xf, LaserY7)
        Wplan.after(3, Tir7)

def Tir8():
    global LaserX8
    global LaserY8
    global Perso8

    xf = LaserX8 + Mvt[0][0]
    if xf==1900:
        Wplan.delete(Perso8)

    if 100 < xf <1900 :
        LaserX8= xf
        Wplan.coords(Perso8, xf, LaserY8)
        Wplan.after(3, Tir8)

def Tir9():
    global LaserX9
    global LaserY9
    global Perso9

    xf = LaserX9 + Mvt[0][0]
    if xf==1900:
        Wplan.delete(Perso9)

    if 100 < xf <1900 :
        LaserX9= xf
        Wplan.coords(Perso9, xf, LaserY9)
        Wplan.after(3, Tir9)

def Tir10():
    global LaserX10
    global LaserY10
    global Perso10

    xf = LaserX10 + Mvt[0][0]
    if xf==1900:
        Wplan.delete(Perso10)

    if 100 < xf <1900 :
        LaserX10= xf
        Wplan.coords(Perso10, xf, LaserY10)
        Wplan.after(3, Tir10)

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

#---------Image-------#

Ciel=PhotoImage(file='Ciel.png')
Fusee=PhotoImage(file='fusée2.png')
Laser=PhotoImage(file='Laser.png')

#---------Variables cordos----------#
LaserX=0
LaserY=0
LaserX2=0
LaserY2=0
LaserX3=0
LaserY3=0
LaserX4=0
LaserY4=0
LaserX5=0
LaserY5=0
LaserX6=0
LaserY6=0
LaserX7=0
LaserY7=0
LaserX8=0
LaserY8=0
LaserX9=0
LaserY9=0
LaserX10=0
LaserY10=0

Persos=[[50,50],[250,250]]
Mvt=[[10,0],[-10,-10]]

#------------- Graphique accueil --------#

Wplan=Canvas(window, width=largeur_fenetre-4, height=hauteur_fenetre-68)
Wplan.grid()

Wplan.create_image(640, 360, image=Ciel)
AffichageChrono = Wplan.create_text(largeur_fenetre//2,hauteur_fenetre//2)

Wfusee=Wplan.create_image(100,360, image=Fusee)

Perso1=0
Perso2=0
perso3=0
perso4=0
perso5=0
Perso6=0
Perso7=0
perso8=0
perso9=0
perso10=0

tour=0

Wasteroide=Wplan.create_image(random.randint(750, 1200), random.randint(100, 620))
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

Finit=False
#-----Déplacement fusée -----#
Wplan.bind_all('z', Haut)
Wplan.bind_all('s', Bas)
Wplan.bind_all('d', Droite)
Wplan.bind_all('q', Gauche)

#----Tir laser--------#


Wplan.bind_all('<space>', Hub)

#------#

chronometre()
Attaque()

window.mainloop()