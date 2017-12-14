#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:40:37 2017

@author: aantoniadis
"""
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
    
    
    
    # set figure resolution
    set_res = 12
    plt.figure(figsize=([set_res,set_res]))
    # set figure title
    plt.title(name1[7:]+" EW Difference Correlation", fontsize=set_res*2)
    # set axis labels
    plt.xlabel("AA_EW_"+name1[7:], fontsize=set_res*1.5)
    plt.ylabel("AA-VN difference", fontsize=set_res*1.5)
    
    plt.plot(list1,list1-list2, 'k.')
    
    dif_average = np.nanmean(list1-list2)
    dif_median = np.nanmedian(list1-list2)
    dif_std = np.nanstd(list1-list2)
    
    plt.text(np.min(list1), np.nanmin(list1-list2), "__  Mean difference = " + "{0:.5f}".format(dif_average)\
             + "\n" + "_._ Median difference = " + "{0:.5f}".format(dif_median)\
             + "\n" + "---  Standard deviation = " + "{0:.5f}".format(dif_std)\
             , color='black', horizontalalignment ='left', verticalalignment = 'bottom', bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))
    plt.plot((np.min(list1),np.max(list1)),(dif_average,dif_average),'b-')    
    plt.plot((np.min(list1),np.max(list1)),(dif_average+dif_std,dif_average+dif_std),'g--')
    plt.plot((np.min(list1),np.max(list1)),(dif_average-dif_std,dif_average-dif_std),'g--')
    plt.plot((np.min(list1),np.max(list1)),(dif_median,dif_median),'r-.')
    
    plt.savefig('ew_diff_cor_results/ew_diff_corr_%s.png'%name1, bbox_inches='tight')
    plt.close()
    
    # save the statistical values for each star
    l = [name1[7:], dif_average, dif_median, dif_std]
    l = "\t".join(list(map(str, l))) + "\n"
    with open("stat_val.dat", "a") as f:
        f.write(l)


def main():
    
    # Define folder names for my data and the given ones
    myData = "EWmyresults"
    GivenData = "EWvascoresults"
    #os.remove("stat_val.dat")
    # Load data and return the pairs
    our_data, VN_Pairs, our_datanames, VN_PairsNames = Load_Data_Pairs(myData, GivenData)
    
    # If these is not a 'results' directory create one
    if not os.path.exists('ew_diff_cor_results'):
        os.makedirs('ew_diff_cor_results')
    
    open("stat_val.dat", "w")
    # for all the pairs do correlation
    for i in range(len(our_data)):
        Get_Correlation(our_data[i], VN_Pairs[i], our_datanames[i], VN_PairsNames[i])
        
    df1 = pd.read_table("VNstarnames.dat", names=["star", "feh", "teff"], delimiter=r"\s+")
    df1.star = df1.star.str.strip(".fits")
    df2 = pd.read_table("stat_val.dat", names=["star", "dif_average", "dif_median", "dif_std"], delimiter=r"\s+")
    #print(df1, df2)
    df = pd.merge(df1, df2)
    
    

    df.to_csv("statistical_study.csv", index=False)
    
if __name__ == '__main__':
    main()
