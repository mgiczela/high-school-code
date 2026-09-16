import sys
import math
import string
from decimal import Decimal, ROUND_HALF_UP
cases = int(sys.stdin.readline().rstrip())
toPrint = []

def mathmaticalFunction(inputX):
    #so math.sin doesnt reutnr 0 when it should be
    #like for sin(pi) it says 1.224e-16
    #so we cant chekc for exacly 0
    #basically if its close enough to 0
    #say 1.0e-10, and -1.0e-10
    if(abs(inputX) <= 1.0e-10):
        return 1
    else:
        
        result = math.sin(inputX) / inputX
    return result



def computeEulers(Xo, Yo, h, numberOfStepsToCompute):
    #only works for the given funciton sinx / x
    #yea
    #h is how big one step is
    
    # for Xo and Yo , the looks mroe like subscript so i use it 
    currentY = 0
    currentX = 0
    previousX = Xo
    previousY = Yo

    #we dont need calculating for start (n=0, initial values)
    for n in range(1, numberOfStepsToCompute+1):
        currentY = previousY + h*(mathmaticalFunction(previousX))
        currentX = h + previousX

        previousX = currentX
        previousY = currentY
    return currentY #only value we acc need as per insturcitons




for caseNum in range(cases):
    inputs = sys.stdin.readline().rstrip()
    inputs = inputs.split(" ")
    initialX = float(inputs[0])
    initialY = float(inputs[1])
    oneStepDistance = float(inputs[2])
    numIterations = int(inputs[3])

    Yfinal = computeEulers(initialX, initialY, oneStepDistance, numIterations)
    Yfinal = Decimal(str(Yfinal))
    YfinalRounded = (Yfinal).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
    yfinalFormatted = f"{YfinalRounded:.3f}".rstrip("0").rstrip(".")
    toPrint.append(yfinalFormatted)


for item in toPrint:
    print(item)