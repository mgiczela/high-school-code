

import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)


for case in inputs:
    fibonnaci = [] 
    nthNumInFib = int(case)

    for i in range(nthNumInFib+5):
        if(i == 0):
            fibonnaci.append(0)
        elif(i==1):
            fibonnaci.append(1)
        else:
            fibonnaci.append(fibonnaci[i-1] + fibonnaci[i-2])

    print(f"{nthNumInFib} = {fibonnaci[nthNumInFib-1]}")

    
    

    

    