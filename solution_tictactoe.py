# -*- coding: utf-8 -*-

#####
# Étienne Boutet (boue2327)
# Raphael Valois (valr2802)
###

from pdb import set_trace as dbg  # Utiliser dbg() pour faire un break dans votre code.

import random
import numpy as np


########################
# Solution tic-tac-toe #
########################

#####
# joueur_tictactoe : Fonction qui calcule le prochain coup optimal pour gagner la
#                     la partie de Tic-tac-toe à l'aide d'Alpha-Beta Prunning.
#
# etat: Objet de la classe TicTacToeEtat indiquant l'état actuel du jeu.
#
# fct_but: Fonction qui prend en entrée un objet de la classe TicTacToeEtat et
#          qui retourne le score actuel tu plateau. Si le score est positif, les 'X' ont l'avantage
#          si c'est négatif ce sont les 'O' qui ont l'avantage, si c'est 0 la partie est nulle.
#
# fct_transitions: Fonction qui prend en entrée un objet de la classe TicTacToeEtat et
#                   qui retourne une liste de tuples actions-états voisins pour l'état donné.
#
# str_joueur: String indiquant c'est à qui de jouer : les 'X' ou 'O'.
#
# retour: Cette fonction retourne l'action optimal à joueur pour le joueur actuel c.-à-d. 'str_joueur'.
###

class Alpha_beta_tuple:
    def __init__(self, action, valeur):
        self.action = action
        self.valeur = valeur


def joueur_tictactoe(etat, fct_but, fct_transitions, str_joueur):

    def alpha_beta_pruning(etat, estMaximiseur, alpha, beta):
        if len(fct_transitions(etat)) == 0:
            return Alpha_beta_tuple(None, fct_but(etat))

        if estMaximiseur:
            maxTuple = Alpha_beta_tuple(None, float('-inf'))
            for action, nouvel_etat in fct_transitions(etat).items():
                tuple = Alpha_beta_tuple(action, alpha_beta_pruning(nouvel_etat, False, alpha, beta).valeur)

                if tuple.valeur > maxTuple.valeur:
                    maxTuple = tuple

                alpha = max(alpha, maxTuple.valeur)
                if beta <= alpha:
                    break
            return maxTuple
        else:
            minTuple = Alpha_beta_tuple(None, float('inf'))
            for action, nouvel_etat in fct_transitions(etat).items():
                tuple = Alpha_beta_tuple(action, alpha_beta_pruning(nouvel_etat, True, alpha, beta).valeur)

                if tuple.valeur < minTuple.valeur:
                    minTuple = tuple

                beta = min(beta, minTuple.valeur)
                if beta <= alpha:
                    break
            return minTuple

    if str_joueur == 'X':
        tuple = alpha_beta_pruning(etat, True, float('-inf'), float('inf'))
    else:
        tuple = alpha_beta_pruning(etat, False, float('-inf'), float('inf'))

    return tuple.action
