# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 09:28:33 2014

@author: Flora Vincent
"""
import math
import numpy as np


def euclidean(a, b):
    result = 0
    squares = 0
    # Check nature of a and b
    if type(a) != int:
        print("'a' is not a number!")
    elif type(b) != int:
        print("'b' is not a number!")
    elif len(a) != len(b):
        print("'a' and 'b' are NOT the same length!")
    else:
        print("Cool, 'a' and 'b' are numbers :) ")
    # Discriminate simple int from lists
    if (len(a) & len(b)) == 1:
        result = pow(pow(a-b, 2), 0.5)
        return result
    else:
        for i in range(0, len(a)):
            squares = squares + pow(a[i]-b[i], 2)  # making the sum of squares
    result = pow(squares, 0.5)
    return result


def opt_euclidean(a, b):
    result = 0
    squares = 0
    # Discriminate simple int from lists
    if (len(a) & len(b)) == 1:
        result = math.sqrt(math.pow(a-b, 2))
        return result
    else:
        for i in range(0, len(a)):
            squares = squares + math.pow(a[i]-b[i], 2)
            # making the sum of squares
    result = math.pow(squares, 0.5)
    return result


def np_euclidean(a, b):
    c = 0
    result = 0
    c = np.array([a, b])  # transform my matrix in array!
    result = pow(np.sum(pow(c[1] - c[0], 2)), 0.5)
    return result
