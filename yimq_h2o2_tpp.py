# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 21:02:34 2019

@author: samsung
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

df = pd.read_excel('2019-11-16_ratio_TPP.xlsx', sheet_name='proteinRatio')
n_row = df.shape[0]

pR1 = df[df.columns[3:11]].values
pR2 = df[df.columns[13:21]].values

x = np.array([37, 41, 49, 53, 57, 61, 65, 70, 75])

fitfunc = lambda p, x: 1/(1+np.exp(p[0]*(x-p[1])))
errfunc = lambda p, x, y: fitfunc(p, x)-y
p0 = np.array([0.2,45])

T1 = np.zeros(n_row)
T2 = np.zeros(n_row)
for i in range(n_row):
    p1, success = optimize.leastsq(errfunc, p0, args=(x, pR1[i,:]))
    if success:
        T1[i] = p1[1]
    else:
        print('row', i, 'failed.')
    p2, success = optimize.leastsq(errfunc, p0, args=(x, pR2[i,:]))
    if success:
        T2[i] = p2[1]
    else:
        print('row', i, 'failed.')

df_out = pd.DataFrame(data={'T1': T1, 'T2': T2, 'deltaT': T2-T1})
df_out.to_excel('out.xlsx')

curve_x = np.linspace(35, 75, 100)
plt.plot(x, pR1[9,:], "ro", curve_x, fitfunc(p1, curve_x), "r-")
plt.show()