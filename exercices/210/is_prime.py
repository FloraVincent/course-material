# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:08:22 2014

@author: Flora Vincent
"""


def is_prime(num):
    if num > 2:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:   # attention le else doit etre en DEHORS de la boucle!
            return True
    elif num == 2:
        return True
    else:
        return False
