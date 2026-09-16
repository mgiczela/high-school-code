

import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)


for case in inputs:
    num = int(case)
    row = ""


    for j in range(num):
        row = row + "# "

    for i in range(num):
        print(row.strip())
    

    