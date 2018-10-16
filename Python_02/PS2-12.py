#!/usr/bin/env python3
import sys

variable = int(sys.argv[1])

if variable > 0:
	print("Positive")
	if variable < 50:
		result = variable
		result %= 2
		if result == 0:
			print(variable,"is an even number that is smaller than 50")
	elif variable > 50:
		divisible = variable%3
		if divisible == 0:
			print(variable,"is larger than 50 and divisible by 3")

elif variable == 0:
	print(variable,"is equal to 0")

else:
	print("Negative")

print("Finished running script")
