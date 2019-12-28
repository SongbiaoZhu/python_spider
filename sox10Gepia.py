# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:49:54 2019

@author: samsung
"""

# survival
outDir = 'D:/ProgramFiles/PythonScripts/surSOX10/'
if not os.path.exists(outDir):
        os.mkdir(outDir)    
sur = survival()
sur.setOutDir(outDir)
sur.showParams()
print(CANCERType)

# result = sur.query()
params = sur.params
methods = ['os','dfs']
sigs = [['SOX10']]
cutoffs = [75,66,50]
datasets = [['GBM']]
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