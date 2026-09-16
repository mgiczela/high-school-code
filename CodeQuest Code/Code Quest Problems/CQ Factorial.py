

import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()

def doFactorial(number):
    sum = 1

    while number > 0:
        sum *= number
        number -= 1

    return sum

for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)

for case in inputs:
    n = doFactorial(int(case))
    print(n)


    

    