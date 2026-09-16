import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

#forumala is dx/dy (d = delta)
def calcSlopeBetweenPts(x1, y1, x2, y2):
    dx = x2 - x1 #no mention of what to do if this is 0
    dy = y2 - y1 

    return (dy / dx)

def isSafeLanding(slopeToStart, slopeToEnd):
    startIsSafe = (slopeToStart <= -0.8) and (slopeToStart >= -1.6)
    endIsSafe = (slopeToEnd <= -0.8) and (slopeToEnd >= -1.6)
    return (startIsSafe and endIsSafe)


for n in range(cases):
    numPlanes = int(sys.stdin.readline().rstrip())
    for plane in range(numPlanes):
        planeName = sys.stdin.readline().rstrip()

        planeCoords = sys.stdin.readline().rstrip()
        planeCoords = planeCoords.split(",")
        planeX = float(planeCoords[0])
        planeY = float(planeCoords[1])

        landingZoneStart = sys.stdin.readline().rstrip()
        landingZoneStart = landingZoneStart.split(",")
        landingZoneStartX = float(landingZoneStart[0])
        landingZoneStartY = float(landingZoneStart[1])

        landingZoneEnd = sys.stdin.readline().rstrip()
        landingZoneEnd = landingZoneEnd.split(",")
        landingZoneEndX = float(landingZoneEnd[0])
        landingZoneEndY = float(landingZoneEnd[1])

        slopeToStart = calcSlopeBetweenPts(planeX, planeY, landingZoneStartX, landingZoneStartY)
        slopeToEnd = calcSlopeBetweenPts(planeX, planeY, landingZoneEndX, landingZoneEndY)
        safeLanding = isSafeLanding(slopeToEnd, slopeToStart)
        if (safeLanding):
            print(f"{planeName}, Clear To Land!")
        else:
            print(f"{planeName}, Abort Landing!")
        

