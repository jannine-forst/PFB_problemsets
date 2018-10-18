#!/usr/bin/env python3
import re

seq = open("Python_07_ApoI.fasta","r")

count = 0
for line in seq:
	line = line.strip()
	for restr in re.finditer(r"[AG]AATT[CT]",line):
		count += 1
		print(restr)
		

print(count)
