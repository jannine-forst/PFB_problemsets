#!/usr/bin/env python3
import re
import sys

restrs = {}

with open("bionet.txt","r") as download:
	for line in download:
		if re.search(r"^(.+[A-Z0-9\)])(\s{2,})([A-Z\^]+)$",line):
			line = line.rstrip()
			found = re.search(r"^(.+[A-Z0-9\)])(\s{2,})([A-Z\^]+)$",line)
			reID = found.group(1)
			seq = found.group(3)
		#	reID,seq = line.split(' {2,}')
			restrs[reID] = seq


legend = {}
with open("IUPAC.txt","r") as IUPAC:
	for line in IUPAC:
		line.rstrip()
		code,meaning = line.split('\t')
		legend[code] = meaning

enzyme = sys.argv[1]
sequence = sys.argv[2]

if enzyme in restrs:
	print('Found the enzyme!')
	print(restrs[enzyme])
	cutsite = restrs[enzyme]
	for found in re.finditer(r"([RYSWKMBDHVN\^])",cutsite):
		lookingfor = found.group(0)
		#print("I'm looking for:",lookingfor)
		replacing = legend[lookingfor]
		#print("I am replacing it with:",replacing)
		replacing = replacing.rstrip()
		fixcutsite = re.sub(lookingfor,replacing,cutsite)
		#print("This is what it should look like:",fixcutsite)
		#print("This is what it looked like before:",cutsite)

		


else:
	print('Enzyme not found...')
