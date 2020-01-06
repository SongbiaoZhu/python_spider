# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:45:40 2019

@author: samsung
"""
import os
import gepia

outDir = 'D:/ProgramFiles/PythonScripts/gepia/'
if not os.path.exists(outDir):
        os.mkdir(outDir)
sur = gepia.survival()
sur.setOutDir(outDir)
sur.showParams()
print(gepia.CANCERType)
sur.setParams({'axisunit': 'month',
               'dataset':['OV'],
               'groupcutoff1': '66',
               'groupcutoff2': '34',
               'highcol': '#ff0000',
               'ifconf': 'conf',
               'ifhr': 'hr',
               'is_sub': 'false',
               'lowcol': '#0000ff',
               'methodoption': 'os',
               'signature':['NAPRT'],
               "signature_norm": "",
               "subtype": ""})
# result = sur.query()
params = sur.params
methods = ['os','dfs']
sigs = [['NAPRT'],['NAMPT'],['HPGD']]
datasets = [['OV'],['ACC'],['UVM']]
for dat in datasets:
    for met in methods:
        for sig in sigs:
            sur.setParams(params)
            sur.setParam('dataset',dat)
            sur.setParam('signature',sig)
            sur.setParam('methodoption',met)
            sur.query()
