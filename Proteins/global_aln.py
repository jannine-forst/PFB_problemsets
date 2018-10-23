#!/usr/bin/env python3
import re
import sys

def rev_comp(dna):
	lowercase = dna.lower()
	complT = lowercase.replace('a','T')
	complTA = complT.replace('t','A')
	complTAG = complTA.replace('c','G')
	complTAGC = complTAG.replace('g','C')
	return complTAGC[::-1]

#Take in the match and mismatch
#Output alignment score

match = input("Score for match: ")
mismatch = input("Score for mismatch: ")
seq1 = input("Sequence 1: ")
rev1 = input("Do you want to rev comp Sequence 1? Input yes or no: ")
seq2 = input("Sequence 2: ")
rev2 = input("Do you want to rev comp Sequence 2? Input yes or no: ")

if rev1 == "yes":
	seq1 = rev_comp(seq1)
else:
	seq1 = seq1.upper()

if rev2 == "yes":
	seq2 = rev_comp(seq2)
else:	
	seq2 = seq2.upper()

length = len(seq1)
score = 0

for num in range(0,length):
	if seq1[num] == seq2[num]:
		score += int(match)
	else:
		score += int(mismatch)


print("Alignment score:",score)
		

 
