# -*- coding: utf-8 -*-
#####
# Raphael Valois (valr2802)
# Étienne Boutet (boue2327)
###

# Utiliser dbg() pour faire un break dans votre code.
from pdb import set_trace as dbg


#
# AEtoileTuple : Classe représentant un tuple de TaquinEtat, score f et d'un parent
# AEtoileTuple.
#
class AEtoileTuple:

    def __init__(self, etat, f, parent=None):
        self.etat = etat
        self.f = f
        self.parent = parent

    # Fonction de comparaison entre deux AEtoileTuple.
    def __lt__(self, autre):
        return self.f < autre.f

    # Fonctions d'équivalence entre deux AEtoileTuple.
    def __eq__(self, autre):
        return self.etat == autre.etat

    def __ne__(self, autre):
        return not (self == autre)

def construct_path(aEtoileTuple):
    parent = aEtoileTuple.parent
    path = [aEtoileTuple.etat]
    while parent is not None:
        path.append(parent.etat)
        parent = parent.parent

    return path[::-1]

def AEtoile(start, isGoal, transitions, heuristique, cost):
    open = [AEtoileTuple(start, heuristique(start), None)]
    closed = []
    while len(open) > 0:
        aeTuple = open.pop(0)
        closed.append(aeTuple)

        if isGoal(aeTuple.etat):
            return construct_path(aeTuple)

        for transition in transitions(aeTuple.etat):
            transition_cost = cost(aeTuple)
            h = heuristique(transition)
            transition = AEtoileTuple(transition, transition_cost + h, aeTuple)
            if transition in closed or transition in open and transition.f < transition_cost + h:
                continue

            open.append(transition)

        open.sort(key=lambda o: o.f, reverse=False)
    return None


#
# joueur_taquin : Fonction qui calcule le chemin, suite d'états, optimal afin de complété
#                  le puzzle.
#
# etat_depart: Objet de la classe TaquinEtat indiquant l'état initial du jeu.
#
# fct_estEtatFinal: Fonction qui prend en entrée un objet de la classe TaquinEtat et
#                   qui vérifie si l'état passée en paramêtre est l'état final ou non.
#
# fct_transitions: Fonction qui prend en entrée un objet de la classe TaquinEtat et
#                   qui retourne la listes des états voisins pour l'état donné.
#
# fct_heuristique: Fonction qui prend en entrée un objet de la classe TaquinEtat et
#                   qui retourne le coût heuristique pour se rendre à l'état final.
#
# retour: Cette fonction retourne la liste des états de la solution triés en ordre chronologique
#          c'est-à-dire de l'état initial jusqu'à l'état final inclusivement.
#
def joueur_taquin(etat_depart, fct_estEtatFinal, fct_transitions, fct_heuristique):
    def fct_cout(y):
        cost = y.f - fct_heuristique(y.etat)
        return cost + 1

    return AEtoile(etat_depart, fct_estEtatFinal, fct_transitions, fct_heuristique, fct_cout)
