#!/usr/bin/env python3

class DNArecord(object):
	def __init__(self,DNA_sequence,gene_name,gene_organism):
		self.gene_name = gene_name
		self.DNA_sequence = DNA_sequence
		self.gene_organism = gene_organism

	def seq_length(self):
		seq_length = len(self.DNA_sequence)
		return seq_length

	def nucl_comp(self):
		length = len(self.DNA_sequence)
		contentA = self.DNA_sequence.count('A') / length
		contentG = self.DNA_sequence.count('G') / length
		contentC = self.DNA_sequence.count('C') / length
		contentT = self.DNA_sequence.count('T') / length
		nucl_content = ('A: '+'{:.2%}'.format(contentA)+'\n'+'G: '+'{:.2%}'.format(contentG)+'\n'+'C: '+'{:.2%}'.format(contentC)+'\n'+'T: '+'{:.2%}'.format(contentT)+'\n')
		return nucl_content  

	def gc_content(self):
		length = len(self.DNA_sequence)
		compG = self.DNA_sequence.count('G')
		compC = self.DNA_sequence.count('C')
		gc_content = (compG + compC) / length
		return gc_content

	def fasta_formatter(self):
		fasta = ">{} | {}\n{}".format(self.gene_name, self.gene_organism, self.DNA_sequence)
		return fasta

				



dna_record_obj1 = DNArecord('AGTCAGTC','ABC1','Mycobacterium tuberculosis')

for d in [dna_record_obj1]:
	print('name:', d.gene_name, '\t', 'seq:',d.DNA_sequence)
	print('\nlength:',d.seq_length())
	print("\nNucleotide composition:\n"+d.nucl_comp())
	#print("Expect 25% for each")
	print("GC content: ","{:.2%}".format(d.gc_content()))
	print("\n"+d.fasta_formatter())

