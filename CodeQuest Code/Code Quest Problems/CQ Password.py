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

def meetsLengthReq(password):
    return (len(password) >= 8)

def containsUpper(password):
    alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in password:
        if letter in alphabetUpper:
            return True
    return False

def containsLower(password):
    alphabetLower = "abcdefghijklmnopqrstuvwxyz"
    for letter in password:
        if letter in alphabetLower:
            return True
    return False

def containsNum(password):
    numbers = "0123456789"
    for letter in password:
        if letter in numbers:
            return True
    return False

def containsSpecialChar(password):
    #plan for this is a bit diff
    #theres lots of special charachters
    #so waht im gonna do is 
    #put all the letters and numbers, 
    #then if a char is NOT on the letters and numbers string, 
    #then we say true

    letterAndNumbers = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in password:
        if letter not in letterAndNumbers:
            return True 
    return False

def repeatingChars(password):
    length = len(password)
    for index, letter in enumerate(password):
        if (index < length - 2): #so we check last 3 letters still if need be
            nextLetter = password[index + 1]
            letterAfterThat = password[index + 2]
            if (letter == nextLetter and letter == letterAfterThat):
                return False
            
    return True

for value in input_nums:
    #make function for each criteria, returns boolean on whether its met
    #only say valid if all are true
    numCorrectChar = 0 #so the acc requirments are that of the uppercase, lowercase, # and speical char, only 3/4 need ot be true
    #numCorrectChar is the variable that tracks that, so just check if its >=3

    lengthStatus = meetsLengthReq(value)
    uppercaseStatus = containsUpper(value)
    lowercaseStatus = containsLower(value)
    numStatus = containsNum(value)
    specialCharStatus = containsSpecialChar(value)
    repeatingStatus = repeatingChars(value)

    if lowercaseStatus == True:
        numCorrectChar += 1
    if uppercaseStatus == True:
        numCorrectChar += 1
    if numStatus == True:
        numCorrectChar += 1
    if specialCharStatus == True:
        numCorrectChar += 1

    

    if (lengthStatus and (numCorrectChar >= 3) and repeatingStatus):
        print("VALID")
    else:
        print("INVALID")