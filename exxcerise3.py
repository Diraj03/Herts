# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:13:42 2023

@author: Diraj
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as  np

barclays= pd.read_csv(r'C:\Users\Diraj\Downloads\Masters - DS\Applied DS- 1\New folder\BCS_ann.csv')
print(barclays.head())

bp= pd.read_csv(r'C:\Users\Diraj\Downloads\Masters - DS\Applied DS- 1\New folder\BP_ann.csv')
print(bp.head())

vod= pd.read_csv(r'C:\Users\Diraj\Downloads\Masters - DS\Applied DS- 1\New folder\VOD_ann.csv')
print(vod.head())

tes= pd.read_csv(r'C:\Users\Diraj\Downloads\Masters - DS\Applied DS- 1\New folder\TSCO_ann.csv')
print(tes.head())

plt.figure()
plt.subplot(2,2,1)
plt.hist(barclays['ann_return'],label='BARCLAYS',density=True,color='Red')
plt.legend()
plt.subplot(2,2,2)
plt.hist(bp['ann_return'],label='BP',density=True,color='Orange')
plt.legend()
plt.subplot(2,2,3)
plt.hist(vod['ann_return'],label='VODO',density=True,color='Green')
plt.legend()
plt.subplot(2,2,4)
plt.hist(tes['ann_return'],label='TESCO',density=True,color='Yellow')
plt.legend()
plt.show()


plt.figure()
plt.hist(barclays['ann_return'],label='BARCLAYS',density=True,alpha=0.5)
plt.hist(bp['ann_return'],label='BP',density=True)
plt.legend()




plt.figure()
name=['BARCLAYS','BP','VODOFONE','TESCO']
plt.boxplot([barclays['ann_return'],bp['ann_return'],vod['ann_return'],tes['ann_return']])
plt.legend(name)
plt.show()


name=['BARCLAYS','BP','VODOFONE','TESCO']
mark_cap=np.array([33367,68785,20979,29741])

plt.figure()
plt.pie(mark_cap,labels=name)
plt.show()

ftse= 1814000
norm = mark_cap / ftse
plt.figure()
plt.pie(norm,labels=name,normalize=False)
plt.show()


plt.figure()
plt.bar(name,mark_cap)
plt.ylabel('market_cap')
plt.show()