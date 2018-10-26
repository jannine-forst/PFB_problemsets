#!/usr/bin/env python3
from Bio import SeqIO
import sys
import re

def gc_content(dna):
	dna = dna.upper()
	length = len(dna)
	count_G = dna.count('G')
	count_C = dna.count('C')
	gc_content = (count_G + count_C) / length
	return gc_content

filename = ''
try:
	filename = sys.argv[1]
	if not filename.endswith('.fasta'):
		raise ValueError("Not a Fasta file!")
	print("Fasta file found, looks good so far")
except ValueError:
	print("Please provide a FASTA file that ends with .fasta")

else:
	count = 0
	length_list = []
	num_nucl = 0
	gc_list = []	

	for seq_record in SeqIO.parse(filename, "fasta"):
		#Print out the ID, decription, and sequence
		print('Name:',seq_record.id)
		print('Decription:',seq_record.description)
		print('Sequence:',seq_record.seq)
		#Start a count for the number of sequences
		count += 1
		#To get the total number of sequences:
		num_nucl += len(seq_record.seq)
		#Make a list of all sequence lengths
		#so that shortest and longest can be pulled out
		length_list.append(len(seq_record.seq))
		
		#Calculate and make a list of all the GC contents
		gc_list.append(gc_content(seq_record.seq))
		


	
	#Make the variables to be printed	
	sorted_list = sorted(length_list) #Sort by size
	shortest = sorted_list[0]
	longest = sorted_list[-1]
	avg_len = int(num_nucl / count)
	#For GC content
	sorted_gc_list = sorted(gc_list)
	gc_total = sum(sorted_gc_list)
	avg_gc = "{:.2%}".format(gc_total / count)
	low_gc = "{:.2%}".format(sorted_gc_list[0])
	high_gc = "{:.2%}".format(sorted_gc_list[-1])
			

	print('Sequence count:',count)
	print('Total number of nucleotides:',num_nucl)
	print('Average length:',avg_len)
	print('Shortest length:',shortest)
	print('Longest length:',longest)
	print('Average GC content:',avg_gc)
	print('Lowest GC content:',low_gc)
	print('Highest GC content:',high_gc)
	


