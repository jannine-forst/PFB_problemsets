#!/usr/bin/env python3
import sys
import re


filename = sys.argv[1]

splitline = []

gene_dict = {}

with open(filename,"r") as samfile:
	for line in samfile:
		line = line.rstrip()
		splitline = line.split('\t')
		#print(splitline)
		read_name = splitline[0]
		gene_name = re.search(r"(.*)\^",splitline[2])
		gene = gene_name.group(1)
		if gene not in gene_dict:
			gene_dict[gene] = set()
			gene_dict[gene].add(read_name)
		else:
			gene_dict[gene].add(read_name)

	for key in gene_dict:
		number_reads = len(gene_dict[key])
		print(key,"\t",number_reads)			

#print(gene_dict)
		
