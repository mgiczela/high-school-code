"""
split each input to its parts (name, class, x and y)
add each input(list) to master list (2d array)

for each  ship (repeat until master list of ships is empty)
find smallest x coord of ships, print and remove 
go thru and based on class (a,b,c) update x pos for each ship


"""

import sys
import math
import string

destroyedShips = []

def run_case():
    numShips = int(sys.stdin.readline().rstrip())
    inputs = list()
    masterList = []

    for caseNum in range(numShips):
        a = sys.stdin.readline().rstrip()
        inputs.append(a)

    def addShip(ship):
        splitOne = ship.split(':')
        name_and_class = splitOne[0].split("_")
        x_and_y = splitOne[1].split(",")
        x_and_y[0] = int(x_and_y[0])
        x_and_y[1] = int(x_and_y[1])

        shipList = []
        name_and_class.append(x_and_y[0])
        name_and_class.append(x_and_y[1])
        shipList = name_and_class

        masterList.append(shipList)


    for ship in inputs:
        addShip(ship)

    while len(masterList) > 0:
        smallestX = masterList[0][2]
        indexOfClosestShip = 0

        for index, ship in enumerate(masterList):
            if ship[2] < smallestX:
                smallestX = masterList[index][2]
                indexOfClosestShip = index
            
        #now that we found lowest x, check if it repeats
        sameXCoords = []
        for index, ship in enumerate(masterList):
            if smallestX == ship[2]:
                sameXCoords.append([ship[3], index])

        #of those lowest x's, see which one has biggest y (thats the one we destroy)
        if len(sameXCoords) != 0:
            largestY = sameXCoords[0][0]
            for index, y in enumerate(sameXCoords):
                if y[0] > largestY:
                    largestY = sameXCoords[index][0]
                    indexOfClosestShip = sameXCoords[index][1]
            
        #print(f"Destroyed Ship: {masterList[indexOfClosestShip][0]} xLoc: {masterList[indexOfClosestShip][2]}")
        destroyedShips.append(f"Destroyed Ship: {masterList[indexOfClosestShip][0]} xLoc: {masterList[indexOfClosestShip][2]}")
        masterList.pop(indexOfClosestShip)

        #update x position based on class (a: -10, b: -20, c: -30) after one round
        for ship in masterList:
            if ship[1] == "A":
                ship[2] -= 10
            elif ship[1] == "B":
                ship[2] -= 20
            else:
                ship[2] -= 30



cases = int(sys.stdin.readline().rstrip())
for case in range(cases):
    run_case()

for destroyedShip in destroyedShips:
    print(destroyedShip)

