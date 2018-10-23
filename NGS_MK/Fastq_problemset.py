#!/usr/bin/env python3
from Bio import SeqIO

with open("Trimmed_fastq.fastq", "w") as trimmed:
	#filename = "Fastq_test.fastq"
	filename = "four_reads.fastq"
	
	#What fraction of nucleotides in the file have a quality > 30
	#Count of each quality then div by total?
	
	nucl_count = 0
	qual_30 = 0
	for fastq_record in SeqIO.parse(filename, "fastq"):
		qualityscore = fastq_record.letter_annotations
		#print(qualityscore)
		for qual in qualityscore['phred_quality']:
			nucl_count += 1
			#print(nucl_count)
			#print(qual)
			if qual	> 30:
				qual_30 += 1
				#print(qual_30)
	fraction = qual_30 / nucl_count
	print("Fraction of nucleotides with qual > 30:","{:.2}".format(fraction))



	#Trim the first five bases off and first five quals
	for fastq_record in SeqIO.parse(filename, "fastq"):
		fastq_trimmed = fastq_record[5:]
		#print(fastq_trimmed)
		SeqIO.write(fastq_trimmed,trimmed,"fastq")
	


