#!/usr/bin/env python3


#Create and print string

people = "sapiens, erectus, neanderthalensis"
print(people)

#Split the string into individual words

species = people.split(', ')
print(species)


#Sort alphabetically
print(sorted(species))

#Sort be length of string and print

print(sorted(species,key=len))

