# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:33:21 2014

@author: Flora Vincent
"""
import operator

a, i = 0, 0
while i <= 100:
    if operator.mod(i, 2) == 0:
        print(i)
        i = i + 1
    else:
        i = i + 1
        # a, i = a + i, i + 1
        # else:
        # i = i + 1
