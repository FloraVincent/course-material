# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:07:00 2014

@author: Flora Vincent
"""
import is_prime

a, i = 0, 0
while i < 100:
    if is_prime.is_prime(i) is True:
        a, i = a + i, i + 1
    else:
        a, i = a, i + 1
print(a)
