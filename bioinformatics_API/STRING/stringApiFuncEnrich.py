# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:59:15 2019

@author: samsung
"""

#!/usr/bin/env python

#######################################################################
## The script retrieves significantly (FDR < 1%) enriched GO process
## annotations for a given set of proteins and outputs the terms
## on the screen in a TSV format
#######################################################################

import sys 
import urllib2
import json

string_api_url = "https://string-db.org/api"
output_format = "json"
method = "enrichment"

my_genes = ['7227.FBpp0074373', '7227.FBpp0077451', '7227.FBpp0077788',
            '7227.FBpp0078993', '7227.FBpp0079060', '7227.FBpp0079448']

species = "7227"
my_app  = "www.awesome_app.org"

## Construct the request

request_url = string_api_url + "/" + output_format + "/" + method + "?"
request_url += "identifiers=" + "%0d".join(my_genes)
request_url += "&" + "species=" + species
request_url += "&" + "caller_identity=" + my_app

## Call STRING

try:    
    response = urllib2.urlopen(request_url)
except urllib2.HTTPError as err:
    error_message = err.read()
    print error_message
    sys.exit()

## Read and parse the results

result = response.read()

if result:
    data = json.loads(result)
    for row in data:
        term = row["term"]
        preferred_names = ",".join(row["preferredNames"])
        fdr = float(row["fdr"])
        description = row["description"]

        if fdr < 0.01:
            print "\t".join([term, preferred_names, str(fdr), description])