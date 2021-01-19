class Case:
    """
    - ligne : la ligne où se trouve la case en question
    - colonne
    - nature : la nature du case (mur , point , port)
    - robot : booléen qui indique si le robot se trouve à cette case ou non
    """

    def __init__(self, nature, robot):
        self.nature = nature
        self.robot = robot

    """def robot_existe(self):
        return self.robot==True

    def robot_quitte(self):
        self.robot=False
        
    def rencontre_un_mur(self):
        try:
            assert not Case.est_un_mur(self)
            self.robot=True
        except AssertionError :
            print("Désolé !! Il s'agit d'un mur")

    def est_la_sortie(self):
        return self.nature=="U"

    def est_un_mur(self,mur="O"):
        return self.nature==mur    
    def est_une_porte(self):
        return self.nature=="."
        """

    def il_y_a_robot(self):
        return self.robot == True

    def __str__(self):
        if self.robot == True:
            return "X"
        else:
            return self.nature


# { (ligne,colonne):case(nature,robot)}
