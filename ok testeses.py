import tkinter as tk


class Perso:
    def __init__(self, x, y, Wplan):
        self.Wplan = Wplan
        self.id = self.Wplan.create_image(x, y, image=Laser)

    def animate(self):
        self.Wplan.move(self.id, 6, 0)


def Create_laser(event):
    Cordo = Wplan.coords(Wfusee)
    LaserX = Cordo.pop(0) + 87.5
    LaserY = Cordo.pop(0)
    personnage = Perso(LaserX, LaserY, Wplan)
    engine.add(personnage)


def animate_ovals():
    to_be_deleted = set()
    for personnage in engine:
        personnage.animate()
        x0, y0, x1, Y1 = Wplan.bbox(personnage.id)
        if x0 > 1368:
            Wplan.delete(personnage.id)
            to_be_deleted.add(personnage)
    for personnage in to_be_deleted:
        engine.remove(personnage)
    app.after(3, animate_ovals)


app = tk.Tk()
instruction = tk.Label(app, text="Clic gauche de souris pour ajout  er un oval",
                       font=("", 28))
instruction.grid()
Wplan = tk.Canvas(app, width=1368, height=912)
Wplan.grid()

Fusee = tk.PhotoImage(file='fusée2.png')
Laser = tk.PhotoImage(file='Laser.png')
Wfusee = Wplan.create_image(100, 360, image=Fusee)

engine = set()
app.after(10, animate_ovals)

app.bind("<space>", Create_laser)
app.mainloop()