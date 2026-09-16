"""



"""

import sys
import math
import string
#cases = int(sys.stdin.readline().rstrip())
inputs = list()
otherInputs = list()


#for caseNum in range(cases):
    #a = sys.stdin.readline().rstrip()
    #inputs.append(a)

def getBlanksToFillIn(numBlanks):
    toFillIn = {}
    

    for caseNum in range(numBlanks):
        a = sys.stdin.readline().rstrip()
        inputs.append(a)

    for i, item in enumerate(inputs):
        itemSplit = item.split(": ")
        toFillIn.update({itemSplit[0] : itemSplit[1]})
    #print(toFillIn)
    #toFillIn.clear()
    return toFillIn

def getOutputTextWithBlanks(numLines):
    message = []
    for caseNum in range(numLines):
        a = sys.stdin.readline().rstrip()
        otherInputs.append(a)
    for i, item in enumerate(otherInputs):
        message.append(item)
    return message

def fillInBlanks(dictionaryOfBlanks, stringToFillIn):
    for key, value in dictionaryOfBlanks.items():
        tempVar = "[" + key + "]"
        stringToFillIn = stringToFillIn.replace(tempVar, value)
    print(stringToFillIn)
    #return stringToFillIn
    

        


#for case in inputs:
    #getBlanksToFillIn()
    

cases = int(sys.stdin.readline().rstrip())
for case in range(cases):
    numbers = sys.stdin.readline().rstrip()
    numbers = numbers.split(" ")
    numLinesOfBlanks = int(numbers[0])
    numLinesOfTxt = int(numbers[1])

    

    #tested up to this pt (above), the numbers work.
    blanks = getBlanksToFillIn(numLinesOfBlanks)
    
    message = getOutputTextWithBlanks(numLinesOfTxt)

    for msg in message:
        fillInBlanks(blanks, msg)
        


    
    