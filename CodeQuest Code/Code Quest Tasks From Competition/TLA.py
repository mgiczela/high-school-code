import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())
inputs = list()

nonPunctionationANDHYPHEN = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890- "

for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)

for case in inputs:
    for letter in case:
        if letter not in nonPunctionationANDHYPHEN:
            case = case.replace(letter, "")
    case = case.replace("-", " ")
    case = case.split(" ")
    acronym = ""
    for word in case:
        firstLetter = word[0:1]
        acronym = acronym + (firstLetter.upper())
    print(acronym)