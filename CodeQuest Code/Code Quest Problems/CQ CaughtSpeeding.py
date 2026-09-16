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
    splitInput = case.split(' ')
    speed = int(splitInput[0])
    isBirthday = (splitInput[1])
    
    if (isBirthday == "true"):
        bonus = 5
    else:
        bonus = 0
    msg = ""
    if speed <= 60 + bonus:
        msg = "no ticket"
    elif speed >= 61 + bonus and speed <= 80 + bonus:
        msg = "small ticket"
    else:
        msg = "big ticket"
    print(msg)
        


    

    

    

    