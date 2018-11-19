#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:59:01 2018

@author: deepayanbhadra
"""
import pandas as pd
from haversine import haversine
import numpy as np

#import xlrd
#workbook = xlrd.open_workbook('distance.xlsx')
#sheet = workbook.sheet_by_index(0)

path = 'distance.xlsx'
df = pd.read_excel(path, parse_cols = [1,2,4,5,7,8])
df = df.assign(dist=pd.Series(np.zeros(27055)).values);
df = df.assign(Depot=pd.Series(np.zeros(27055)).values);


temp1 = 1e10
for i in range(0, len(df)):
    for j in range(0, len(df)):
        if  df.iloc[j]['lat1'] is '.' and df.iloc[j]['long1'] is '.':
            continue
        else:     
            p1 = (df.iloc[j]['lat1'],df.iloc[j]['long1'])
            p2 = (df.iloc[i]['lat2'],df.iloc[i]['long2'])
            df.dist.iloc[i] = min(temp1,haversine(p1, p2, miles=True))
            if df.dist.iloc[i] < temp1:
                df.Depot.iloc[i] = j
            temp1 = df.dist.iloc[i]
    temp1 = 1e10
        

        
   

   


