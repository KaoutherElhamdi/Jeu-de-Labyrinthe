# coding=utf-8
""" Ce fichier juste pour alléger le code dans le fichier roboc.py (pour la visibilité c'est tout)"""

from carte import Carte
import os
from fonctions import *


# *******************
def charger_les_cartes_existantes():
    # liste des cartes ( les élèments sont de type : Carte )
    cartes = []
    for nom_fichier in os.listdir("cartes"):
        if nom_fichier.endswith(".txt") and nom_fichier != "partie_sauvegardee.txt":
            chemin = os.path.join("cartes", nom_fichier)
            nom_carte = nom_fichier[:-3].lower()
            with open(chemin, "r") as fichier:
                contenu = fichier.read()

                # création d'une carte
                cartes.append(Carte(nom_carte, contenu))
    return cartes


# *******************


def afficher_les_cartes_existants(cartes):
    print("Labyrinthes existants :")
    for i, carte in enumerate(cartes):
        if carte.nom != "partie_sauvegardee.":
            print("  {} - {}".format(i + 1, carte.nom))


# *******************


def choisir_une_carte(cartes):
    c = "n"
    if "partie_sauvegardee.txt" in os.listdir("cartes"):
        c = partie_sauvegardee_ou_nouvelle()

    if c.lower() == "o":
        print("Partie Sauvegardée")
        # ouvrir la partie_sauvegardee
        chaine = ouvrir_partie("partie_sauvegardee.txt")
        carte = Carte("partie_sauvegardee.", chaine)

    else:
        # supprimer s'il exite un partie sauvegardée
        supprimer_partie_sauvegardee()
        # ouvrir une nouvelle partie
        test = False
        while test == False:
            try:
                c = int(
                    input("Entrez un numéro de labyrinthe pour commencer à jouer : ")
                )
                carte = cartes[c - 1]
                test = True
            except ValueError:
                print("La valeur donnée doit  un entier")
                test = False
            except IndexError:
                print(
                    "le numéro doit être correspondant à l'une des cartes affichées au dessus"
                )
                test = False
    return carte

# TEEEEEST TEST
