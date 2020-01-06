# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:12:00 2019

@author: samsung
https://www.kegg.jp/kegg/rest/keggapi.html
"""

import pandas as pd

hsaPathway = 'http://rest.kegg.jp/list/pathway/hsa'
res=pd.read_csv(hsaPathway, sep='\t')
res.to_csv('hsaPathway.csv',sep=',',index=None) 

# /list/pathway/hsa 	   	returns the list of human pathways
species = ['hsa', 'mmu','rno']
for i in range(len(species)):
    allPathway = 'http://rest.kegg.jp/list/pathway/{}'.format(species[i])
    res=pd.read_csv(allPathway, sep='\t')
    res.to_csv('Pathways{}.csv'.format(species[i]),sep=',',index=None) 

# http://rest.kegg.jp/find/pathway/Citrate cycle
qurey = 'http://rest.kegg.jp/find/pathway/Citrate cycle'
res=pd.read_csv(qurey, sep='\t')

s