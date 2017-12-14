#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:01:38 2017

@author: aantoniadis
"""

# open and plot data from a csv file

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("statistical_study.csv")

set_res = 12

plt.title("EW mean difference VS Teff", fontsize=set_res*2)
    # set axis labels
plt.ylabel("EW mean difference", fontsize=set_res)
plt.xlabel("Teff", fontsize=set_res)
    
plt.plot(df["teff"],df["dif_average"], 'k.')
plt.show()
plt.savefig('meandiff_VS_Teff'+'.png')
