#!/usr/bin/env python3
import sys

dna = sys.argv[1]
#print("Should be position 2, nucleotide should be G")

#Find the starting nucleotide position of an EcoRI site in the DNA sequence

ecoRI = "GAATTC"

ecoInDNA = dna.find(ecoRI)
positionEcoRI = ecoInDNA + 1

print("Starting position =",positionEcoRI)


#Find the ending nucleotide position

endEcoRI = ecoInDNA + 6

print("Ending position =",endEcoRI)


#Print outusing string formatting
#Format => EcoRI startPos:yourStartPos endPos:yourEndPos

print("EcoRI startPos:{} endPos:{}".format(positionEcoRI,endEcoRI))

