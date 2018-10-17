#!/usr/bin/env python3

dna = "ATGCAGGGGAAACATGATTCAGGAC"

#Make all lowercase
lowerDNA = dna.lower()

#Replace the complementary ones
complA = lowerDNA.replace('a','T')
complAT = complA.replace('t','A')
complATG = complAT.replace('g','C')
complATGC = complATG.replace('c','G')

#reverse the complement
revDNA = complATGC[::-1]

#Print out the answers
print("Original Sequence\t5'",dna,"5'")
print("Complement\t\t3'",complATGC,"5'")
print("Reverse Complement\t5'",revDNA,"3'")


