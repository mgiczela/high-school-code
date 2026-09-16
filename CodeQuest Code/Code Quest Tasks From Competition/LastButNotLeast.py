import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())
inputs = list()

for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)

for case in inputs:
    case = case.replace('"', "")
    case = case.replace(" ", "")
    
    if(case != ""):
        lastLetter = case[len(case) - 1:]
        print(lastLetter)
    else:
        print("No Letter Found")
    