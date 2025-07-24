
# Demonstration du polymorphisme

# Le Polymorphisme permet de nommer deux methode qui ont une meme fonction dans les class fils des classe parente, sauf que le comportement est different

class Form:
    def __init__(self, nom_forme):
        self.nom_forme = nom_forme

    def calcule_aire(self):
        print("Calcule de l'aire")

    def affiche_nom_forme(self):
        print(f"le nom de la figure est {self.nom_forme}")

class Rectangle(Form):
    def __init__(self,long,larg):
        super().__init__("Rectangle")
        self.long=long
        self.larg = larg

    def calcule_aire(self):
        result =(self.long+self.larg)**2
        print(f"le calcule de l'aire est {result}")


class Cercle(Form):
    def __init__(self,r):
        super().__init__("Cercle")
        self.rayon = r

    def calcule_aire(self):
        result = self.rayon**2
        print(f"le calcule de l'aire est {result}")



rect = Rectangle(15,10)
rect.affiche_nom_forme()
rect.calcule_aire()

cer = Cercle(15)
cer.affiche_nom_forme()
cer.calcule_aire()