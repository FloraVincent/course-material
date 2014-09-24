# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:33:19 2014

@author: Flora Vincent
"""
import re


def start_with(input, value):
    p = re.compile(value, re.IGNORECASE)
    alpha = p.match(input)
    if alpha is None:
        return False
    else:
        return True
