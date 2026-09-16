import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()
toPrint = []

for case in range(cases):
    numRowsAndCols = sys.stdin.readline().rstrip()
    numRowsAndCols = numRowsAndCols.split(" ")
    numRowsGiven = int(numRowsAndCols[0])
    numColsGiven = int(numRowsAndCols[1])

    numRowsDesired = numColsGiven
    numColsDesired = numRowsGiven

    #plan is gonna be to store everything in index n in a list
    #then go thru and list 1 will be the first row and so on 
    #make sure ot add commas but yea
    #all that stored in massiveDataList
    massiveDataList = []
    for i in range(numColsGiven):
        massiveDataList.append([])

    for inputLine in range(numRowsGiven):
        data = sys.stdin.readline().rstrip()
        data = data.split(",")
        for index, item in enumerate(data):
            try:
                massiveDataList[index].append(item)
            except:
                pass #sometimes if theres a blank space at end (like in the 3 num sequence 4,5,,), theres an extra empty space
                    #we can just ignore it since its extra empty space that we dont care abt

    #now we have the data where the list at index 0 is what supposed to be the first row, index 1 the second and so on
    #print it out with the commas
    for row in massiveDataList:
        stringToPrint = ""
        for index, number in enumerate(row):
            if index != len(row) - 1:
                stringToPrint = stringToPrint + (f"{number},")
            else:
                stringToPrint = stringToPrint + (f"{number}")
        print(stringToPrint)


    

