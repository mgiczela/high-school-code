"""
copy the last code for sorting the input, convert to int, use " " as delimiter, then preform the math and reutrn
"""

import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
input_nums = list()

for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    input_nums.append(a)


for value in input_nums:
    case = value.split(' ')
    num1 = int(case[0])
    num2 = int(case[1])

    sum = num1 + num2
    product = num1 * num2
    print(f"{sum} {product}")
