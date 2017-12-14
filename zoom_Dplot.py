#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 14:04:19 2017

@author: aantoniadis
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

df1 = pd.read_csv("tableCD.dat")

df2 = pd.read_csv("statistical_study.csv")


df3 = df1[df2["star"]]




for i in range(len(df1["central_lines"])):
    
    plt.plot(df1['central_lines'].iloc[[i]],np.nanmean(df3.iloc[[i]]), '.')

set_res = 12

plt.title("EW mean differences according to each line", fontsize=set_res)
plt.ylim(-20,20) 
plt.xlabel("absorption lines [$\AA$]", fontsize=set_res)
plt.ylabel("EW mean difference", fontsize=set_res)
plt.show() 
plt.savefig('zoom_Dplot'+'.png')
