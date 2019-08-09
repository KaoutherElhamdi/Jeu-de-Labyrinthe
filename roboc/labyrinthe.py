# -*-coding:Utf-8 -*

#from fonctions import max_ligne , max_colonne

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, robot="X", obstacles="O",espaces=" ",porte=".",point_de_quitte="U"):
        self.robot = robot
        self.obstacle=obstacles
        self.espace=espaces
        self.porte=porte
        self.point_de_quitte=point_de_quitte
        self.grille = {}

    def insert_une_case(self,position,case):
        #position : tuple (ligne,colonne)
        #case : de type Case
        self.grille[position]=case
        
    def get_robot(self):
        return self.robot

    def __str__(self):
        chaine= ""
        if self.grille != {}:
            max_ligne_labyrinthe=max_ligne(self.grille)
            max_colonne_labyrinthe=max_colonne(self.grille)
            for i in range(max_ligne_labyrinthe+1):
                for j in range(max_colonne_labyrinthe+1):
                    case=self.grille[(i,j)]
                    if case.il_y_a_robot():
                        chaine = chaine + self.robot
                    else:
                        chaine = chaine + str(case)
                chaine = chaine + "\n"
        return chaine




#******************************************************************
def max_ligne(d):
    l=[cle[0] for cle in d.keys()]
    l.sort()
    return l[-1]

def max_colonne(d):
    l=[cle[1] for cle in d.keys()]
    l.sort()
    return l[-1]
