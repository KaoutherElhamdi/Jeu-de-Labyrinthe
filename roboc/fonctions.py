import os
from carte import *


def verifier_le_mouvement(mvt, d, position, max_ligne, max_colonne):
    """fonction retourne un booléen si :
    True: le mouvement est possible
    False: Le mouvement est impossible"""

    if len(mvt) == 1:
        if mvt.upper() not in ["N", "E", "S", "O"]:
            return False
        else:
            nb = 1
    else:
        if mvt[0].upper() not in ["N", "E", "S", "O"]:
            return False
        else:
            nb = int(mvt[1:])

    if mvt[0].upper() == "N":
        if nb > position[0]:
            return False
        else:
            i = position[0] - 1
            nb -= 1
            while nb >= 0:
                if d[(i, position[1])].nature == "O":
                    return False
                else:
                    i -= 1
                    nb -= 1
            return True

    if mvt[0].upper() == "S":
        if nb > max_ligne - position[0]:
            return False
        else:
            i = position[0] + 1
            nb -= 1
            while nb >= 0:
                if d[(i, position[1])].nature == "O":
                    return False
                else:
                    i += 1
                    nb -= 1
            return True

    if mvt[0].upper() == "O":
        if nb > position[1]:
            return False
        else:
            i = position[1] - 1
            nb -= 1
            while nb >= 0:
                if d[(position[0], i)].nature == "O":
                    return False
                else:
                    i -= 1
                    nb -= 1
            return True

    if mvt[0].upper() == "E":
        if nb > max_colonne - position[1]:
            return False
        else:
            i = position[1] + 1
            nb -= 1
            while nb >= 0:
                if d[(position[0], i)].nature == "O":
                    return False
                else:
                    i += 1
                    nb -= 1
            return True


# *****************************************


def faire_le_mouvement(mvt, carte):
    position = carte.position_du_robot
    carte.labyrinthe.grille[position].robot = False
    if len(mvt) == 1:
        nb = 1
    else:
        nb = int(mvt[1:])

    nouvelle_position = position
    if mvt[0].upper() == "N":
        nouvelle_position = position[0] - nb, position[1]
    if mvt[0].upper() == "S":
        nouvelle_position = position[0] + nb, position[1]
    if mvt[0].upper() == "E":
        nouvelle_position = position[0], position[1] + nb
    if mvt[0].upper() == "O":
        nouvelle_position = position[0], position[1] - nb

    carte.labyrinthe.grille[nouvelle_position].robot = True
    carte.position_du_robot = nouvelle_position
    return carte


# *****************************************
def verifier_l_entree(entree):
    """Vérifier si l'entree saisie égale soit à :
    q : pour quitter la partie
    mouvement : pour faire un mouvement (doit étre sous la forme lettre appartient à [E/e,O/o,S/s,N/n] seule
    ou suivie par le nombre de sauts à faire"""
    if entree == "":
        return False
    if len(entree) == 1:
        if entree.lower() in ["e", "s", "n", "o", "q"]:
            return True
        else:
            return False
    else:
        if entree[0].lower() not in ["e", "s", "n", "o"]:
            return False
        else:
            try:
                int(entree[1:])
            except:
                return False
            else:
                return True


# *****************************************


def partie_sauvegardee_ou_nouvelle():
    print("\n Il y a une partie déjà sauvegardée. Voulez-vous continuer ?\n")
    c = input(
        "Cliquer sur (o ou O) : pour continuer à jouer la partie sauvegardée\nou cliquer sur (n ou N): pour commencer une nouvelle partie\n===>  "
    )
    while c.lower() not in ["o", "n"]:
        c = input("\no/O : continuer \nn/N : nouvelle partie\n===>    ")
    return c


# *****************************************


def sauvegarger_automatiquement_la_partie(carte):
    """ Une fonction pour le sauvegard automatique du partie aprés chaque mouvement """
    with open(os.path.join("cartes", "partie_sauvegardee.txt"), "w") as f:
        chaine = str(carte)
        f.write(chaine)


# *****************************************


def ouvrir_partie(nom_carte):
    with open(os.path.join("cartes", nom_carte), "r") as f:
        chaine = f.read()
        return chaine


# *****************************************


def supprimer_partie_sauvegardee():
    if "partie_sauvegardee.txt" in os.listdir("cartes"):
        os.remove(os.path.join("cartes", "partie_sauvegardee.txt"))


# *****************************************


def gagner():
    print("Félicitations ! Vous avez gagné !")
    supprimer_partie_sauvegardee()
