import sys
import math
import string
from decimal import Decimal, ROUND_HALF_UP, ROUND_CEILING

cases = int(sys.stdin.readline().rstrip())
inputs = list()

for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)

for case in inputs:

    case = case.split(" ")
    dimensions = case[0]

    dimensions = dimensions.split("x")
    brickL = int(dimensions[0])
    brickH = int(dimensions[1])

    brickArea = brickH * brickL

    wallHeight = int(case[1])
    numWalls = int(case[2])

    totalNumBricks = Decimal("0.0")
    for index, item in enumerate(case):
        if index > 2:
            currentWallArea = int(item) * wallHeight
            numBricks = Decimal(str(currentWallArea)) / Decimal(str(brickArea))

            totalNumBricks += numBricks
    
    totalNumBricks = Decimal(str(totalNumBricks))
    totalNumBricksRounded = (totalNumBricks).quantize(Decimal("1"), rounding=ROUND_CEILING)
    
    print(totalNumBricksRounded)

    


    