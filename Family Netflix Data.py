#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:05:49 2020

@author: RileyBallachay
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import datetime
import numpy as np

directory = '/Users/RileyBallachay/Downloads/NetflixViewingHistory'
files = [' (2)',' (3)',' (4)',' (5)']
names = ['Brian','Mitchell','Riley','Myrene']

def date_range(start, end):
    r = (end+datetime.timedelta(days=1)-start).days
    return [start+datetime.timedelta(days=i) for i in range(r)]
 

li = []
for index,file in enumerate(files):
    
    pathname = directory+file+'.csv'
    df = pd.read_csv(pathname,index_col=None)
    haha=df
    df['Date']  = [str(pd.Timestamp(date))[0:7] for date in list(df['Date'])]
    df = df.groupby('Date').count().reset_index()
    
    if index==0:
        start = pd.Timestamp(df['Date'].min())
        end = pd.Timestamp(df['Date'].max())
        dateList = date_range(start, end)
        listedDates = [str(pd.Timestamp(date))[0:7] for date in dateList]
    
    df = df.rename(columns={'Title':names[index]})
    
    li.append(df)


Dataframe = pd.DataFrame(listedDates,columns=['Date'])
li.append(Dataframe)

New = pd.concat(li, axis=0, ignore_index=True,sort=True).sort_values(by='Date').reset_index().fillna(0).drop('index',axis=1)
New = New.groupby('Date',as_index=False).sum()

plt.figure(figsize=(50,10))
plt.plot(New['Date'],New['Brian'],c='purple',label='Brian')
plt.plot(New['Date'],New['Mitchell'],c='blue',label='Mitchell')
plt.plot(New['Date'],New['Riley'],c='red',label='Riley')
plt.plot(New['Date'],New['Myrene'],c='green',label='Myrene')
plt.legend( prop={'size': 20})
plt.xticks(rotation=45)
plt.ylabel('Number of Shows/Movies Watched Per Month')
plt.xlabel('Date (Month)')
plt.savefig("netflix.png")