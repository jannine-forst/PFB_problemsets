#!/usr/bin/env python3

seq = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']


#Problem 11 Part 1 - print each item in list using for loop
#for each in seq:
#	print(each)

#Problem 11 Part 2 - print each item with its length and sequence, tab separated
#for each in seq:
#	print(len(each),"\t",each)


#Problem 12 - use list comprehension
tuple_list = [print(len(each),"\t",each,"\n") for each in seq]
print(type(tuple_list))

#Problem 13 - add position in list
tuple_list = [print((seq.index(each)+1),"\t",len(each),"\t",each,"\n") for each in seq]
#each = seq[1]
#print(seq.index('ATGCCCGGCCCGGC'))
#print("\t",len(each),"\t",each,"\n")

