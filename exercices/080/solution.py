# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:21:19 2014

@author: Flora Vincent
"""

u = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
v = []
for i in u:
    for j in u:
        new = i + j
        combi = j + i
        if i != j:
            if combi not in v:
                v.append(new)
                print(new)
