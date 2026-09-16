

import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
inputs = list()


for caseNum in range(cases):
    a = sys.stdin.readline().rstrip()
    inputs.append(a)

def findComaptibleAgents(agentLetter, agentScore, allAgentScores): #the allAgentScores list is in the format desc below 
    validPartners = []

    for agent in allAgentScores:
        letterOfAgent = agent[0]
        currentAgentScore = int(agent[1])
        
    #skip over the current agent (ie agent a cannot be parter wirh agent a [himself])
        
        if(currentAgentScore <= agentScore + 10 and currentAgentScore >= agentScore - 10 and letterOfAgent != agentLetter):
            validPartners.append(agent)

    return validPartners
            




for case in inputs:
    #plan:
    #go thru and for each agent: make a team for them (of all valid agents w/ score diff <= 10)
    #each agent team goes into a dictionary of the format: number of agents:list of agents
    #go thru dicitonary and find largest key, then print that out in the right format

    #as for formatting and acessing the data: case.split(" ") as usual
    #then for each value in there (in the format letter=score), use case.split("=") and put hte value bakc in the list
    #so the data is in the form ((a, 12), (b, 3), (c, 46)) , so a list of lists

    #formatting data:
    case = case.split(" ")
    caseFormatted = []
    for value in case:
        temp = value.split("=")
        caseFormatted.append(temp)

    #data is now in the format decribed above

    #stores how many and who compatible agents for each agent
    
    compatibleAgentsDict = {}

    for agent in caseFormatted:
        letterOfAgent = agent[0]
        currentAgentScore = int(agent[1])
        currentAgentValidPartners = findComaptibleAgents(letterOfAgent, currentAgentScore, caseFormatted)
        compatibleAgentsDict[(currentAgentValidPartners)] = len(currentAgentValidPartners)

    #so update, i changed the dict to be list of compativlae agnets:num of compatible agents
    #so data dont get overriden if 2 have same length

    #now go find longest, and deal with ties
    numMostCompatibles = 0
    biggestCompatiblesList = []
    mostCompsTiesList = [] #list if theres a tie for who has most
    for key, value in compatibleAgentsDict.values():
        #key = list of agents
        #value is num of agents
        if (value > numMostCompatibles):
            numMostCompatibles = value
            biggestCompatiblesList = key
            mostCompsTiesList.clear() #clear cuz that means all the old ties werent the max so we dont care abt them
        elif (value == numMostCompatibles):
            mostCompsTiesList.append(key)

    if (len(mostCompsTiesList) == 0):
        #outright winner

        #PRINT OUT THE LIST IN THE FORMAT
        toPrint = ""
        for agent in biggestCompatiblesList:
            toPrint += agent[0] + " "
        toPrint = toPrint.strip()#get rid of last space at the end, .strip only removes spaceas at start and end so we're fine w uising it
        print(toPrint)
    else:
        ##so many thing are wrong imma jus.,. do another one
        print("fix this progrma leter i cannot w ts")

        



    
    








    


    

    