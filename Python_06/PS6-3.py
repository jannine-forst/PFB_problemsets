#!/usr/bin/env python3

with open("Python_06.fastq", "r") as sequence:

#each line is seqName\tsequence\n
#reverse complements the sequence only
#	for line in sequence:
#		name,seq = line.rstrip().split()
#		lowercase = seq.lower()
#		complA = lowercase.replace('a','T')
#		complAT = complA.replace('t','A')
#		complATC = complAT.replace('c','G')
#		complATCG = complATC.replace('g','C')
#		reverse = complATCG[::-1]
#		print(name,"\t",reverse)



# Problemset 6-4, open and go through each line
#count number of lines and number of characters per line

	total_lines = 0
	total_chars = 0
	for line in sequence:
		line = line.rstrip()
		total_lines += 1
		total_chars += len(line)
	av_len = total_chars/total_lines

	print("Total number of lines:",total_lines)
	print("Total number of characters:",total_chars)
	print("Average line length:",av_len)
		
		
