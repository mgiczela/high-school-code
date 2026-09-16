

import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)

def convertToLargestInt(numBits): 
    sum = 0
    for i in range(numBits):
        sum += 2 ** i
    return sum


for case in inputs:
    numBits = int(case)

    largestInt = convertToLargestInt(numBits)
    for i in range(largestInt+1):
        numInBinary = str((bin(i)[2:]))
        if (len(numInBinary) < numBits):
            numLen = len(numInBinary)
            diff = numBits - numLen
            newNum = ""
            for j in range(diff):
                newNum += "0"
            newNum += numInBinary
            numInBinary = newNum
        print(numInBinary)





    

    
    
