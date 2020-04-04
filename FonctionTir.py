import PartieJeu

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