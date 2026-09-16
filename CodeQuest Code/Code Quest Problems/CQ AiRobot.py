"""
copy the last code for sorting the input, convert to int, use " " as delimiter, then preform the math and reutrn
"""

import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()

for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)

def move(direction, x, y):
    if direction == "N":
        y += 1
    elif direction == "E":
        x += 1
    elif direction == "S":
        y -= 1
    else:
        x -= 1
    return direction, x, y

def rotate(direction, rotation):
    if rotation == "L":
        if direction == "N":
            direction = "W"
        elif direction == "E":
            direction = "N"
        elif direction == "S":
            direction = "E"
        else:
            direction = "S"
    else:
        if direction == "N":
            direction = "E"
        elif direction == "E":
            direction = "S"
        elif direction == "S":
            direction = "W"
        else:
            direction = "N"
    return direction
    
# d, x, y = move("N", 0, 0)
    


for value in inputs:
    case = value.split(' ')
    x = int(case[0])
    y = int(case[1])
    direction = case[2]
    commands = case[3]

    for command in commands:
        if command == "A":
            direction, x, y = move(direction, x, y)
        elif command == "L":
            direction = rotate(direction, "L")
        else:
            direction = rotate(direction, "R")
    print(f"{x} {y} {direction}")

