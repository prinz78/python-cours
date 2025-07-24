

#LES FONCTIONS

# Declaration d'une fonction

def ma_fonction1():
    print (f"je suis le corp de la fonction")

# Fonction avec Argument pour calculer un cercle par exemple

def calcule_air(air:int):
    print(f"l'air du cercle est : {3.14*air**2}")

# Declaration de fonction avec Argument nome, exemple temperature

def message_temperature(prenom, temperature):
    print(f"Bonjour {prenom}")
    print(f"La temperature est de {temperature}")

# Exercice Conversion unite

def conversion_distance(distance,unite):
    taux_de_conversion = {"km": 0.001,"hm": 0.01,"dam": 0.1,
                          "m": 1,"dec": 10,"cm": 100,
                          "mm": 1000}
    if unite in taux_de_conversion:
        resultat = distance*taux_de_conversion[unite]
        print(f"Conversion: {distance} m = {resultat} {unite}")
    else :
        print("Unite invalide")

# Fonction avec instruction return qui permet de retourner une variable apres son traitement

def calcule_carre(nombre:int):
    nombre*=nombre
    return nombre

# Argument parr deffaut dans une fonction

def arg_deffaut(prenom="Mouloud", age=22):
    print(f"prenom est {prenom} mon age est {age}")

# Exercice nombre de mot dans une phrase

def nombre_mot_dans_une_phrase(texte:str):
    tab_mot = texte.split()
    return len(tab_mot)

# Fonctions anonymes : ce sont des fonctions avec le mor cle lambda qui sert a cree des fonction courte en ecriture

ajout = lambda a,b : a+b
multp = lambda a,b : a*b

# Arguments arbitraire sont les argument utiliser dans une fonction qui ne sont pas limite on les declare avec un asterix *

def fonction_argument_arbitraire(*arguments_sans_limite):
    print(f"le nombre d'argument est {len(arguments_sans_limite)}")

# Arguments arbitraire sont les argument utiliser dans une fonction qui ne sont pas limite avec des parametres on les declare avec deux asterix **

def fonction_argument_arbitraire_avec_parametre(**arguments_sans_limite):
    print(f"le nombre d'argument est {len(arguments_sans_limite)}")


# on peut utiliser la Methode du docstring pour documenter les fonctions souhaite

def calcule_air(air:int):
    """Permet de calculer un rayon en (m)"""
    print(f"l'air du cercle est : {3.14*air**2}")


#######################------------------------------------------------------------------####################################################################

ma_fonction1()

calcule_air(10)

message_temperature(prenom="Mouloud",temperature=45)

# Exercice Conversion unite

distance = int(input("entrer la distance en (m) : "))
unite = str(input("entre l'unite (km, cm ou mm) : "))

conversion_distance(distance=distance, unite=unite)

# fonction avec return

nbr= int(input("entrer le nombre a metre au carre: "))
carre = calcule_carre(nbr)

print(f"le carre de {nbr} est {carre}")

# Argument parr deffaut dans une fonction

arg_deffaut()

# Exercice nombre de mot dans une phrase

phrase = str(input("entrer votre phrase pour compter les mots : "))

nbr_mot = nombre_mot_dans_une_phrase(phrase)

print(f"le nombre de mot dans la phrase est {nbr_mot}")

# Fonctions anonymes : ce sont des fonctions avec le mor cle lambda qui sert a cree des fonction courte en ecriture

print(f"Resultat fonction lambda ajout : {ajout(4,6)}")

print(f"Resultat fonction lambda multip : {multp(4,6)}")

# Arguments arbitraire sont les argument utiliser dans une fonction qui ne sont pas limite on les declare avec un asterix *

fonction_argument_arbitraire("mouloud","nadya","mimou","zizou","gatita")

fonction_argument_arbitraire_avec_parametre(bn1=22,bn2=22,bn3=22,bn4=58,bn5=22,bn6=22,bn7=22)

print(calcule_air(50).__doc__)