import networkx as nx


class QuoridorError(Exception):
    pass


# FONCTION FOURNIE
def construire_graphe(joueurs, murs_horizontaux, murs_verticaux):
    """
    Crée le graphe des déplacements admissibles pour les joueurs.

    :param joueurs: une liste des positions (x,y) des joueurs.
    :param murs_horizontaux: une liste des positions (x,y) des murs horizontaux.
    :param murs_verticaux: une liste des positions (x,y) des murs verticaux.
    :returns: le graphe bidirectionnel (en networkX) des déplacements admissibles.
    """
    graphe = nx.DiGraph()

    # pour chaque colonne du damier
    for x in range(1, 10):
        # pour chaque ligne du damier
        for y in range(1, 10):
            # ajouter les arcs de tous les déplacements possibles pour cette tuile
            if x > 1:
                graphe.add_edge((x, y), (x-1, y))
            if x < 9:
                graphe.add_edge((x, y), (x+1, y))
            if y > 1:
                graphe.add_edge((x, y), (x, y-1))
            if y < 9:
                graphe.add_edge((x, y), (x, y+1))

    # retirer tous les arcs qui croisent les murs horizontaux
    for x, y in murs_horizontaux:
        graphe.remove_edge((x, y-1), (x, y))
        graphe.remove_edge((x, y), (x, y-1))
        graphe.remove_edge((x+1, y-1), (x+1, y))
        graphe.remove_edge((x+1, y), (x+1, y-1))

    # retirer tous les arcs qui croisent les murs verticaux
    for x, y in murs_verticaux:
        graphe.remove_edge((x-1, y), (x, y))
        graphe.remove_edge((x, y), (x-1, y))
        graphe.remove_edge((x-1, y+1), (x, y+1))
        graphe.remove_edge((x, y+1), (x-1, y+1))

    # retirer tous les arcs qui pointent vers les positions des joueurs
    # et ajouter les sauts en ligne droite ou en diagonale, selon le cas
    for joueur in map(tuple, joueurs):

        for prédécesseur in list(graphe.predecessors(joueur)):
            graphe.remove_edge(prédécesseur, joueur)

            # si admissible, ajouter un lien sauteur
            successeur = (2*joueur[0]-prédécesseur[0], 2*joueur[1]-prédécesseur[1])

            if successeur in graphe.successors(joueur) and successeur not in joueurs:
                # ajouter un saut en ligne droite
                graphe.add_edge(prédécesseur, successeur)

            else:
                # ajouter les liens en diagonal
                for successeur in list(graphe.successors(joueur)):
                    if prédécesseur != successeur and successeur not in joueurs:
                        graphe.add_edge(prédécesseur, successeur)

    # ajouter les noeuds objectifs des deux joueurs
    for x in range(1, 10):
        graphe.add_edge((x, 9), 'B1')
        graphe.add_edge((x, 1), 'B2')

    return graphe  
# FIN DE LA FONCTION FOURNIE

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

        if joueur != 1:
            if joueur != 2:
                raise QuoridorError('le numéro du joueur doit être 1 ou 2')

        if position[0] > 9 or position[0] < 1 or position[1] > 9 or position[1] < 1:
                    raise QuoridorError('la position est invalide (en dehors du damier)')

        graphe = construire_graphe(
        [joueur['pos'] for joueur in self.gamestate['joueurs']], 
        self.gamestate['murs']['horizontaux'],
        self.gamestate['murs']['verticaux'])
        self.nouvelle_position = list(position) 

        if position not in list(graphe.successors((5,6))):
                    raise QuoridorError("la position est invalide pour l'état actuel du jeu.")
       
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

        if self.partie_terminée() != False:
            raise QuoridorError('La partie est déjà terminée')

        if joueur != 1:
            if  joueur != 2:
                raise QuoridorError('le numéro du joueur doit être 1 ou 2')

        graphe = construire_graphe(
        [joueur['pos'] for joueur in self.gamestate['joueurs']], 
        self.gamestate['murs']['horizontaux'],
        self.gamestate['murs']['verticaux'])

        position_a_aller = nx.shortest_path(
            graphe,
            tuple(self.gamestate['joueurs'][joueur - 1]['pos']), f'B{joueur}')

        self.déplacer_jeton(joueur, position_a_aller[1])

        

        

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
        
        if joueur != 1:
            if joueur != 2:
                raise QuoridorError('le numéro du joueur doit être 1 ou 2')

        
        if self.gamestate['joueurs'][joueur-1]['murs'] == 0:
            raise QuoridorError('le joueur a déjà placé tout ses murs.')

        self.gamestate['joueurs'][joueur-1]['murs'] = self.gamestate['joueurs'][joueur-1]['murs']-1
        if orientation == 'horizontal':
            self.gamestate['murs']['horizontaux'].append(position)
        if orientation == 'vertical':
            self.gamestate['murs']['verticaux'].append(position)

        

        
        """
        Pour le joueur spécifié, placer un mur à la position spécifiée.

        :param joueur: le numéro du joueur (1 ou 2).
        :param position: le tuple (x, y) de la position du mur.
        :param orientation: l'orientation du mur ('horizontal' ou 'vertical').
        :raises QuoridorError: le numéro du joueur est autre que 1 ou 2.
        ##:raises QuoridorError: un mur occupe déjà cette position.
        ##:raises QuoridorError: la position est invalide pour cette orientation.
        :raises QuoridorError: le joueur a déjà placé tous ses murs.
        """

a = Quoridor([{'nom': 'Dude', 'murs': 0, 'pos': [2, 2]},{'nom': 'Dudesse', 'murs': 9, 'pos': [5, 6]}],
                             {'horizontaux': [], 'verticaux': [(5,5)]})

print(a)
a.placer_mur(2, (7,7), 'vertical')
