import logging
import os
from flask import Flask, render_template, request, redirect, url_for
from jeu import Jeu
from joueur import Joueur

app = Flask(__name__)
app.debug = True

jeu = Jeu()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/partie-de-fou")
def partie_de_fou():
    return render_template('partie.html')


@app.route('/joueurs', methods=['POST'])
def creer_joueur():
    joueur = Joueur(request.form['nom_joueur'])
    jeu.ajoute_des_joueurs([joueur])
    return redirect('partie-de-fou')


if __name__ == "__main__":
    app.run()
