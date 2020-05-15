# -*- coding: utf-8 -*-
#
from tkinter import *
from tkinter import font
import os
from PIL import Image, ImageTk
import openpyxl
import time
from pygame import mixer

mixer.init()
mixer.music.load("DuaLipa1.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.2)

def ChangePage():
    os.startfile("PartieJeu.py")
    window.quit()

def PageBoutique():
    os.startfile("Boutique.py")
    window.quit()

def Exit(evt):
    window.attributes('-fullscreen', True)
    Wplan.bind_all('<Escape>', Tixe)
def Tixe(evt):
    window.attributes('-fullscreen', False)
    Wplan.bind_all('<Escape>', Exit)

def FullEcran():
    window.attributes('-fullscreen', False)
    WFullscreen.config(command = lambda : FullEcran2())
def FullEcran2():
    window.attributes('-fullscreen', True)
    WFullscreen.config(command= lambda : FullEcran())


def FuseeAnim():
    global Wfusee, deltaX, deltaY, FuseePil, Fusee, Passer, NumImage

    if Wplan.coords(Wfusee)[0] < (largeur_fenetre//2)-56 and Wplan.coords(Wfusee)[1] == 360 :
        deltaX+=9
        Wplan.coords(Wfusee, deltaX, deltaY )
        Wplan.after(12, FuseeAnim)

    elif Wplan.coords(Wfusee)[0] >= (largeur_fenetre//2)-56 and Wplan.coords(Wfusee)[1] ==360 :
        Passer = True

    if Passer ==True and NumImage < 9:
        NumImage += 1
        deltaX+=5
        deltaY-=20
        Wplan.delete(Wfusee)
        Wfusee=Wplan.create_image(deltaX, deltaY, image=mesImages[NumImage])
        Wplan.after(40, FuseeAnim)

    elif Passer==True and NumImage == 9:
        if deltaY < 525 :
            deltaY+=10
            Wplan.delete(Wfusee)
            Wfusee = Wplan.create_image(deltaX, deltaY, image=mesImages[NumImage])
            Wplan.after(4, FuseeAnim)
        elif deltaY >=525:
            TitreJumper()

NumImage=0
Passer = False

def TitreJumper():
    Wtitre=Wplan.create_image(largeur_fenetre//2, (hauteur_fenetre//2)-75, image=TkTitre)


if __name__ == '__main__':

    window=Tk()
    window.title("SPACE JUMPER 3000")

    #Faire en sorte que la taille de la fenêtre s'adapte à n'importe quel écran :
    largeur_fenetre = window.winfo_screenwidth()
    hauteur_fenetre = window.winfo_screenheight()

    window.geometry("%dx%d+0+0" % (largeur_fenetre,hauteur_fenetre))
    window.attributes('-fullscreen', True)
    #window.geometry("1280x720+40+50")

    #------- Police -------#

    Times = font.Font(family='Times', size=24, weight='bold')
    Times2 = font.Font(family='Times', size=16, weight='bold')

    #Ciel=PhotoImage(file='CielAccueil.png')

    #------Config Image-----#

    Fusee =PhotoImage(file='Fusées/Fusee0.png')
    FuseeFeu = PhotoImage(file='Fusées/FuseeFeu0.png')

    Invisible = PhotoImage(file='invisible.png')
    Titre = Image.open('Titre.png')
    TkTitre= ImageTk.PhotoImage(Titre)

    #------- Configuration du score --------#

    #workbook = Workbook()
    worksheets = openpyxl.load_workbook("Score.xlsx")
    worksheet = worksheets.active
    B1 = worksheet.cell(row=1, column=2)

    #------------- Graphique accueil --------#

    Wplan=Canvas(window, width=largeur_fenetre, height=hauteur_fenetre)
    Wplan.grid()

    WCCiel = Image.open('Ciel.png')
    WCCiel = WCCiel.resize((largeur_fenetre, hauteur_fenetre), Image.ANTIALIAS)
    Ciel = ImageTk.PhotoImage(WCCiel)
    WCiel = Wplan.create_image((largeur_fenetre // 2) - 2, (hauteur_fenetre // 2) - 2, image=Ciel)

    window.iconbitmap('Fusées/FuseeFeu3.ico')

  #  FuseePil = Image.open("fusée2.png")
 #   FuseePil = FuseePil.rotate(45)
   # Fusee = ImageTk.PhotoImage(FuseePil)
    deltaX=-20
    deltaY=360
    Wfusee = Wplan.create_image(deltaX, deltaY, image=FuseeFeu)

    mesImages=[]
    for i in range (10):
        nom = "Fusées/FuseeFeu"+str(i)+'.png'
        mesImages.append(PhotoImage(file=nom))

    #------------- Fullscreen -----------#

    Wplan.bind_all('<Escape>', Exit)

    #--------- Boutons --------#

    Jouer=Button(window, text='Jouer', width=9, font =Times, command = lambda : ChangePage())
    Jouer.grid()
    Jouer.place(x=(largeur_fenetre//2)-100, y=(hauteur_fenetre//1.5))

    Boutique = Button(window, text='Boutique', width=12, font=Times2, command=lambda: PageBoutique())
    Boutique.grid()
    Boutique.place(x=(largeur_fenetre // 2) - 86, y=(hauteur_fenetre // 1.35))

    Wquitter = Button(window, text="Quitter", font=Times2, command=window.quit)
    Wquitter.grid()
    Wquitter.place(x=50, y= hauteur_fenetre -150)

    WFullscreen = Button(window, text="Plein Ecran", font=Times2, command=FullEcran)
    WFullscreen.grid()
    WFullscreen.place(x=40, y=40)

    WScore = Wplan.create_text(largeur_fenetre - 190, 35, text='Banque : ', font=Times, fill='yellow',activefill='white')
    WPoints = Wplan.create_text(largeur_fenetre - 70, 35, text=str(B1.value) + " $", font=Times, fill='yellow',activefill='white')
    Wplan.create_line(largeur_fenetre - 255, 57, largeur_fenetre - 20, 57, fill='white', activefill='yellow', width=4)
    FuseeAnim()

    window.mainloop()