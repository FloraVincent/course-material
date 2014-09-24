# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 14:49:45 2014

@author: Flora Vincent
"""
import is_prime

listflora = []
for i in range(10000, 10051):
    prime = is_prime.is_prime(i)
    if prime is True:
        listflora.append(i)
print(listflora)
