class Quoridor:
    #erreur si non itérable
    if hasattr(joueurs, '__iter__') is False:
        raise QuoridorError
    #erreur si plus de deux joueurs
    if len(joueurs)>2:
        raise QuoridorError
    #erreur si plus de 10 murs par joueurs ou murs négatif
    for i in range(2):
        if joueurs[i].get('murs')<0 or joueurs[i].get('murs')>10:
            raise QuoridorError
    if joueurs[0].get('pos') != (5, 1) or joueurs[1].get('pos') =! (5, 9):
        raise QuoridorError

    #erreur si position joueur est sur mur horizontal existant.
    for i in range(2):
    for k in range(len(murs.get('horizontaux'))):
        if joueurs[i].get('pos')[1] == murs.get('horizontaux')[k][1]:
            for x in range(3):
                if joueurs[i].get('pos')[0] == murs.get('horizontaux')[k][0] + x:
                    raise QuoridorError
                
    #traitement erreur pour déplacement jeton
    #erreur si déplacement en x et y out of bound
    for i in range(2):
        if joueurs[i].get('pos')[i]<1 or joueurs[i].get('pos')[i]>=10:
            raise QuoridorError
    
class QuoridorError(Exception):
    def __init__(self, message):
        super().__init__(message)
