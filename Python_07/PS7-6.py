#!/usr/bin/env python3
import re

seq = open("Python_07_ApoI.fasta","r")

for line in seq:
	line = line.strip()
	cutsite = re.sub(r"([AG])AATT([CT])",r"\1^AATT\2",line)
	print(type(cutsite))
		




