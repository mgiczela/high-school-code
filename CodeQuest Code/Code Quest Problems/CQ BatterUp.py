
import sys
import math
import string
from decimal import Decimal, ROUND_HALF_UP 
cases = int(sys.stdin.readline().rstrip())
inputs = list()


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)


for case in inputs:
    numStrikes = Decimal("0") #K
    numWalks = Decimal("0") #BB
    numSingles = Decimal("0") #1B
    numDoubles = Decimal("0") #2B
    numTriples = Decimal("0") #3B
    numHomeRuns = Decimal("0") #HR

    name = ""

    dataSplit1 = case.split(":")

    name = dataSplit1[0]
    playerData = dataSplit1[1].split(",")


    for item in playerData:
        if item == "BB":
            numWalks += Decimal("1")
        elif item == "K":
            numStrikes += Decimal("1")
        elif item == "1B":
            numSingles += Decimal("1")
        elif item == "2B":
            numDoubles += Decimal("1")
        elif item == "3B":
            numTriples += Decimal("1")
        elif item == "HR": 
            numHomeRuns += Decimal("1")
        
        
        numAtBats = len(playerData) - numWalks

        



    if numAtBats != 0:
        SLG = ((numSingles) + (2 * numDoubles) + (3 * numTriples) + (4 * numHomeRuns)) / numAtBats
        SLGRounded = (SLG).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP) 
        print(f"{name}={SLGRounded}")
    else:
        print(f"{name}=0.000")

    

    

    