# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 01:21:04 2017
Author: VAIBHAV BAGGA
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats.stats import pearsonr
from sklearn.model_selection import train_test_split
training_dataset = pd.read_csv('train.csv')
x = []
for _ in training_dataset['portfolio_id']:
   x.append(float(( _[2:])))
training_dataset['corrected_id'] = x
y = []
for _ in training_dataset['office_id']:
   y.append(float( _[3:]))
training_dataset['corrected_office'] = y
swiss_rate = 1005560/10**6
pound_rate = 1346840/10**6
training_dataset['currency'].replace({'USD':1,'GBP':pound_rate,'CHF':swiss_rate},inplace = True)
training_dataset['pf_category'].replace({'A':1,'B':2,'C':3,'D':4,'E':5},inplace = True)
training_dataset['country_code'].replace({'T':1,'N':2,'Z':3,'U':4,'M':5},inplace = True)
training_dataset['type'].replace({'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8},inplace = True)
training_dataset.fillna(-99999,inplace = True)
dat = []
mon = []
yea = []
for _ in training_dataset['start_date']:
    d = _ % 100
    m = ((_ - d)//100)%100
    y = _//10000 
    dat.append(d)
    mon.append(m)
    yea.append(y)

training_dataset['start_y'] = yea
training_dataset['start_m'] = mon
training_dataset['start_d'] = dat
dat = []
mon = []
yea = []
for _ in training_dataset['creation_date']:
    d = _ % 100
    m = ((_ - d)//100)%100
    y = _//10000 
    dat.append(d)
    mon.append(m)
    yea.append(y)

training_dataset['creation_y'] = yea
training_dataset['creation_m'] = mon
training_dataset['creation_d'] = dat
dat = []
mon = []
yea = []
for _ in training_dataset['sell_date']:
    d = _ % 100
    m = ((_ - d)//100)%100
    y = _//10000 
    dat.append(d)
    mon.append(m)
    yea.append(y)

training_dataset['sell_y'] = yea
training_dataset['sell_m'] = mon
training_dataset['sell_d'] = dat
