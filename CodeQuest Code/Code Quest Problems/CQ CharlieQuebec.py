

import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()
toPrint = []



alphabetDict = {"A":"Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta", "E":"Echo", "F":"Foxtrot",
                "G":"Golf", "H":"Hotel", "I":"India", "J":"Juliet", "K":"Kilo",
                "L":"Lima", "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa", 
                "Q":"Quebec", "R":"Romeo", "S":"Sierra", "T":"Tango", "U":"Uniform", 
                "V":"Victor", "W":"Whiskey", "X":"Xray", "Y":"Yankee", "Z":"Zulu"}


def convertToICAO(msg, alphabetDict):
    newString = ""
    msg = msg.upper()
    for index, word in enumerate(msg):
        for letter in word:
            if letter != " " and index < len(msg) - 1:
                if msg[index + 1] != " ":
                    newString = newString + alphabetDict[letter] + "-"
                else:
                    newString = newString + alphabetDict[letter]
            elif letter != " ":
                newString = newString + alphabetDict[letter]
            else:
                newString = newString + " "
    return newString

for caseNum in range(cases):
    numLines = int(sys.stdin.readline().rstrip())
    for line in range(numLines):
        case = sys.stdin.readline().rstrip()
        toICAO = convertToICAO(case, alphabetDict)
        toPrint.append(toICAO)



for msg in toPrint:
    print(msg)
    

    