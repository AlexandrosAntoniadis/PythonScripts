#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:59:23 2017

@author: aantoniadis
"""

import numpy

int_ew

f0 = open('VNstarnames.dat')

string = f0.read()
starlist = []
a = ''
for index,c in enumerate(string):
    if c =='.' and string[index+1] == 'f':
        starlist.append(a)
        a = ''
    elif c == '\n':
        a = ''
    else:
        a += c
        
        
for ind , star in enumerate(starlist):
    string0 = int_ew[ind]
    b = ''
    for val in string0:
        b += str(val)
        b += '\n'
    f = open('/home/aantoniadis/Documents/EWvascoresults/VNresult_'+ star + '.dat','w')
    f.write(b)
    f.close()
    
print starlist