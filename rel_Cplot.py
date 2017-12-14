#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 18:05:48 2017

@author: aantoniadis
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

df1 = pd.read_csv("rel_tableCD.dat")

df2 = pd.read_csv("statistical_study.csv")


df3 = df1[df2["star"]]

for i in range(len(df1["central_lines"])):
   
    set_res = 12
    plt.plot(df2['teff'],np.array(df3.iloc[[i]]).T, '.')
    
    plt.title("line"+" "+str(np.array(df1['central_lines'].iloc[[i]])), fontsize=set_res)
    
    plt.xlabel("Teff", fontsize=set_res)
    plt.ylabel("% EW difference", fontsize=set_res)
    plt.savefig('./rel_C_diagrams/'+str(np.array(df1['central_lines'].iloc[[i]])).replace('[','').replace(']','')+'.png')
    plt.close()
