# --- PARTIE 3 ---
# Créer un script python qui va récupérer les informations systèmes (voir les packages 'platform', 'cpuinfo', 'socket' et 'os' pour plus d'info)
# Avec le moteur de templating jinja, afficher dans un beau template HTML (avec du CSS dans un fichier CSS séparé) ces informations systèmes
# Évidemment, le tout en POO...
# /!\ Je demande pas le site de l'année, mais faites un effort sur le CSS svp /!\

import os
import platform

from flask import Flask
from flask import render_template

class Ninja:
    def __init__(self):
        self.app = Flask(__name__)
        @self.app.route("/")
        def hello():
            return render_template('partie3.html', processor=platform.processor(), system=platform.system())

     #Definition du getter
    def get_app(self):
        return self.app
    
    #Definition du setter
    def set_app(self, value):
        self.app = value

    def run(self):
        self.app.run(debug=True)

xiang = Ninja()
xiang.run()