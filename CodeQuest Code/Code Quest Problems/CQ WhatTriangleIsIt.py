"""
format
turkeys goats horses
ex:
2 3 4
"""

import sys
import math
import string
from decimal import Decimal
cases = int(sys.stdin.readline().rstrip())
inputs = list()


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)


for case in inputs:
    all = case.split(", ")
    s1 = int(all[0])
    s2 = int(all[1])
    s3 = int(all[2])

    numEqualSides = 0
    if(s1 == s2):
        numEqualSides += 1
    if(s1 == s3):
        numEqualSides += 1
    if(s3== s2):
        numEqualSides += 1

    canTriangle = False
    if (s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1):
        canTriangle = True
    
    if (canTriangle):
        if(numEqualSides == 3):
            print("Equilateral")
        elif(numEqualSides == 1):
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Not a Triangle")


    
    

    