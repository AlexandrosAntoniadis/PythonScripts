# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
# This function loads the data and returns the pairs
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

# This function creates and plots the correlation diagram
def Get_Correlation(list1, list2, name1, name2):
    
    # compute slope and intersection by doing linear regration to data
    slope, intersection  = np.polyfit(list1, list2, 1)
    
    # create the linear fit data (red line)
    fit_fn = np.poly1d([slope, intersection])
    x = np.linspace(0,np.max(list1))
    
    
    
    # set figure resolution
    set_res = 12
    plt.figure(figsize=([set_res,set_res]))
    # set figure title
    plt.title(name1[7:]+" EW Correlation", fontsize=set_res*2)
    # set axis labels
    plt.xlabel("AA_EW_"+name1[7:], fontsize=set_res*1.5)
    plt.ylabel("VN_EW_"+name2[9:], fontsize=set_res*1.5)
    # plot the data (experimental and linear fit)
    plt.plot(list1,list2, 'k.', x, fit_fn(x), '--r')
    # set text box for printing the slope and intersection of the red line
    plt.text(np.abs(np.max(list1)/2),0,"Slope = " + "{0:.5f}".format(slope)\
             + "\n" + "Intersection = " + "{0:.5f}".format(intersection)\
             , color='black', bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))
    
    plt.savefig('ew_cor_results/ew_corr_%s.png'%name1, bbox_inches='tight')
    plt.close()


def main():
    
    # Define folder names for my data and the given ones
    myData = "EWmyresults"
    GivenData = "EWvascoresults"
    
    # Load data and return the pairs
    our_data, VN_Pairs, our_datanames, VN_PairsNames = Load_Data_Pairs(myData, GivenData)
    
    # If these is not a 'results' directory create one
    if not os.path.exists('ew_cor_results'):
        os.makedirs('ew_cor_results')
    
    # for all the pairs do correlation
    for i in range(len(our_data)):
        Get_Correlation(our_data[i], VN_Pairs[i], our_datanames[i], VN_PairsNames[i])
    
if __name__ == '__main__':
    main()
