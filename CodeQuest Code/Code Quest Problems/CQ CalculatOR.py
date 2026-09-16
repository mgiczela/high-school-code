"""
format
nuCases
each case: num operation num

ex:
2
1 + 2
2 - 3
"""

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
    tempList = case.split(" ")
    num1 = int(tempList[0])
    num2 = int(tempList[2])
    operation = tempList[1]

    if operation == "+":
        answer = num1 + num2
        print(f"{answer:.1f} {answer:.1f}")
    elif operation == "-":
        answer1 = num1 - num2
        answer2 = num2 - num1
        print(f"{answer1:.1f} {answer2:.1f}")
    elif operation == "*":
        answer = num1 * num2
        print(f"{answer:.1f} {answer:.1f}")
    elif operation == "/":
        num1 = Decimal(str(num1))
        num2 = Decimal(str(num2))
        answer1 = num1 / num2
        answer2 = num2 / num1
        answer1 = answer1.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP) 
        answer2 = answer2.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP) 
        print(f"{answer1} {answer2}")


    

    