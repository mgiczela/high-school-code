"""
format
turkeys goats horses
ex:
2 3 4
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
    both = case.split(" ")
    dividenValid = False
    divisorValid = False
    divByZero = False
    thing1 = both[0]
    thing2 = both[1]

    try:
        thing1 = int(thing1)
        dividenValid = True
    except:
        pass
# from w3 schools, chekc if we converted to int
#cuz we should still try to convert to float
#if both those have failed, then we are wrong format totally
    if not type(thing1) is int:
        try:
            thing1 = float(thing1)
            dividenValid = True
        except:
            pass

            
############################
    try:
        thing2 = int(thing2)
        divisorValid = True
    except:
        pass
#same for the divisor
    if not type(thing2) is int:
        try:
            thing2 = float(thing2)
            divisorValid = True
        except:
            pass

    if (dividenValid and divisorValid):
        #double chceck we are right format
        if thing2 == 0 or thing2 == 0.0:
            print("Divide By Zero")
        else:
            thing1 = Decimal(str(thing1))
            thing2 = Decimal(str(thing2))
            result = (thing1 / thing2).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP) 
            print(result)
    else:
        if dividenValid == False:
            print("Invalid Dividend")
        elif divisorValid == False:
            print("Invalid Divisor")


    
        
   


    

    