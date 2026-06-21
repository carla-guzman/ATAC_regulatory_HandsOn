#!/usr/bin/env python


#************
# LIBRARIES *
#************

import sys
from optparse import OptionParser


#*****************
# OPTION PARSING *
#*****************

parser = OptionParser()
parser.add_option("-i", "--input", dest="input")
parser.add_option("-s", "--start", dest="start")
options, args = parser.parse_args()

open_input = open(options.input)
enhancer_start = int(options.start)


#********
# BEGIN *
#********

x=1000000 # set maximum distance to 1 Mb
selectedGene="" # initialize the gene as empty
selectedGeneStart=0 # initialize the start coordinate of the gene as empty

for line in open_input.readlines():
        gene, y = line.strip().split('\t')

        position = int(y)
        distance = abs(position - enhancer_start)

        if distance < x:
                x = distance
                selectedGene = gene
                selectedGeneStart = position

print "\t".join([selectedGene, str(selectedGeneStart), str(x)])
