# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:46:24 2019

check the abbr of ID name:
    https://www.uniprot.org/help/api_idmapping
"""

import urllib.parse
import urllib.request

url = 'https://www.uniprot.org/uploadlists/'

# read query accession from uniprotAccession.txt as query
with open('uniprotAccession.txt', 'r') as f:
    query = ' '.join(f.readlines()[1:]).replace('\n', '')
    
params = {
'from': 'ACC+ID',
'to': 'P_ENTREZGENEID',
'format': 'tab',
'query': query # or input a string, 'P40925 P40926 O43175'; and other separators eg tab, comma are OK
}

data = urllib.parse.urlencode(params)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as f:
   response = f.read()
print(response.decode('utf-8'))

# write query result to uniprotAccConvert.txt
with open('uniprotAccConvert.txt', 'w') as f:
    f.writelines(response.decode('utf-8'))
