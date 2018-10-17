#!/usr/bin/env python3

dna = "ATGCAGGGGAAACATGATTCAGGAC"

#Make all lowercase
lowerDNA = dna.lower()

#Replace the complementary ones
complA = lowerDNA.replace('a','T')
complAT = complA.replace('t','A')
complATG = complAT.replace('g','C')
complATGC = complATG.replace('c','G')

print("This is the complement: 3'",complATGC,"5'")



