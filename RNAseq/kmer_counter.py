#!/usr/bin/env python3
import sys
from Bio import SeqIO
import re


kmer_length = int(sys.argv[1])
filename = sys.argv[2]
num_top_kmers = int(sys.argv[3])

kmer_dict = {}
combined_list = []
count = 0

for seq_record in SeqIO.parse(filename, "fastq"):
	count += 1
	#print(count)
	#print(seq_record.seq)
	length = len(seq_record.seq)
	#print(length)
		
	for index in range(length):
		kmer = str(seq_record.seq[index:index+kmer_length])
		#print(kmer)
		if len(kmer) == kmer_length:
			#print(kmer)
			if kmer not in kmer_dict:
				kmer_dict[kmer] = 1
				#print(kmer)
			else:
				#print("Duplicate")
				kmer_dict[kmer] += 1
			combined_list.append(str(kmer_dict[kmer])+str(kmer))
	#print(combined_list)
	sorted_list = sorted(combined_list)
	print(combined_list)	

#print(kmer_dict)

	
#create a list, sort the list. Pull out the top 10 from the list and print them
#by calling the keys	
			




	#Output a table of the num top kmers sorted by abundance
	#sorted_kmers = sorted()

