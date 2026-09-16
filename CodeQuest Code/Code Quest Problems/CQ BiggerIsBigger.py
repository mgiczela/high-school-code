"""
format
turkeys goats horses
ex:
2 3 4
"""

import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)

largestNumbersToPrint = []

for case in inputs:
    largestNum = -9999999999999999999
    numbers = case.split(" ")
    for num in numbers:
        number = int(num)
        if number > largestNum:
            largestNum = number
    largestNumbersToPrint.append(largestNum)

for num in largestNumbersToPrint:
    print(num)
    

    