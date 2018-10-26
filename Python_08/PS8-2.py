#!/usr/bin/env python3
import sys
import re

#Write a script that takes a multi-FASTA file Python_08.fasta
#from user input and breaks each sequence into codons (every
#three nucleotides is a codon) in just the first reading frame.
codons = []
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
	sequence = ''
	for line in fasta:
		header = re.search(r">(\w+)\s?",line)
		if header:
			genename = header.group(1)
			print(genename+"-frame-1-codons")
		else:
			line = line.rstrip()
			sequence = sequence + line
	#print(sequence) works now!
		codons = re.findall(r"(.{3})",sequence)	
		if sequence != '':
			print(codons)
			
				
