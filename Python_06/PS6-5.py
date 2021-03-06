#!/usr/bin/env python3

allSet = set()
pigSet = set()
stemSet = set()

with open("alpaca_all_genes.tsv","r") as allgenes:
	for line in allgenes:
		if line.startswith('Gene'):
			print("Found header")
		else:
			line = line.rstrip()
			allSet.add(line)



with open("alpaca_pigmentation_genes.tsv","r") as piggenes:
	for line in piggenes:
		if line.startswith('Gene'):
			print("Found header")
		else:
			line = line.rstrip()
			pigSet.add(line)

with open("alpaca_stemcellproliferation_genes.tsv","r") as stemgenes:
	for line in stemgenes:
		if line.startswith('Gene'):
			print("Found header")
		else:
			line = line.rstrip()
			stemSet.add(line)


#All genes that are not involved in stemcell proliferation

noProlif = allSet.difference(stemSet)
#print(noProlif)

print(len(allSet))
print(len(stemSet))
print(len(noProlif))

# All genes in both stem cell and pigment
pigstem = stemSet.intersection(pigSet)

print(len(pigstem))


