

import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)

for case in inputs:
    numBits = int(case)

    total = pow(2, numBits)

    for i in range(0, total):
        currentBitString = ""

        for j in range(numBits - 1, -1,  -1):
            bit = (i // pow(2, j)) % 2
            currentBitString += str(bit)

        print(currentBitString)

            

    


    

    