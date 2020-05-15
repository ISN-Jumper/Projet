from tkinter import *
from PIL import Image, ImageTk
import os
def RetourAccueil():
    os.startfile("C:/Users/User/Desktop/ProjetTest2/Accueil.py")
    CopyrightsPage.quit()

CopyrightsPage = Tk()
CopyrightsPage.title("Space Shooter - Copyrights")
CopyrightsPage.geometry("600x600")

CopyrightsPage.resizable(width=False, height=False)

Wplan = Canvas(CopyrightsPage, width=600, height=600)
Wplan.pack()


WCCiel = Image.open('Ciel.png')
WCCiel = WCCiel.resize((1280, 720), Image.ANTIALIAS)
Ciel = ImageTk.PhotoImage(WCCiel)
WCiel = Wplan.create_image(150, 300, image=Ciel)

image = Image.open("titrecopyrights.png")
titre = ImageTk.PhotoImage(image)
Wplan.create_image(300,100, image=titre)

#---Sources---#
Musique = Wplan.create_text(300,300, text="Musique : Dua Lipa - Swan Song Instrumental", fill="white", font="Arial 12")
BruitageLaser = Wplan.create_text(300,330, text="Bruitage Laser : Youtube/Bruitage Pro - Bruitage Pistolet n°6", fill="white", font="Arial 12")
BruitageExplosion = Wplan.create_text(300,360, text="Bruitage Explosion : Youtube/Clashofgamer43 Gamer - Bruitage explosion", fill="white", font="Arial 12")
BruitageCraquement = Wplan.create_text(300,390, text="Bruitage Craquement : Youtube/Bruitage Pro - bruitage craquement de doigts", fill="white", font="Arial 12")

Retour = Button(CopyrightsPage, text="Revenir à la page d'accueil", font="Arial 12", command=lambda:RetourAccueil()).place(x=200,y=500)

CopyrightsPage.mainloop()