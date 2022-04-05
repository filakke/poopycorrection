# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
nbr_personne = 3

list_personne = []

for i in range(nbr_personne):
    
    
    nom = input("Nom de la personne "+ str(i+1) + " : ")
    list_personne.append(Personne(nom))

for personne in list_personne:
    personne.SePresenter()