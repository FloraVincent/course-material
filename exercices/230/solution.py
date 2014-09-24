# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 14:57:49 2014

@author: Flora Vincent
"""
import itertools
import is_prime
import sys

for i in itertools.count(100000000):
    prime = is_prime.is_prime(i)
    if prime is True:
        print(i)
        break
