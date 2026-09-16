import sys
import math
import string
from decimal import Decimal, ROUND_DOWN


cases = int(sys.stdin.readline().rstrip())
inputs = list()

for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)

for case in inputs:
    case = case.split(" ")
    distance = float(case[0])
    milePace = case[1].split(":")

    if(distance <= 2.0):
        print(1)
    else:

        milePaceinSeconds = (int(milePace[0]) * 60) + (int(milePace[1]))

        numIntervalsRan = Decimal(str((milePaceinSeconds) * (distance - 2.0) / (600.0)))
        numIntervalsRanRounded = (numIntervalsRan).quantize(Decimal("1"), rounding=ROUND_DOWN)
        print(numIntervalsRanRounded)
    