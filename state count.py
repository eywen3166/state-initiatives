# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:43:24 2020

@author: Elaine Wen
"""

import csv

with open('state_initiatives.csv', 'r',
    encoding='utf-8') as datafile:
    reader = csv.reader(datafile)
    state_count = {}
    
    for line in reader:
        
        state = line[0]
        if state not in state_count: 
               state_count[state] = 1
        state_count[state] += 1
    for key in state_count:
        num = state_count[key]
        if key == "States":
            continue
        print(key + ": " + str(num))


            