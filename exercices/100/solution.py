# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 10:18:25 2014

@author: Flora Vincent
"""
station = {
    'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
    'number': 31705,
    'latitude': 48.8645278209514,
    'name': 'CHAMPEAUX (BAGNOLET)',
    'longitude': 2.416170724425901
}

length = len(list(station.items()))


for i in range(0, length):
    out = str(list(station.items())[i][0]) + str(" ") + str(list(station.items())[i][1])
    print(out)
