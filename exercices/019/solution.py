# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:02:54 2014

@author: Flora Vincent
"""


import sys

if len(sys.argv) == 1:
    print("usage: python3 solution.py OP1 OP2")
else:
    print(int(sys.argv[1]) + int(sys.argv[2]))
