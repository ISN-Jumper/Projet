liste = []

class test:
    def __init__(self, name):
        self.name = name
    def remove(self):
        liste.remove(self)
    def ton_nom(self):
        print(self.name)

for i in range(10):
    testing = test(i)
    liste.append(testing)
print(liste)
for perso in liste.copy()[:5]:
    perso.remove()
print(liste)