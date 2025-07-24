
class Rectangle:
    def __init__(self, long,larg):
        self.long = long
        self.larg = larg

    def perimetre(self):
        result = (self.long*2)+(self.larg*2)
        print(f"Perimetre : {result}")

    def aire(self):
        result = (self.long * self.larg)
        print(f"Aire : {result}")

    def est_carre(self):

        verif = False
        if self.long == self.larg :
            verif = True
            print(f"Est carre ? {verif}")
        else :
            print(f"Est carre ? {verif}")


rect1 = Rectangle(5,6)
rect1.perimetre()
rect1.aire()
rect1.est_carre()

rect2 = Rectangle(8,8)
rect2.perimetre()
rect2.aire()
rect2.est_carre()