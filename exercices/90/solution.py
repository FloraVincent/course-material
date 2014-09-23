# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 09:42:37 2014

@author: Flora Vincent
"""
import sys

length = (len(sys.argv))
# print(length)
arguments = list(enumerate(sys.argv))

for i in range(0, length):
    out = str(arguments[i][0]) + str(" ") + str(arguments[i][1])
    print(out)
    # print arguments[i][0], arguments[i][1]
