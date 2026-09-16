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



for n in range(cases):
    numLines = int(sys.stdin.readline().rstrip())
    total = 0
    for line in range(numLines):
        total += int(sys.stdin.readline().rstrip())

    print(total)
     

    