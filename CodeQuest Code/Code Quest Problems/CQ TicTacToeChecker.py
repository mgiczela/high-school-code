
import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)

def doesXWin(boardAsStr):
    currentWinStatus = False #store whether x's won
    foundResult = False #keep track of whether we found result
    #keep goin until a win is found
    symbol = "X"
    while foundResult == False:
        #this is the board btw (as indexes of the boardOfStr)
        # 0 1 2
        # 3 4 5
        # 6 7 8

        # x x x
        # x x x
        # x x x

        #check rows
        row1 = boardAsStr[0] == symbol and boardAsStr[1] == symbol and boardAsStr[2] == symbol
        row2 = boardAsStr[3] == symbol and boardAsStr[4] == symbol and boardAsStr[5] == symbol
        row3 = boardAsStr[6] == symbol and boardAsStr[7] == symbol and boardAsStr[8] == symbol
        if (row1 or row2 or row3):
            currentWinStatus = True
            foundResult = True
            break
        #check columns
        col1 = boardAsStr[0] == symbol and boardAsStr[3] == symbol and boardAsStr[6] == symbol
        col2 = boardAsStr[1] == symbol and boardAsStr[4] == symbol and boardAsStr[7] == symbol
        col3 = boardAsStr[2] == symbol and boardAsStr[5] == symbol and boardAsStr[8] == symbol
        if (col1 or col2 or col3):
            currentWinStatus = True
            foundResult = True
            break
        #chekc diagonals
        diag1 = boardAsStr[0] == symbol and boardAsStr[4] == symbol and boardAsStr[8] == symbol
        diag2 = boardAsStr[6] == symbol and boardAsStr[4] == symbol and boardAsStr[2] == symbol
        if (diag1 or diag2):
            currentWinStatus = True
            foundResult = True
            break
        #if we are here and still nothing is true then theres a tie.
        currentWinStatus = False
        foundResult = True
    return currentWinStatus

def doesOWin(boardAsStr):
    currentWinStatus = False #store whether x's won
    foundResult = False #keep track of whether we found result
    #keep goin until a win is found
    symbol = "O"
    while foundResult == False:
        #this is the board btw (as indexes of the boardOfStr)
        # 0 1 2
        # 3 4 5
        # 6 7 8

        #check rows
        row1 = boardAsStr[0] == symbol and boardAsStr[1] == symbol and boardAsStr[2] == symbol
        row2 = boardAsStr[3] == symbol and boardAsStr[4] == symbol and boardAsStr[5] == symbol
        row3 = boardAsStr[6] == symbol and boardAsStr[7] == symbol and boardAsStr[8] == symbol
        if (row1 or row2 or row3):
            currentWinStatus = True
            foundResult = True
            break
        #check columns
        col1 = boardAsStr[0] == symbol and boardAsStr[3] == symbol and boardAsStr[6] == symbol
        col2 = boardAsStr[1] == symbol and boardAsStr[4] == symbol and boardAsStr[7] == symbol
        col3 = boardAsStr[2] == symbol and boardAsStr[5] == symbol and boardAsStr[8] == symbol
        if (col1 or col2 or col3):
            currentWinStatus = True
            foundResult = True
            break
        #chekc diagonals
        diag1 = boardAsStr[0] == symbol and boardAsStr[4] == symbol and boardAsStr[8] == symbol
        diag2 = boardAsStr[6] == symbol and boardAsStr[4] == symbol and boardAsStr[2] == symbol
        if (diag1 or diag2):
            currentWinStatus = True
            foundResult = True
            break
        #if we are here and still nothing is true then theres a tie.
        currentWinStatus = False
        foundResult = True
    return currentWinStatus

        
    



for case in inputs:
    #not most efficient buuut...
    #make a doesXwin and doesOwin meathod, if both false tie
    xWin = doesXWin(case)
    oWin = doesOWin(case)

    if (xWin == True):
        print(f"{case} = X WINS")
    elif (oWin == True):
        print(f"{case} = O WINS")
    else:
        print(f"{case} = TIE")

    

        
    

    