import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    numCards = int(sys.stdin.readline().rstrip())
    cardsList = []
    for i in range(numCards):
        card = sys.stdin.readline().rstrip()
        cardsList.append(card)
    whatWeLookFor = sys.stdin.readline().rstrip()

    numOfDesiredCard = 0
    for card in cardsList:
        if card == whatWeLookFor:
            numOfDesiredCard += 1
    print(numOfDesiredCard)