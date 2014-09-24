# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:08:22 2014

@author: Flora Vincent
"""


def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print("FALSE")
                break  # break stops the loop after the first FALSE
            else:
                print("TRUE")
                break  # break stop the loop after the first TRUE
    else:
        print("FALSE")
