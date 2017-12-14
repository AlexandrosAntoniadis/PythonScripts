#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:01:17 2017

@author: aantoniadis
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

df1 = pd.read_csv("rel_tableCD.dat")

df2 = pd.read_csv("statistical_study.csv")


df3 = df1[df2["star"]]




for i in range(len(df2["star"])):
    
    plt.plot(df2['teff'].iloc[[i]],np.nanmean(df3.iloc[[i]]), 'k.')

set_res = 12

plt.title("EW relative mean difference VS Teff", fontsize=set_res*1.5)
    

plt.ylabel("EW mean difference %", fontsize=set_res)
plt.xlabel("Teff", fontsize=set_res)

plt.savefig('relativemeandiff_VS_Teff'+'.png')
plt.show()
