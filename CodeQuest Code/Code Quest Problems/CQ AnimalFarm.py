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
    animalCount = case.split(' ')
    numTurkeys = int(animalCount[0])
    numGoats = int(animalCount[1])
    numHorses = int(animalCount[2])

    turkeyLegCount = numTurkeys * 2
    goatLegCount = numGoats * 4
    horseLegCount = numHorses * 4

    print(turkeyLegCount + goatLegCount + horseLegCount)

    

    