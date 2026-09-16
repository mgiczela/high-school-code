"""
plan:
- make all the text uppercase (cuz final result wants each letter uppercase so this saves a step)
- go thru charachter for charachter and if its not in the alphabet string then do nothing
- while we are iterating: adding the letter to dictionary if not in it, if they are update count in dicitonary of em (also add 1 to counter of letters var)
- afterwards: update each value in the dictioanry to be its frequency (using the count of letters var weve been updating)
"""

import sys
import math
import string
from decimal import Decimal, ROUND_HALF_UP
inputs = list()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 




def runCase(message):
    letterFreq = {}
    message = message.upper()
    letterCount = 0
    for char in message:
        if char in alphabet:
            letterCount += 1
            if char in letterFreq:
                letterFreq[char] += 1
            else: 
                letterFreq.update({char : 1})
    
    letterRelativeFreq = {}
    for letter, numLetterOccurances in letterFreq.values():
        relativeFreq = Decimal(str((numLetterOccurances / letterCount) * 100)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) 
        letterRelativeFreq.update({letter : relativeFreq})
    
    return letterRelativeFreq

cases = int(sys.stdin.readline().rstrip())
for case in range(cases):
    numLines = int(sys.stdin.readline().rstrip())
    combinedMsg = ""
    for line in range(numLines):
        a = sys.stdin.readline().rstrip()
        combinedMsg = combinedMsg + a

    letterRelativeFreq = runCase(combinedMsg)
    for letter, relFreq in letterRelativeFreq.values():
        print(f"{letter}: {relFreq}%")


    
    

    


    

    