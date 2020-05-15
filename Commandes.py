from tkinter import *
from PIL import Image, ImageTk
import os

def RetourAccueil():
    os.startfile("C:/Users/User/Desktop/ProjetTest2/Accueil.py")
    CommandesPage.quit()



CommandesPage = Tk()
CommandesPage.title("Space Shooter - Commandes")
CommandesPage.geometry("600x600")

CommandesPage.resizable(width=False, height=False)

Wplan = Canvas(CommandesPage, width=600, height=600)
Wplan.pack()


WCCiel = Image.open('Ciel.png')
WCCiel = WCCiel.resize((1280, 720), Image.ANTIALIAS)
Ciel = ImageTk.PhotoImage(WCCiel)
WCiel = Wplan.create_image(150, 300, image=Ciel)

imageClavier = Image.open("zqsd.png")
imageClavier.resize((10,10), Image.ANTIALIAS)
touche_clavier = ImageTk.PhotoImage(imageClavier)
Wplan.create_image(300,150, image=touche_clavier)

#---Image SpaceShooter3000 ---#
touches_clavier = PhotoImage("zqsd.png")
Wplan.create_image(0,100, image=touches_clavier)



#---Commandes clavier---#
EnHaut = Wplan.create_text(290,130, text="Se déplacer vers le haut", fill="white", font="Arial 10")
AGauche = Wplan.create_text(130,290, text="Se déplacer vers la gauche |", fill="white", font="Arial 10")
Decendre = Wplan.create_text(295,290, text="Se déplacer vers le bas |", fill="white", font="Arial 10")
ADroite = Wplan.create_text(450,290, text="Se déplacer vers la droite", fill="white", font="Arial 10")
TirLaser = Wplan.create_rectangle(500, 350, 100, 400,fill="white")
TextTireLaser = Wplan.create_text(295,410, text="Appuyez sur la barre Espace pour lancer le laser", fill='white', font="Arial 10")

Retour = Button(CommandesPage, text="Revenir à la page d'accueil", font="Arial 12", command=lambda:RetourAccueil()).place(x=200,y=500)

CommandesPage.mainloop()