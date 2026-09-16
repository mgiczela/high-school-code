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


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)


for case in inputs:
    temp = case.split(" ")
    numSmallBricks = int(temp[0])
    numBigBricks = int(temp[1])
    targetLen = int(temp[2])
    solveStatus = 0 # gonna jus add 1 if solved so yea

    #we can have leftovers
    #so plan is to subract bricks and if we get to 0 len then we print true

    #basically:
    #keep -ing big bricks until the len is < 5
    #then switch to small bricks, if we can make it 0 then then print that
    #otherwise no

    while (numBigBricks > 0 and targetLen >= 5):
        targetLen -= 5
        numBigBricks -= 1
        if targetLen == 0:
            solveStatus += 1
    while (numSmallBricks > 0):
        targetLen -= 1
        numSmallBricks -= 1
        if targetLen == 0:
            solveStatus += 1
    
    if solveStatus >= 1:
        print("true")
    else:
        print("false")    

        
    

    