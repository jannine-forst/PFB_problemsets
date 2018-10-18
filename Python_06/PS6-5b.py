#!/usr/bin/env python3

factSet = set()
stemSet = set()

with open("alpaca_transcriptionFactors.tsv","r") as factors:
	for line in factors:
		if line.startswith('Gene'):
			print("Found header")
		else:
			line = line.rstrip()
			factSet.add(line)

with open("alpaca_stemcellproliferation_genes.tsv","r") as stemgenes:
	for line in stemgenes:
		if line.startswith('Gene'):
			print("Found header")
		else:
			line = line.rstrip()
			stemSet.add(line)

cellfactors = factSet.intersection(stemSet)
print(len(cellfactors))

