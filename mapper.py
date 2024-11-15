#!/usr/bin/env python

import sys                                                                                                                         
import csv                                                                                                                         
                                                                                                                                   
reader = csv.reader(sys.stdin)                                                                                                     
                                                                                                                                   
# Removes the fist line form the standard input.                                                                                   
# id,nombre,municipio,provincia,altura,latitud,logintud                                                                            
header = next(reader)                                                                                                              
                                                                                                                                   
for line in reader:                                                                                                                
                                                                                                                                   
    # Checks that the fields are not empty.                                                                                        
    if not line[3] or not line[4]:                                                                                                 
        continue                                                                                                                   
                                                                                                                                   
    # Store the values to print                                                                                                    
    provincia = line[3]                                                                                                            
    altura = line[4]                                                                                                               
                                                                                                                                   
    # Print the information to be processed on the reducer.                                                                        
    print(provincia + '\t' + altura)