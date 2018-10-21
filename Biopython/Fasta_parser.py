#!/usr/bin/env python3
from Bio import SeqIO
import sys
import re


filename = ''
try:
	filename = sys.argv[1]
	if not filename.endswith('.fasta'):
		raise ValueError("Not a Fasta file!")
	print("Fasta file found, looks good so far")
except ValueError:
	print("Please provide a FASTA file that ends with .fasta")

else:

	for seq_record in SeqIO.parse(filename, "fasta"):
		print('Name:',seq_record.id)
		print('Decription:',seq_record.description)
		print('Sequence:',seq_record.sequence)



