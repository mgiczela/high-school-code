

import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)


for case in inputs:
    nums = case.split(" ")
    numsDict = {}
    for num in nums:
        num = int(num)
        if num in numsDict:
            numsDict[num] += 1
        else:
            numsDict[num] = 1
        
    foundTrio = False

    for num, numCount in numsDict.items():
        if numCount == 3:
            foundTrio = True
            break

    if (foundTrio):
        print("TRUE")
    else:
        print("FALSE")
    
    

    