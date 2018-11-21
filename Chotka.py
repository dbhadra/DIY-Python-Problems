#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:59:01 2018

@author: deepayanbhadra
"""
import pandas as pd
from haversine import haversine
import numpy as np
from pandas import ExcelWriter

np.set_printoptions(precision=20)


path = 'distance.xlsx'
df = pd.read_excel(path,parse_cols = [1,2,3,4,5,7,8])
df = df.assign(Dist=pd.Series(np.zeros(27055)).values);
#df = df.assign(Facility=pd.Series(np.zeros(27055)).values);
df = df.assign(Facility=pd.Series(np.zeros((27055,),dtype='float,float')).values);
df["Facility_city"] = ""

#idx = np.asarray(df.loc[df["lat1"] != '.'].ix[:,0].index)
temp1 = 1e10
j = 0

idx = np.asarray(df[(df['lat1']!='.') & (df['state']== df['state'][0])].index)


for i in range(0, len(df)-26000):
    
    if df['state'][i+1] != df['state'][i]:
        idx = np.asarray(df[(df['lat1']!='.') & (df['state']== df['state'][i+1])].index)
    
    #while (df.iloc[idx[j]]['state'] == df.iloc[i]['state']):     
    while (j<len(idx)):
        
        p1 = (df.iloc[idx[j]]['lat1'],df.iloc[idx[j]]['long1'])
        p2 = (df.iloc[i]['lat2'],df.iloc[i]['long2'])
        df.Dist.iloc[i] = min(temp1,haversine(p1, p2, miles=True))
        
        if df.Dist.iloc[i] < temp1:
            #df.Facility.iloc[i] = idx[j]
            df.Facility.iloc[i] = (p1[0],p1[1])
            df.Facility_city.iloc[i] = df.city.iloc[idx[j]]
            
        temp1 = df.Dist.iloc[i]
        j+=1
        
    j = 0            
    temp1 = 1e10
        
writer = ExcelWriter('Alaska.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
        
   

   


