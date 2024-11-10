#!/usr/bin/env python3

import sys

provincia2count = {}
altura2average = {}

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    municipio, altura, provincia, count = line.split('\t')

    # convert 
    try:
        count = int(count)
        altura = int(altura)
    except ValueError:
        continue
    try:
        provincia2count[provincia] += count
        altura2average[provincia]  += altura
    except:
        provincia2count[provincia] = count
        altura2average[provincia]  = altura
    
# write the tuples to stdout
# Note: they are unsorted

for provincia in provincia2count.keys():
    altura2average[provincia] /= provincia2count[provincia]
    print(f"{provincia}\t{provincia2count[provincia]}\t{altura2average[provincia]}")