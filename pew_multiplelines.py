#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:22:52 2017

@author: aantoniadis
"""

from build_pew_verygeneral import pseudo_EW
import numpy as np

filepaths = np.loadtxt('filelist.dat', dtype=str)

wavelength_range = np.loadtxt('lines.rdb', skiprows=2)
dw = 0.4
plot = False


for i in np.arange(len(filepaths)):
    output = np.empty(len(wavelength_range))    
    for j in np.arange(len(wavelength_range)):
        output[j] = pseudo_EW(fname=filepaths[i], w1=wavelength_range[j,0], w2=wavelength_range[j,1], dw=dw, plot=plot)
    np.savetxt('./EWmyresults/result_'+filepaths[i].replace('.fits','.dat').replace('spectra/HARPS/',''), output, fmt='%.2f')
