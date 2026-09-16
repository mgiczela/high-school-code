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
    both = case.split(" ")
    g1 = both[0]
    g2 = both[1]

    if (g1 == "true" and g2 == "true") or (g1 == "false" and g2 == "false"):
        print("true")
    else:
        print("false")
    

    