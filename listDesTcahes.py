

class Taches:

# Declaration sans passage de parametre contructeur
    def __init__(self):
        self.tab_taches = {}
        self.tab_bool = {}
        self.tache_id = 0
        self.ete = False


# Ajout d'une tache en liant les deux dictionaire(teche, booleen) par self.tache.id
    def ajout_tache(self,tach_aj):

        self.ete = False
        if tach_aj in self.tab_taches.values():
            print(f"cette tache {tach_aj} existe deja dans la liste des taches")

        else:
            # self.tache_id += 1
            self.tab_taches[self.tache_id] = tach_aj
            self.tab_bool[self.tache_id] = self.ete
            self.tache_id += 1

    def terminer_tache(self,tach_termin):
        self.tache_id = tach_termin
        if tach_termin in self.tab_taches.keys():
            #del self.tab_taches[self.tache_id]
            self.tab_bool[self.tache_id] = True

        else :
            print(f"ce numero de tache {tach_termin} n'existe pas")



# supression d'une tache en liant les deux dictionaire(teche, booleen) par self.tache.id avec la fonction del

    def supprimer_tache(self,tach_sp):
        self.tache_id = tach_sp
        if tach_sp in self.tab_taches.keys():
            del self.tab_taches[self.tache_id]
            del self.tab_bool[self.tache_id]



        else :
            print(f"ce numero de tache {tach_sp} n'existe pas")

# Affichage  d'une tache en liant les deux dictionaire(teche, booleen) par self.tache.id et en les convertissant en list

    def afficher_tache(self):

        dict_trie1 = {self.tache_id: self.tab_taches[self.tache_id] for self.tache_id in sorted(self.tab_taches)}
        dict_trie2 = {self.tache_id: self.tab_bool[self.tache_id] for self.tache_id in sorted(self.tab_bool)}
        self.tab_taches = {}
        self.tab_bool = {}
        c = 0

        for i, j in dict_trie1.items():
            c += 1
            self.tab_taches[c] = dict_trie1[i]
            self.tab_bool[c] = dict_trie2[i]

        list_tache_key = list(self.tab_taches.keys())
        list_tache_value = list(self.tab_taches.values())
        action = list(self.tab_bool.values())
        # print(list_tache_key)
        # print(list_tache_value)
        # print(action)
        i=1
        for i in self.tab_taches:
            print(f"{list_tache_key[i]} : {list_tache_value[i]} - {action[i]}")


nouvelle_tache = Taches()

kb ="q"

while kb == "q":


    nouvelle_tache.afficher_tache()

    kb = str(input("Entrez une commande (+: Ajouter, -: Terminer, s: Supprimer, a: Afficher, q: Quitter) : "))


    while kb == "+":
        ajout = str(input("entrer le nom de la tache : "))
        nouvelle_tache.ajout_tache(ajout)
        kb = str(input("Ajouter une tache '+': "))
        nouvelle_tache.afficher_tache()



    while kb == "-":
        terminer = int(input("entrer le numero de la tache a terminer : "))
        nouvelle_tache.terminer_tache(terminer)
        kb = str(input("Terminer une tache '-' : "))
        nouvelle_tache.afficher_tache()



    while kb == "s":
        supprime = int(input("entrer le numero de la tache a supprimer : "))
        nouvelle_tache.supprimer_tache(supprime)
        kb = str(input("supprimer une tache 's' : "))
        nouvelle_tache.afficher_tache()



    while kb == "a":
        nouvelle_tache.afficher_tache()
        kb = str(input("supprimer une tache 'a' : "))

    kb = "q"

    print("Merci de votre visite!")






