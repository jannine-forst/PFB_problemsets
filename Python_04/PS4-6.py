#!/usr/bin/env python3

numlist = ['101','2','15','22','95','33','2','27','72','15','52']

#for num in numlist:
#	if int(num)%2 == 0:
#		print(num)


sortNum = sorted(numlist)
print(sortNum)

even = 0
odd = 0

for num in numlist:
	if int(num)%2 == 0:
		even = int(even)+int(num)
	else:
		odd = int(odd)+int(num)
print("Sum of even numbers:",even)
print("Sum of odd numbers:",odd)	

print("Done!")

