"""
format
turkeys goats horses
ex:
2 3 4
"""

import sys
import math
import string
from decimal import Decimal
cases = int(sys.stdin.readline().rstrip())
inputs = list()


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)




#number is a decimal type
def giveChange(amount):
    numQuarters = 0
    numDimes = 0
    numNickels = 0
    numPennies = 0
    #keep remoivng quarter until we have les than 25 cents
    while amount >= Decimal("0.25"):
        numQuarters += 1
        amount -= Decimal("0.25")
    #if no money left return amounts
    if amount == Decimal("0"):
        return numQuarters, numDimes, numNickels, numPennies
    #keep remooving dimes till less than value of dime
    while amount >= Decimal("0.10"):
        numDimes += 1
        amount -= Decimal("0.10")
    #again check if no money left
    if amount == Decimal("0"):
        return numQuarters, numDimes, numNickels, numPennies
    #same process for nickels...
    while amount >= Decimal("0.05"):
        numNickels += 1
        amount -= Decimal("0.05")

    if amount == Decimal("0"):
        return numQuarters, numDimes, numNickels, numPennies
    #...and finaly for pennies 
    while amount >= Decimal("0.01"):
        numPennies += 1
        amount -= Decimal("0.01")

    #return final amount
    return numQuarters, numDimes, numNickels, numPennies
    




    

for case in inputs:
    numQuarters = 0
    numDimes = 0
    numNickels = 0
    numPennies = 0

    amount = Decimal(case.split("$")[1])
    numQuarters, numDimes, numNickels, numPennies = giveChange(amount)
    print(f"${amount}")
    print(f"Quarters={numQuarters}")
    print(f"Dimes={numDimes}")
    print(f"Nickels={numNickels}")
    print(f"Pennies={numPennies}")


        


    

    