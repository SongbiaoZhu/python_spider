# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:07:25 2020
    tidy rank txt into country-specific rank txt, and md.
@author: samsung
"""
import os
import re
def country_rank(fname):
    '''
    tidy rank txt into country-specific rank txt, and md.
    '''
    with open(fname, mode = 'r', encoding = 'utf-8') as f:
        world_rank = f.read()
    pattern = re.compile(r'\n\d+\t')
    world_rank_list = re.split(pattern, world_rank)[1:]
    # extract the university list, and country list
    univ_list = [x.split('\t')[0] for x in world_rank_list]
    country_list = [x.split('\t')[1] for x in world_rank_list]
    # count the frequency of countries
    freq_dict = {}
    for key in country_list:
        freq_dict[key] = freq_dict.get(key, 0) + 1
    print(freq_dict)
    # get the country-specific university rank, store in a dict
    country_rank = {}
    for x in freq_dict.keys():
        country_rank[x] = [i[1] for i in zip(country_list, univ_list) if i[0] == x]
    # save txt， save markdown file
    fname_1 = fname.split('.')[0] + '_country.' + fname.split('.')[1]
    f = open(fname_1, mode = 'w', encoding = 'utf-8')
    for key, value in country_rank.items():
        f.write(key + '\n')
        f.write('\n'.join(value) + '\n')
    f.close()
    fname_2 = fname.split('.')[0] + '_country.md'
    f = open(fname_2, mode = 'w', encoding = 'utf-8')
    for key, value in country_rank.items():
        f.write('## ' + key + '\n')
        f.write('\n'.join(value) + '\n')
    f.close()

path = r'F:\GitHub\python_spider\university_rank_spider'
flist = [os.path.join(path, x) for x in os.listdir(path) if x.endswith('.txt') ]
list(map(country_rank, flist))