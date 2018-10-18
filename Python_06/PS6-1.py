#!/usr/bin/env python3


# Open and read the file, make each line uppercase then print
test_reading = open("Python_06.txt","r")
test_writing = open("Python_06_uc.txt","w")

for line in test_reading:
	uppercase = line.upper()
	test_writing.write(uppercase)
	
print("Wrote the file")
	
