# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:45:40 2019

@author: samsung
"""
import os
import gepia
bp=gepia.boxplot()
bp.showParams()
bp.setParam('jittersize',0.5)
print(gepia.CANCERType)

outDir = 'D:/ProgramFiles/PythonScripts/gepiaResults/'
bp.setOutDir(outDir)
if not os.path.exists(outDir):
        os.mkdir(outDir)

bp.setParam('dataset',['BLCA', 'BRCA'])
result=bp.query()


from IPython.display import IFrame

IFrame(result,width=500,height=500)
params=bp.params
sigs=[['CCR7','LEF1','TCF7','SELL'],['CX3CR1','FGFBP2','FCGR3A'],['HAVCR2','TIGIT','LAG3','PDCD1','CXCL13','LAYN']]


for sig in sigs:
    bp.setParams(params)
    bp.setParam('signature',sig)
    bp.query()
