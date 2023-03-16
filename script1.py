# ÉNONCÉ
# --- PARTIE 1 ---
# Créer un script python qui va afficher dans le terminal une phrase aléatoire,
# venant d'un tableau que vous aurez préalablement rempli de quelques citations par exemple
# /!\ En POO même s'il y a peu d'attributs/getters/setters à faire /!\

import random

class Blabla :
    #Tout le blabla de Teemo
    def __init__(self):
        self.text = [
            "Captain Teemo on duty.",
            "Yes, sir!",
            "Armed and ready.",
            "Reporting in.",
            "Hut, two, three, four.",
            "I'll scout ahead!",
            "Never underestimate the power of the Scout's code.",
            "Size doesn't mean everything."
        ]
    
    #Definition du getter
    def get_text(self):
        return self.text
    
    #Definition du setter
    def set_text(self, value):
        self.text = value

    #fonction donnant un text aléatoire
    def randomText(self):
        index = random.randint(0, len(self.text)-1)
        return self.text[index]

#Création nouvelle instance
teemo = Blabla()
#Affichage
print(teemo.randomText())
