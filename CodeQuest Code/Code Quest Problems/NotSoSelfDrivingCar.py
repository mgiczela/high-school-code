"""

3 cases:
- we'd hit in 1 or less sec: SWERVE
- if dist - vel <= 0

- we'd hit in 5 or less sec: BRAKE
- if dist - 5(vel) <= 0

else: SAFE

"""
import sys
import math
import string
#collect input and add into list
cases = int(sys.stdin.readline().rstrip())
input_strings = list()
for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    input_strings.append(a)
# print(input_strings)

for value in input_strings:
    case = value.split(':')
    #conversion
    velocity = float(case[0])
    distance = float(case[1])
    #math
    if distance - velocity <= 0:
        print("SWERVE")
    elif distance - (5 * velocity) <= 0:
        print("BRAKE")
    else:
        print("SAFE")
    

