#!/usr/bin/env python3
import sys
import re

#Take a multi-FASTA Python_08.fasta file from user input and calculate the nucleotide composition for each sequence. Use a datastructure to keep count. Print out each sequence name and its compostion in this format seqName\tA_count\tT_count\tG_count\C_count


filename = ''
try:
	filename = sys.argv[1]
	if not filename.endswith('.fasta'):
		raise ValueError("Not a Fasta file!")
	print("Fasta file found, looks good so far")
except ValueError:
	print("Please provide a FASTA file that ends with .fasta")

else:
	fasta = open(filename, "r")
	genes={}
	for line in fasta:
		header = re.search(r">(\w+)\s?",line)
		if header:
			genename = header.group(1)
			genes[genename] = {}		#create a new gene (key) with dictionary as the value
			genes[genename]['A'] = 0	#Add dictionary key and value for each nucleotide
			genes[genename]['T'] = 0
			genes[genename]['G'] = 0
			genes[genename]['C'] = 0
		else:
			genes[genename]['A'] += line.count('A')	#append nucleotide composition to any prev values
			genes[genename]['T'] += line.count('T')				
			genes[genename]['G'] += line.count('G')				
			genes[genename]['C'] += line.count('C')				

	print("Dictionary:",genes)
	for genename in genes:
		print(genename,"\t",genes[genename]['A'],"\t",genes[genename]['T'],"\t",genes[genename]['G'],"\t",genes[genename]['C'])




