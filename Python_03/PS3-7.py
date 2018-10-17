#!/usr/bin/env python3
import sys

dna = sys.argv[1]

capitalDNA = dna.upper()

capitalRNA = capitalDNA.replace('T','U')


numA = capitalRNA.count("A")
numT = capitalRNA.count("T")
numG = capitalRNA.count("G")
numC = capitalRNA.count("C")
numU = capitalRNA.count("U")

print("As:",numA,"Ts:",numT,"Gs:",numG,"Cs:",numC,"Us:",numU)





