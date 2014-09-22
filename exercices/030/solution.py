# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:33:21 2014

@author: Flora Vincent
"""
import operator

for i in list(range(100)):
    if operator.mod(i, 2) == 0:
        print(i)
