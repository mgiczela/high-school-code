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

def formatHeight(x, y):
    return (f"{x}'{y}\"")

def formatDate(yr, month, dayOfMonth):
    if(month < 10):
        month = "0" + str(month)
    if(dayOfMonth < 10): 
        dayOfMonth = "0" + str(dayOfMonth)
    return(f"{yr}{month}{dayOfMonth}")

def concatenate(strList):
    finalStr = ""
    for index, word in enumerate(strList):
        if index == len(strList) - 1:
            finalStr += word
        elif word != " " and word != "":
            finalStr += word + ","
        
    return finalStr

for case in inputs:
    temp = case.split(" ")
    if(temp[0] == "formatHeight"):
        feet = int(temp[1])
        inches = int(temp[2])
        formatedStr = formatHeight(feet, inches)
        print(formatedStr)
    elif (temp[0] == "formatDate"):
        yr = int(temp[1])
        month = int(temp[2])
        day = int(temp[3])
        formatedStr = formatDate(yr, month, day)
        print(formatedStr)
    else:
        strings = temp[1:]
        for item in strings:
            if item == " " or item == "":
                strings.remove(item)

        msg = concatenate(strings)
        print(msg)