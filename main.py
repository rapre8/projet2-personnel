class Quoridor:
    def __init__(self, joueurs, murs=None):
        #initialise les variables joueurs et murs
        self.joueurs = joueurs 
        self.murs = murs
        #si chaine de caracteres, on cree un dictionnaire
        if type(self.joueurs) is str:
            joueurs = [{'nom': self.joueurs[0],
            'murs': 10,
            'pos': (5, 1)},
            {'nom': self.joueurs[1],
            'murs': 10,
            'pos': (5, 9)}]
            # si dictionnaire, on affecte les dictionnaires aux joueurs
        if type(self.joueurs) is dict:
            joueur1 = self.joueurs[0]
            joueur2 = self.joueurs[1]
        param_mur = {'horizontaux': [], 'verticaux': []} #dictionnaire des positions de murs. Pour linstant vide car aucun mur sur jeux
        #debut des classes error
        if hasattr(joueurs, '__iter__') is False:
            raise QuoridorError('Objet non itérable')
class QuoridorError(Exception):
    def __init__(self, message):
        super().__init__(message)
