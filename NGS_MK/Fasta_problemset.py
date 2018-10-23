#!/usr/bin/env python3
import re
import sys
from Bio import SeqIO

with open("NGS_table.txt","w") as output_file:
	

	filename = "human_cds.fasta"
	fasta_dict = SeqIO.to_dict(SeqIO.parse(filename, 'fasta'))

	output_file.write("Sequence_name\tGC_Percentage\n")
	for seq in fasta_dict:
		#print(fasta_dict[seq].seq)
		countA = fasta_dict[seq].seq.count('A')
		countT = fasta_dict[seq].seq.count('T')
		countG = fasta_dict[seq].seq.count('G')
		countC = fasta_dict[seq].seq.count('C')
#print(seq+"->","A:",countA,"T:",countT,"G:",countG,"C:",countC)
		#Percentage of GC
		length = len(fasta_dict[seq].seq)
		perc_gc = (countG + countC) / length
		output_file.write(seq+"\t"+"{:.2%}".format(perc_gc)+"\n")
	

