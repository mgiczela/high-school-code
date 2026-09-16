"""
Plan for each input:
string of just vowels, then for each letter in 1 input sentnace, use "indexOf" meathod (check if output is not -1)
if it exists, if true add 1 to counter var, return counter when at last index
use the "if x in y", its easier
"""
import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()
vowels = "aeiou"

for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)


for words in inputs:
    counter = 0
    for letter in words:
        if letter in vowels:
            counter += 1
    print(counter)
