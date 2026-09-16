

import sys
import math
import string
from decimal import Decimal, ROUND_HALF_UP


def getLetterGrade(percentGrade):
    letter = ""
    if percentGrade >= 90:
        letter = "A"
    elif percentGrade >= 80:
        letter = "B"
    elif percentGrade >= 70:
        letter = "C"
    elif percentGrade >= 60:
        letter = "D"
    else:
        letter = "F"

    return letter

numCases = int(sys.stdin.readline().rstrip())



for n in range(numCases):
    line1 = sys.stdin.readline().rstrip()
    temp1 = line1.split(" ")

    numStudents = int(temp1[0])
    answerKey = temp1[1]
    numQuestions = len(answerKey)

    studentsList = []
    for i in range(numStudents):
        a = sys.stdin.readline().rstrip()
        studentsList.append(a)

    for student in studentsList:
        temp2 = student.split(" ")
        studentName = temp2[0]
        studentResponses = temp2[1]
        numCorrect = 0
        for index, response in enumerate(studentResponses):
            if(response == answerKey[index]):
                numCorrect += 1
        
        numCorrect = Decimal(str(numCorrect))
        numQuestions = Decimal(str(numQuestions))

        percentGrade = (numCorrect / numQuestions ) * Decimal("100")

        percentGrade = (percentGrade).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        gradeAsLetter = getLetterGrade(percentGrade)
        print(f"{studentName} {percentGrade}% {gradeAsLetter}")
            





    