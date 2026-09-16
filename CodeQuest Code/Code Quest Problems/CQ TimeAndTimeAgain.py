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

def retriveNumOfGivenTimeUnit(indexOfTimeUnitMarker, theString):
    #the 1st paramater is the index of "h", "m" or "s"
    OneIndexBefore = indexOfTimeUnitMarker - 1
    TwoIndexBefore = indexOfTimeUnitMarker - 2
    numDigitOne = 0
    numDigitTwo = 0
    checkSpotTwo = True
    if(TwoIndexBefore < 0):
        checkSpotTwo = False
    
    if(checkSpotTwo):
        try:
            numDigitOne = int(theString[TwoIndexBefore])
        except:
            pass
    numDigitTwo = int(theString[OneIndexBefore])

    return (f"{numDigitOne}{numDigitTwo}")
    

for case in inputs:
    hrs = "00"
    mins = "00"
    sec = "00"

    #find index of h, m, s (if not found then 0)
    #take the 2 previous indexes, one immediedly before is 100 % an int, the one before might not be so check if we can make it int OR if out of bounds
    indexOfHrsMarker = case.find("h")
    indexOfMinsMarker = case.find("m")
    indexOfSecondsMarker = case.find("s")

    #if not found then assumed 0, nothing needs changing
    if(indexOfHrsMarker != -1):
        hrs = retriveNumOfGivenTimeUnit(indexOfHrsMarker, case)
    if(indexOfMinsMarker != -1):
        mins = retriveNumOfGivenTimeUnit(indexOfMinsMarker, case)
    if(indexOfSecondsMarker != -1):
        sec = retriveNumOfGivenTimeUnit(indexOfSecondsMarker, case)

    print(f"{hrs}:{mins}:{sec}")
    
    
   


    
    

    