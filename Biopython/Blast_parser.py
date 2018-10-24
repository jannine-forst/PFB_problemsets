#!/usr/bin/env python3
from Bio import SeqIO

ID_list = []

for seq_record in SeqIO.parse("Small_uniprot_test.fasta", "fasta"):
	ID_list.append(seq_record.id)
	print(ID_list)

num_ID = len(ID_list)
print("Number of IDs present:",num_ID)

