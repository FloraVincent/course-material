# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:07:00 2014

@author: Flora Vincent
"""
import is_prime

a, i = 0, 0
while i < 10:
    prime = is_prime.is_prime(i)
    if prime is True:
        a, i = a + i, i + 1
    else:
        i = i + 1
print(a)
