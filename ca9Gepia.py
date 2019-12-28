# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:29:22 2019

@author: samsung
"""
import os

# survival
outDir = 'D:/ProgramFiles/PythonScripts/surCA9/'
if not os.path.exists(outDir):
        os.mkdir(outDir)    
sur = survival()
sur.setOutDir(outDir)
sur.showParams()
print(CANCERType)

# result = sur.query()
params = sur.params
methods = ['os','dfs']
sigs = [['CA9'],['MCAM'], ['CA9','MCAM']]
cutoffs = [75,66,50]
datasets = [['KIRC']]
sig_norms = ["","GAPDH","ACTB"]
for dat in datasets:
    for met in methods:
        for sig in sigs:
            for cut in cutoffs:
                for sig_norm in sig_norms:
                    sur.setParams(params)
                    sur.setParam('dataset',dat)
                    sur.setParam('signature',sig)
                    sur.setParam('methodoption',met)
                    sur.setParam('groupcutoff1',str(cut))
                    sur.setParam('groupcutoff2',str(100-cut))
                    sur.setParam('signature_norm',sig_norm)
                    sur.query()

# correlation
outDir = 'D:/ProgramFiles/PythonScripts/corrCA9/'
if not os.path.exists(outDir):
        os.mkdir(outDir)                   
corr = correlation()
corr.setOutDir(outDir)
corr.showParams()
corr.showParams()
params = corr.params

sig1s = [['CA9']]
sig2s = [['MCAM']]
sig_norms = ["GAPDH","ACTB",""]
datasets = TCGATumor

for dat in datasets:
    for sig1 in sig1s:
        for sig2 in sig2s:
            for sig_norm in sig_norms:
                corr.setParams(params)
                corr.setParam('dataset',dat)
                corr.setParam('signature1',sig1)
                corr.setParam('signature2',sig2)
                corr.setParam('signature1_norm',sig_norm)
                corr.setParam('signature2_norm',sig_norm)
                corr.query()
