"""
define a function for each case 
for each case: 
make an empty list for budgeted cost 
make an empty list for actual cost 
make an empty list for average cost variances to print

in the input, 
first line: use split(" ") and save it in the budgeted costs list
repeat for actual cost list

make an empty list for cost variance for each item
iterate thru prediciton and for each item:
that item - item in actual cost at same index, add that number to avg cost variance

after that, get the mean value of all items in the cost variance list
add that number to the avg cost variances to print list

once all cases have been handled, print our avg cost variances to print list one by one

"""

import sys
import math
import string
from decimal import Decimal, ROUND_HALF_UP

avgCostVariance = []


def runCase():
    budgetedCost = []
    actualCost = []
    costVariance = []
    
    numItems = int(sys.stdin.readline().rstrip())
    inputs = list()

    for caseNum in range(2):
        a = sys.stdin.readline().rstrip()
        inputs.append(a)

    for i, item in enumerate(inputs):
        if i == 0:
            budgetedCost = (item.split(" "))
        else:
            actualCost = (item.split(" "))

    for i in range(len(budgetedCost)):
        budgetedCost[i] = Decimal(budgetedCost[i])
        actualCost[i] = Decimal(actualCost[i])

    for i, num in enumerate(budgetedCost):
        costVariance.append((actualCost[i] - num))
    
    costVarianceMean = sum(costVariance) / len(costVariance)
    costVarianceMeanRounded = (costVarianceMean).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) 
    avgCostVariance.append(f"{costVarianceMeanRounded:.2f}")


cases = int(sys.stdin.readline().rstrip())
for case in range(cases):
    runCase()

for num in avgCostVariance:
    print(num)


    




