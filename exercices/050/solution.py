# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 17:37:17 2014

@author: Flora Vincent
"""
import operator

a, i = 0, 0
while i <= 10:
    if operator.mod(i, 3) == 0 | operator.mod(i, 5) == 0:
        a, i = a + i, i + 1
    else:
        i = i + 1
print(a)
