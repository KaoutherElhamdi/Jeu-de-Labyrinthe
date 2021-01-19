# -*-coding:Utf-8 -*

from case import Case
from labyrinthe import Labyrinthe

"""Ce module contient la classe Carte."""


class Carte:

    """Objet de transition entre un fichier et un labyrinthe.
    -nom : nom du carte
    -labyrinthe : labyrinthe associé
    -position_du_robot : la position où se trouve notre robot"""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe, self.position_du_robot = creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def __str__(self):
        return str(self.labyrinthe)


# *****************************************************


def creer_labyrinthe_depuis_chaine(chaine):
    position_du_robot = (0, 0)
    lab = Labyrinthe()
    lignes = chaine.split("\n")
    for i, ligne in enumerate(lignes):
        for j, c in enumerate(ligne):
            if c == lab.get_robot():
                case = Case(nature=" ", robot=True)
                position_du_robot = (i, j)
            else:
                case = Case(nature=c, robot=False)
            lab.insert_une_case((i, j), case)
    return lab, position_du_robot
