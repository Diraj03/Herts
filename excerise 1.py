# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 13:15:13 2023

@author: Diraj
"""

import pandas as pd

countries = pd.read_csv(r'C:\Users\Diraj\Downloads\Masters - DS\Applied DS- 1\countries_top10.csv')
print(countries)

countries.describe()

countries['new_column']= countries['Population'] / countries['GDP']
print(countries)

countries['population/km2']= countries['Population'] / countries['Area']

gdp = pd.read_excel(r'C:\Users\Diraj\Downloads\Masters - DS\Applied DS- 1\GDP_2015dollars.xls')
print(gdp)

import matplotlib.pyplot as plt
plt.figure()
plt.plot(gdp['Year'],gdp['China'],label='china')
plt.plot(gdp['Year'],gdp['Germany'],label='Germany')
plt.plot(gdp['Year'],gdp['Japan'],label='Japan')
plt.plot(gdp['Year'],gdp['United States'],label='United States')
plt.legend()
plt.show()

import numpy as np

data = gdp.loc[gdp['Year']<=2020 & gdp['Year']>=2011]
print(data)

