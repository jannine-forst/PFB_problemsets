#!/usr/bin/env python3
import sys

dna = sys.argv[1]

capitalDNA = dna.upper()

numA = capitalDNA.count("A")
numT = capitalDNA.count("T")
numG = capitalDNA.count("G")
numC = capitalDNA.count("C")


countAT = numA + numT
countGC = numG + numC
countTotal = numA + numT + numG + numC

contentAT = countAT/countTotal
contentGC = countGC/countTotal


print("AT Content:",contentAT)
print("GC Content:",contentGC)



