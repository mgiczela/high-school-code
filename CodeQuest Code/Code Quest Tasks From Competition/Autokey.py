import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

def makeCyptherAlphabet(letter, alphabetUppercase):
    indexOfLetter = alphabetUppercase.index(letter)
    alpabetBeforeLetter = alphabetUppercase[0:indexOfLetter]
    alphabetAfterAndIncludingLetter = alphabetUppercase[indexOfLetter:]

    return (alphabetAfterAndIncludingLetter + alpabetBeforeLetter)

uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for n in range(cases):
    uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encriptKeyword = sys.stdin.readline().rstrip()
    encryptedMessage = ""

    

    message = sys.stdin.readline().rstrip()
    message = message.upper()
    for letter in message:
        if letter not in uppercaseAlphabet:
            message = message.replace(letter, "")

    encriptKeyword = encriptKeyword + message

    

    for index, letter in enumerate(message):
        currentLetterAlphabet = makeCyptherAlphabet(encriptKeyword[index], uppercaseAlphabet)
        indexOfLetterInRegularAlphabet = uppercaseAlphabet.index(letter)
        encryptedMessage += currentLetterAlphabet[indexOfLetterInRegularAlphabet]
    print(encryptedMessage)
       






    