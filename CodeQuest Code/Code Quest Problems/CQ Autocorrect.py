"""
take in the input for number of cases

for each case:

take in the 2 #'s (A and B) of the dictionary words and the misspelled words

make a list called dictionary, that list holds the first A input values
make a list for the rest of the input values, called typoes

for every typo:
- make new list of words of same length
- iterate through dictionary list, find all words of same length and add to sameLenghtWords list
- if sameLength is just 1, automaticaly print out that word and move on to next case
- otherwise, go tru and for each word of same length:
    - make variable to track index of word wiht least differences
    - make variable to track the number of differences
    - go letter by letter in the word, compare to coresponding indexed letter in the typoed word:
        - if they dont match, add 1 to differneces counter
"""

import sys
import math
import string

def collectInputs():
    correctAndIncorrectWordNumbers = (sys.stdin.readline().rstrip())
    correctAndIncorrectWordNumbersSplit = correctAndIncorrectWordNumbers.split(" ")
    numCorrectWords = int(correctAndIncorrectWordNumbersSplit[0])
    numIncorrectWords = int(correctAndIncorrectWordNumbersSplit[1])

    corrects = []
    incorrects = []
    
    
    for caseNum in range(numCorrectWords):
        a = sys.stdin.readline().rstrip()
        corrects.append(a)
    for caseNum in range(numIncorrectWords):
        a = sys.stdin.readline().rstrip()
        incorrects.append(a)
    return corrects, incorrects 
        

def getSameLength(incorrectWord, allCorrectWords):
    length = len(incorrectWord)
    wordsOfSameLen = []
    for word in allCorrectWords:
        if len(word) == length:
            wordsOfSameLen.append(word)
    return wordsOfSameLen

def findLeastNumDifferences(incorrectWord, correctWords):
    numDifferentLetters = []
    for correctWord in correctWords:
        numDifferences = 0
        for index, letter in enumerate(correctWord):
            if letter != incorrectWord[index]:
                numDifferences += 1
        numDifferentLetters.append(numDifferences)
    
    indexofLeastDifferences = 0
    leastDifferences = 999999999999
    for index, num in enumerate(numDifferentLetters):
        if num < leastDifferences:
            leastDifferences = num
            indexofLeastDifferences = index
    return(correctWords[indexofLeastDifferences])
        
    


autocorrectedWords = []

cases = int(sys.stdin.readline().rstrip())
for case in range(cases):
    corrects = []
    incorrects = []
    corrects, incorrects = collectInputs()

    for incorrectWord in incorrects:
        correctWordsOfSameLen = getSameLength(incorrectWord, corrects)
        if len(correctWordsOfSameLen) == 1:
            autocorrectedWords.append(correctWordsOfSameLen[0]) #if only 1 word has same length, autocorrect to that one
        else:
            #if there are multiple, run a funciton that does the algoritm to find one with fewest differences:
            word = findLeastNumDifferences(incorrectWord, correctWordsOfSameLen)
            autocorrectedWords.append(word)

for word in autocorrectedWords:
    print(word)


