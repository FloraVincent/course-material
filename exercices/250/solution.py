# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:38:58 2014

@author: Flora Vincent
"""

# build squares


def draw_n_squares(m):
    n = m
    Matrix = [[0 for x in range((4*n+1))] for x in range((2*n+1))]
    for i in range(0, (2*n + 1)):
        if (i % 2) == 0:  # si la ligne est paire
            for j in range(0, (4*n + 1)):
                if (j % 4) == 0:  # si la colonne est un multiple de 4
                    Matrix[i][j] = "+"
                else:
                    Matrix[i][j] = "-"
        else:
            for j in range(0, (4*n + 1)):
                if (j % 4) == 0:
                    Matrix[i][j] = "|"
                else:
                    Matrix[i][j] = " "
    for mat in Matrix:
        result = print("".join(map(str, mat)))
    return result
