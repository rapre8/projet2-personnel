import networkx as nx



class Quoridor:

    def __init__(self, joueurs, murs=None):
        self.joueur1 = joueurs[0]
        self.joueur2 = joueurs[1]
        self.murs = murs
        if str(self.joueur1) == self.joueur1:
            self.gamestate = {'joueurs':
                            [{'nom': self.joueur1, 'murs': 10, 'pos': [5, 1]},
                            {'nom': self.joueur2, 'murs': 10, 'pos': [5, 9]}],
                            'murs': {'horizontaux': [], 'verticaux': []}}
        else:
                self.gamestate = {'joueurs':
                                [self.joueur1, self.joueur2],
                                'murs': {'horizontaux': [], 'verticaux': []}}
        if type(self.murs) == dict:
                self.gamestate['murs'] = self.murs
        

        """
        :raises QuoridorError: si joueurs n'est pas itérable.
        :raises QuoridorError: si l'itérable de joueurs en contient plus de deux.
        :raises QuoridorError: si le nombre de murs qu'un joueur peut placer est >10, ou négatif.
        :raises QuoridorError: si la position d'un joueur est invalide.
        :raises QuoridorError: si murs n'est pas un dictionnaire lorsque présent.
        :raises QuoridorError: si le total des murs placés et plaçables n'est pas égal à 20.
        :raises QuoridorError: si la position d'un mur est invalide.
        """
        

    def __str__(self):
        
        haut = f'Légende: 1={self.gamestate["joueurs"][0]["nom"]}, 2={self.gamestate["joueurs"][1]["nom"]}\n'
        haut += '   -----------------------------------\n'
        bas = '--|-----------------------------------\n'
        bas += '  | 1   2   3   4   5   6   7   8   9'
        liste_vide = []
        for i in range(18,1,-1):
            style_damier_1 = list(f"{i//2} | .   .   .   .   .   .   .   .   . |")
            style_damier_2 = list("  |                                   |")
            if i%2 == 0:
                liste_vide.append(style_damier_1)
            else:
                liste_vide.append(style_damier_2)   
        for i in range(2):
            liste_vide[18-2*self.gamestate["joueurs"][i]["pos"][1]][4*self.gamestate["joueurs"][i]["pos"][0]] = f'{i+1}'
        for i in range(len(self.gamestate["murs"]["horizontaux"])):
            for j in range(7):
                liste_vide[19-2*self.gamestate["murs"]["horizontaux"][i][1]][4*self.gamestate["murs"]["horizontaux"][i][0]+j-1] = '-'
        for i in range(len(self.gamestate["murs"]["verticaux"])):
            for j in range(3):
                liste_vide[18-2*self.gamestate["murs"]["verticaux"][i][1]-j][4*self.gamestate["murs"]["verticaux"][i][0]-2] = '|'
        damier = []
        for ligne in liste_vide:
            damier += ligne + ['\n']
        a = ''.join(damier)
        
        return haut + a + bas

    def déplacer_jeton(self, joueur, position):

        self.nouvelle_position = list(position)
        self.gamestate['joueurs'][joueur - 1]['pos'] = self.nouvelle_position

        """
        :param joueur: un entier spécifiant le numéro du joueur (1 ou 2).
        :param position: le tuple (x, y) de la position du jeton (1<=x<=9 et 1<=y<=9).
        :raises QuoridorError: le numéro du joueur est autre que 1 ou 2.
        :raises QuoridorError: la position est invalide (en dehors du damier).
        :raises QuoridorError: la position est invalide pour l'état actuel du jeu.
        """

    def état_partie(self):
        
        return self.gamestate

    def jouer_coup(self, joueur):

        """
        Pour le joueur spécifié, jouer automatiquement son meilleur coup pour l'état actuel 
        de la partie. Ce coup est soit le déplacement de son jeton, soit le placement d'un 
        mur horizontal ou vertical.

        :param joueur: un entier spécifiant le numéro du joueur (1 ou 2).
        :raises QuoridorError: le numéro du joueur est autre que 1 ou 2.
        :raises QuoridorError: la partie est déjà terminée.
        """

    def partie_terminée(self):
        
        if self.gamestate['joueurs'][0]['pos'] == [5, 9]:
            return self.gamestate['joueurs'][0]["nom"]
        if self.gamestate['joueurs'][1]['pos'] == [5, 1]:
            return self.gamestate['joueurs'][1]["nom"]
        else:
            return False
        
        """
        Déterminer si la partie est terminée.

        :returns: le nom du gagnant si la partie est terminée; False autrement.
        """

    def placer_mur(self, joueur: int, position: tuple, orientation: str):
        """
        Pour le joueur spécifié, placer un mur à la position spécifiée.

        :param joueur: le numéro du joueur (1 ou 2).
        :param position: le tuple (x, y) de la position du mur.
        :param orientation: l'orientation du mur ('horizontal' ou 'vertical').
        :raises QuoridorError: le numéro du joueur est autre que 1 ou 2.
        :raises QuoridorError: un mur occupe déjà cette position.
        :raises QuoridorError: la position est invalide pour cette orientation.
        :raises QuoridorError: le joueur a déjà placé tous ses murs.
        """
a = Quoridor([{'nom': 'raphael', 'murs': 3, 'pos': [5, 3]},
              {'nom': 'jean-guy', 'murs': 6, 'pos': [5, 5]}], {'horizontaux': [(5, 7)], 'verticaux': [(6,3)]}
             )

print(a.état_partie())
a.déplacer_jeton(1, (5,9))
print(a)
if a.partie_terminée() != None:
    print(a.partie_terminée())