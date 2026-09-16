

import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)

for case in inputs:
    case = case.split()
    print(case.index("Nimo") + 1)
    


    

    