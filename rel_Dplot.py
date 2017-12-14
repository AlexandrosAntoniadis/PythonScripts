#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 18:00:36 2017

@author: aantoniadis
"""


import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

df1 = pd.read_csv("rel_tableCD.dat")

df2 = pd.read_csv("statistical_study.csv")


df3 = df1[df2["star"]]


#    plt.savefig('./C_diagrams/'+str(np.array(df1['central_lines'].iloc[[i]])))
#df3 = df2.sort_index(axis=1, by=df1.columns.values[1::])
#print(df2)
#print(df3)

for i in range(len(df1["central_lines"])):
   
    plt.plot(df1['central_lines'].iloc[[i]],np.nanmean(df3.iloc[[i]]), '.')

set_res = 12

plt.title("EW relative mean differences according to each line", fontsize=set_res)
    
plt.xlabel("absorption lines [$\AA$]", fontsize=set_res)
plt.ylabel("EW mean difference %", fontsize=set_res)
   
plt.savefig('rel_Dplot'+'.png')
plt.close()
