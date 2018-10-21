#!/usr/bin/env python3
import re
import sys

def uptolength(dna,maxlength):
	nowhitespace = dna.replace("\n","")
	#print(dna)
	regex = "[A-Z]{1," + str(maxlength) + "}"
	sixty = re.findall(regex,nowhitespace)
	sequence = '\n'.join(sixty)
	#print(sequence)
	return sequence

def gc_content(dna):
	c_count = dna.count('C')
	g_count = dna.count('G')
	dna_len = len(dna)
	gc_content = (c_count + g_count) / dna_len
	return gc_content


def rev_comp(dna):
	lowercase = dna.lower()
	complT = lowercase.replace('a','T')
	complTA = complT.replace('t','A')
	complTAG = complTA.replace('c','G')
	complTAGC = complTAG.replace('g','C')
	return complTAGC[::-1]



#dna = 'AGCT'

#dna = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
#GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
#CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
#TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
#TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
#CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
#GTCATCTTCT'''

#dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'

#print(dna)

sequencefile = sys.argv[1]
maxlength = sys.argv[2]


with open(sequencefile, "r") as input_file, open("Reformatted_sequence.fasta", "w") as output:
	dna = input_file.read()

	print(uptolength(dna,maxlength))
	output.write(uptolength(dna,maxlength))
	output.write("\n")

	print("Percent GC:","{:.2%}".format(gc_content(dna)))
	output.write("Percent GC:")
	output.write("{:.2%}".format(gc_content(dna)))
	output.write("\n")

	print("Reverse Complement:",uptolength( rev_comp(dna) , maxlength ))
	output.write("Reverse Complement: "+uptolength( rev_comp(dna) , maxlength )+"\n")


