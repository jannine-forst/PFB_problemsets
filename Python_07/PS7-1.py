#!/usr/bin/env python3
import re

with open("Python_07_nobody.txt","r") as nobody:
	for line in nobody:
		for found in re.finditer(r"Nobody",line):
			word_start = found.start() + 1
			word_end = found.end() + 1

			print("Start:",word_start,"\tEnd:",word_end)

#problemset 7-2, subsitute every occurance of nobody with your fav name and write output file with that name

payo = open("Payo.txt", "w")

with open("Python_07_nobody.txt","r") as nobody:
	for line in nobody:
		fav_name = re.sub(r"Nobody",r"Payo",line)
		payo.write(fav_name)

print("Wrote Payo.txt")


