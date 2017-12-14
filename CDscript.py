#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:58:51 2017
@author: aantoniadis
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

def Load_Data_Pairs(data1, data2):
    
    # Get the data and the names from our results
    our_datanames = []
    our_data = []
    for file in os.listdir(data1):
        # get all .dat files
        if file.endswith(".dat"):
            temp_name = os.path.join(data1, file)
            # remove unwanded elements and append the names
            our_datanames.append(temp_name.split('/')[1].strip( '.dat' ))
            # append data
            our_data.append(np.loadtxt(temp_name))
    
    # Get the data and the names from VN results
    VN_datanames = []
    VN_data = []
    for file in os.listdir(data2):
        # get all .dat files
        if file.endswith(".dat"):
            temp_name = os.path.join(data2, file)
            # remove unwanded elements and append the names
            VN_datanames.append(temp_name.split('/')[1].strip( '.dat' ))
            # append data
            VN_data.append(np.loadtxt(temp_name))
    
    # create our results and VN results pairs
    VN_Pairs = []   
    VN_PairsNames = []     
    for names in our_datanames:
        # find index for the same result pairs and append
        pair_idx = [i for i, s in enumerate(VN_datanames) if names in s][0]
        VN_Pairs.append(VN_data[pair_idx])
        VN_PairsNames.append(VN_datanames[pair_idx])
        
    return our_data, VN_Pairs, our_datanames, VN_PairsNames



def main():
    
    # Define folder names for my data and the given ones
    myData = "EWmyresults"
    GivenData = "EWvascoresults"
    #os.remove("stat_val.dat")
    # Load data and return the pairs
    our_data, VN_Pairs, our_datanames, VN_PairsNames = Load_Data_Pairs(myData, GivenData)
    
    # If these is not a 'results' directory create one
    #if not os.path.exists('ew_diff_cor_results'):
        #os.makedirs('ew_diff_cor_results')
    
    open("individual_lines.csv", "w") #not needed
    lines = np.loadtxt("../central_lines.dat")
    table = np.empty((len(lines), len(our_datanames)+1))
    table[:,0] = lines
    
    
    headers = "central_lines"
    for i in range(len(our_datanames)):
        headers = headers + "," + our_datanames[i]
    
    
    
    for i in range(len(our_datanames)):
        table[:, 1+i] = our_data[i] - VN_Pairs[i]
        print(len(our_data[i] - VN_Pairs[i]))
        
    np.savetxt("tableCD.dat", table, header = headers, delimiter=",")   
    
      
    
    
    
if __name__ == '__main__':
    main()   
    
    
