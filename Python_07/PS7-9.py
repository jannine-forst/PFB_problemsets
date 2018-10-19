#!/usr/bin/env python3
import re

restrs = {}

with open("bionet.txt","r") as download:
	for line in download:
		if re.search(r"^(.+\s?.[A-Z0-9\)])(\s{2,})([A-Z\^]+)$",line):
			line = line.rstrip()
			found = re.search(r"^(.+\s?.[A-Z0-9\)])(\s{2,})([A-Z\^]+)$",line)
			reID = found.group(1)
			seq = found.group(3)
		#	reID,seq = line.split(' {2,}')
			restrs[reID] = seq
print(restrs)


