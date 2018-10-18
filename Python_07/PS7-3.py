#!/usr/bin/env python3
import re

#Using pattern matching, find and print all the header lines in file


#seq = open("Python_07.fasta","r")

#for line in seq:
#	for match in re.finditer(r"^>\S",line):
#		print(match)


# If line matches a header, extract sequence name and description using subpatterns

seq = open("Python_07.fasta","r")

for line in seq:
	for match in re.finditer(r"(^>.+? )(.+)",line):
		#print(match)
		seqname = match.group(1)
		description = match.group(2)
		print("id:",seqname,"desc:",description)

