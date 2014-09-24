# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 10:26:37 2014

@author: Flora Vincent
"""
import re

p = re.compile('[a-z]', re.IGNORECASE)  # First I create my reg exp


def is_alpha(input):
    alpha = p.search(input)  # do NOT at the print! alpha STORES the value!
    if alpha is not None:
        return True
    else:
        return False
