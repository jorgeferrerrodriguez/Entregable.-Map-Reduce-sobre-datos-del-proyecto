#!/usr/bin/env python

import sys                                                                                                                         
from collections import defaultdict                                                                                                
                                                                                                                                   
provincia2count = defaultdict(int)                                                                                                 
altura2average = defaultdict(int)                                                                                                  
                                                                                                                                   
for line in sys.stdin:                                                                                                             
    # remove leading and trailing whitespace                                                                                       
    line = line.strip()                                                                                                            
    # parse the input we got from mapper.py                                                                                        
    provincia, altura = line.split('\t')                                                                                           
                                                                                                                                   
    # convert                                                                                                                      
    try:                                                                                                                           
        altura = int(altura)                                                                                                       
    except ValueError:                                                                                                             
        continue                                                                                                                   
    try:                                                                                                                           
        altura2average[provincia] += altura                                                                                        
    except:                                                                                                                        
        altura2average[provincia] = altura                                                                                         
                                                                                                                                   
    provincia2count[provincia] += 1                                                                                                
                                                                                                                                   
# write the tuples to stdout                                                                                                       
# Note: they are unsorted                                                                                                          
                                                                                                                                   
for provincia in provincia2count.keys():                                                                                           
    altura2average[provincia] /= provincia2count[provincia]                                                                        
    print(provincia + '\t' + str(provincia2count[provincia]) + '\t' + str(altura2average[provincia]))