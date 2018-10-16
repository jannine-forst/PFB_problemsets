#!/usr/bin/env python3
import sys

variable = int(sys.argv[1])

if variable > 0:
	print("Positive")

elif variable == 0:
	print(variable,"is equal to 0")

else:
	print("Negative")

print("Finished running script")
