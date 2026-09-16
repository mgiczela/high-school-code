import sys
import math
import string
from decimal import Decimal, ROUND_HALF_UP, ROUND_CEILING

planetRatios = {"Mercury":0.377, "Venus":0.905, "Earth":1, "Mars":0.379,
                "Jupiter":2.528, "Saturn":1.065, "Uranus":0.886, "Neuptune":1.137}

cases = int(sys.stdin.readline().rstrip())
inputs = list()

for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)

for case in inputs:
    earthWeight = int(case)
    for planet, ratio in planetRatios.items():
        updatedMass = Decimal(str(ratio)) * Decimal(str(earthWeight))
        updatedMassRounded = (updatedMass).quantize(Decimal("1.0"), rounding=ROUND_HALF_UP)
        print(f"{planet}: {updatedMassRounded}")
    
    