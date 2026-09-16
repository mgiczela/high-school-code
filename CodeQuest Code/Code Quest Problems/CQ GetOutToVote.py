

import sys
import math
import string
from decimal import Decimal, ROUND_HALF_UP
cases = int(sys.stdin.readline().rstrip())

def runOneElectionRound(votersList, candidatesDict):
    for vote in votersList:
        currentVote = vote[0]
        candidatesDict[currentVote] += 1


    #after all votes tallied, return winner
    numVoters = len(votersList)

    mostVotesCandidate = ""
    mostVotesNumber = 0
    mostVotesPercentage = 0
    candidatesPercentageDict = {}

    lowestNumVotes = 999999999999999999999
    candidateWithLeastNumVotes = ""

    

    for candidate, numVotesForCandidate in candidatesDict.items():
        numVotesForCandidate = Decimal(str(numVotesForCandidate))
        perecentageForCandidate = (numVotesForCandidate / Decimal(str(numVoters)) * Decimal("100")).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        candidatesPercentageDict[candidate] = perecentageForCandidate
        
        if numVotesForCandidate > mostVotesNumber:
            mostVotesNumber = numVotesForCandidate
            mostVotesCandidate = candidate
            mostVotesPercentage = perecentageForCandidate
        
        if numVotesForCandidate < lowestNumVotes:
            lowestNumVotes = numVotesForCandidate
            candidateWithLeastNumVotes = candidate


    return candidatesPercentageDict, candidatesDict, mostVotesCandidate, mostVotesNumber, mostVotesPercentage, candidateWithLeastNumVotes



for caseNum in range(cases):
    electionInfo = sys.stdin.readline().rstrip()
    electionInfo = electionInfo.split(" ")

    numVoters = int(electionInfo[0])
    numCandidates = int(electionInfo[1])

    votersList = []
    for voter in range(numVoters):
        a = sys.stdin.readline().rstrip()
        votersList.append(a)

    #we arent told its guarateed to be letters for candidates
    #so dont assume that

    #use random voter to get the charachter for each candidate in a dict
    candidatesDict = {}
    for candidate in votersList[0]:
        candidatesDict.update({candidate: 0})
    
    numElectionRounds = 1
    foundWinner = False
    winningCandidate = "_if ur seeing this somethings wrong fix it now!!_"
    mostVotesCandidate = ""
    mostVotesNumber = 0
    mostVotesPercentage = Decimal("0")
    candidateWithLeastNumVotes = ""

    while foundWinner == False:
        #    return candidatesPercentageDict, candidatesDict, mostVotesCandidate, mostVotesNumber, mostVotesPercentage

        candidatesPercentageDict, candidatesDict, mostVotesCandidate, mostVotesNumber, mostVotesPercentage, candidateWithLeastNumVotes = runOneElectionRound(votersList, candidatesDict)
        if mostVotesNumber > Decimal(numVoters) / 2:
            winningCandidate = mostVotesCandidate
            foundWinner = True
            break
        #if no winner, then for any voter who ranked em first remove them and run another election round
        for i in range(len(votersList)):
            if votersList[i][0] == candidateWithLeastNumVotes:
                votersList[i] = votersList[i][1:]

        #remove the elimited candidate from all the ballots, regardless of what ranking the person put em at
        for i in range(len(votersList)):
            updatedVote = ""
            for candidate in votersList[i]:
                if candidate != candidateWithLeastNumVotes:
                    updatedVote += candidate
            votersList[i] = updatedVote

        #reset the variables that need resetting
        candidatesPercentageDict.clear()
        candidatesDict.pop(candidateWithLeastNumVotes)
        for candidate, numVotes in candidatesDict.items():
            candidatesDict[candidate] = 0
        mostVotesCandidate = ""
        mostVotesNumber = 0
        mostVotesPercentage = Decimal("0")
        candidateWithLeastNumVotes = ""

        #add 1 to numROunds of elecitons count
        numElectionRounds += 1


    print(f"Candidate {winningCandidate} won with {mostVotesPercentage}% of the vote after {numElectionRounds} tallies")



    

    

    