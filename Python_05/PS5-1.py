#!/usr/bin/env python3
import sys

#Make dictionary, print fav book
fav = {'book':'Sabriel','band':'The Killers','tree':'Maple'}
print(fav['book'])

#Print out fav book by using variable
favbook = 'book'
print(fav[favbook])

#Print fav tree
print(fav['tree'])

#Add favourite organism
fav['organism'] = 'cat'
#fav_thing = 'organism'
#print(fav[fav_thing])

#Take a value from the command line to make a value
#print("Here are the keys you can use:")
#for things in fav:
#	print(things)

#userkey = input("Please type in a key: ") 
#print(userkey)
#print("The value of",userkey,"is :",fav[userkey])

#Change fav organism
print("Here are the keys you can use:")
for things in fav:
	print(things)

userkey = input("Please type in a key: ") 
userValue = input("Please type in a new value: ")
fav[userkey] = userValue
print("The value of",userkey,"is now:",fav[userkey])


