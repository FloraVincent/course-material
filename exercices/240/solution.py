# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:03:56 2014

@author: Flora Vincent
"""
# liste de Fibonacci
import itertools
suite = [1, 2]

for i in itertools.count(2):
    if len(suite) < 10:
        new = suite[i-2] + suite[i-1]
        suite.append(new)
    else:
        break
print(', '.join(map(str, suite)) + ".")
