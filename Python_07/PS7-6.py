#!/usr/bin/env python3
import re

seq = open("Python_07_ApoI.fasta","r")

longseq = ''
for line in seq:
	if not re.search(r">.+?",line): 		
		line = line.strip()
		cutsite = re.sub(r"([AG])AATT([CT])",r"\1^AATT\2",line)
		longseq += cutsite
		separated = longseq.split('^')
		sorted_seq = sorted(separated,key=len,reverse=True)
print(sorted_seq)

		




