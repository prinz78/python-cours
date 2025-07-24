

# Creation d'une class et verification, une classe se cree avec le format CamelCase

class Personne :
    # nom = "Willis"
    # prenom ="Bruce"
    # age = 33

# declaration des parametre par deffaut du constructeur avec le parametre self qui met en relation le constructeur de la classe et l'objet instancie
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.email = None
# pour ajouter des fonctions(methodes) a la class :

# premierre fonction pour afficher l'utilisateur :

    def afficher_utilisateur(self):
        print(f"j'affiche l'objets personnes isntancie {self.nom}, {self.prenom}, {self.age}, {self.email}")

# deuxiemme fonction pour ajouter un email a l'utilisateur avec l'operateur return

    def ajout_email(self, email):
        self.email = email

# Heritage ajouter une classe derive :

class Etudiant(Personne):
# pour heriter les atribut il faut ajouter le constructeur de la classe herite + de la classe pere(avec la methode constructeur super().__init__()) et les parametre pere sans le self
    def __init__(self, nom, prenom, age,notes):
        super().__init__(nom, prenom, age)
        self.notes=notes

    def ajout_matiere(self, matiere, note):
        self.notes[matiere] = note

    def moyenne_etudiant(self):
        moyenne = sum(self.notes.values())/float(len(self.notes.values()))
        return moyenne

class Musicien(Personne):
    def __init__(self, nom, prenom, age, instrument):
        super().__init__(nom, prenom, age)
        self.instrument = instrument

per1 = Personne("Charm","Mouloud",22)
per2 = Personne("War","daniella",18)
per3 = Personne("Dor","leila",18)

per1.afficher_utilisateur()
per2.afficher_utilisateur()
per3.afficher_utilisateur()

per1.ajout_email("char@gemail.com")
per2.ajout_email("war@gmail.com")
per3.ajout_email("dor@gmail.com")

per1.afficher_utilisateur()
per2.afficher_utilisateur()
per3.afficher_utilisateur()

etudiant1 = Etudiant("Rakel","Nadine",18, {"Anglais" : 12,"la democratie": 20,"physyque" : 14})

etudiant1.afficher_utilisateur()

print(etudiant1.notes)
etudiant1.ajout_matiere("Allemand", 16)

print(etudiant1.notes)

la_moyenne1 = etudiant1.moyenne_etudiant()

print(f"la moyene de l'etudiant est: {la_moyenne1}")

musicien1 = Musicien("Correl", "Damien",25,"Bass")

print(musicien1.instrument)


# print(f"ceci est le resultat de la creation d'une classe {Personne}")

# Pour instancier une class :

# objet_instancie = Personne()
#
# print(objet_instancie.nom)