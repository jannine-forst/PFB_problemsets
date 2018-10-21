#!/usr/bin/env python3

class DNArecord(object):
	def __init__(self,gene_name,DNA_sequence,gene_organism):
		self.gene_name = gene_name
		self.DNA_sequence = DNA_sequence
		self.gene_organism = gene_organism

	def seq_length(self):
		seq_length = len(self.DNA_sequence)
		return seq_length


dna_record_obj1 = DNArecord('AGTCAGTC','ABC1','Mycobacterium tuberculosis')

for d in [dna_record_obj1]:
	print('name:', d.gene_name, '\t', 'seq:',d.DNA_sequence)



