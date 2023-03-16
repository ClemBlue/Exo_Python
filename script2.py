# --- PARTIE 2 ---
# Créer un script python qui va contenir un dictionnaire (par exemple une personne, avec des attributs comme l'âge, le prénom, le genre...)
# Retourner ce dictionnaire sous forme d'objet JSON dans le terminal (voir le package 'json' pour plus d'info)
# /!\ En POO également, vous devez initialiser le dictionnaire soit dans le constructeur soit avec un setter après instanciation de la classe /!\

import json

class Jason :
    #Le Dictionnaire
    def __init__(self):
        self.personne = {
            'nom' : 'Billy',
            'age' : 42,
            'genre' : 'AH-1 Cobra'
        }

    #Definition du getter
    def get_personne(self):
        return self.personne
    
    #Definition du setter
    def set_personne(self, value):
        self.personne = value

    #Fonction qui convertie en json le dictionnaire
    def getJson(self):
        return json.dumps(self.personne)

newChallenger = Jason()
print(newChallenger.getJson())
