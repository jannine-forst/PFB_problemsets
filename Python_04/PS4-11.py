#!/usr/bin/env python3

seq = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']


#Problem 11 Part 1 - print each item in list using for loop
#for each in seq:
#	print(each)

#Problem 11 Part 2 - print each item with its length and sequence, tab separated
#for each in seq:
#	print(len(each),"\t",each)


#Problem 12 - use list comprehension
tuple_list = (print(len(each),"\t",each,"\n") for each in seq)
print(type(tuple_list))



