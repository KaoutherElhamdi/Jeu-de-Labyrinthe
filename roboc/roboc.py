# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte
from fonctions import *
from roboc_details import *
from labyrinthe import max_colonne,max_ligne

# On charge les cartes existantes
cartes = charger_les_cartes_existantes()
print()

# On affiche les cartes existantes
afficher_les_cartes_existants(cartes)
print()

#choisir une carte pour jouer      
carte=choisir_une_carte(cartes)
print()

print()
print(carte)
    
sauvegarger_automatiquement_la_partie(carte)
# ... Le jeu se commence ...

while True :

    while True :
        c=input(">\t")
        if verifier_l_entree(c)==True :
            break
        else :
            print("Vérifier votre saisie")
    
    if c=="q" :
        print("Partie bien sauvegardée")
        break
    else :
        test=verifier_le_mouvement(c,carte.labyrinthe.grille,carte.position_du_robot,max_ligne(carte.labyrinthe.grille),max_colonne(carte.labyrinthe.grille))
        if test==False :
            print("Faux Mouvement!!\n ")
        else:
            carte=faire_le_mouvement(c,carte)
        sauvegarger_automatiquement_la_partie(carte)
        print(carte)
    if carte.labyrinthe.grille[carte.position_du_robot].nature==carte.labyrinthe.point_de_quitte :
        gagner()
        break
    
    

