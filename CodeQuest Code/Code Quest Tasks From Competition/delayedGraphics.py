import sys
import math
import string
numCases = int(sys.stdin.readline().rstrip())

for case in range(numCases):
    maxDelayAllowed = int(sys.stdin.readline().rstrip())
    inputData = sys.stdin.readline().rstrip()
    inputData = inputData.split(" ")

    inputDelayTime = int(inputData[0])
    processDelayTime = int(inputData[1])

    totalDelay = inputDelayTime + processDelayTime
    if(totalDelay <= maxDelayAllowed):
        print("PASS")
    else:
        print((totalDelay - maxDelayAllowed))