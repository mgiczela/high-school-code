'''
so

plan is: go thru each letter, add to a dictionary
then in the dictionary find letter with most counts
return that #

'''




import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)


for case in inputs:
    caseNoSpaces = case.replace(" ", "")
    #that makes it easier to process
    word_letters = {}
    for letter in caseNoSpaces:
            if letter in word_letters:
                word_letters[letter] += 1
            else: 
                word_letters.update({letter : 1})
    
    mostCommonLetterCount = 0
    for letterCount in word_letters:
         if word_letters[letterCount] > mostCommonLetterCount:
              mostCommonLetterCount = word_letters[letterCount]
    print(mostCommonLetterCount)

    

    