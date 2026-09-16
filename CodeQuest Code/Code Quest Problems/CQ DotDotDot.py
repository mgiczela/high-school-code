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

alphabet = "_abcdefghijklmnopqrstuvwxyz" #the _ there so the each number's index is its # of dots (a = 1 dot, b = 2 dots, c = 3 dots...)
#for this use hte .index() function, which is basically the indexOf() function from java



for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)


for case in inputs:
    total = 0
    for letter in case:
        total += alphabet.index(letter)
    print(total)
    

    