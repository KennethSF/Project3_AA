from ground import Ground
from robot import Robot
import random

def createMap():
    ground=Ground("ground.txt")
    generation=createRobots()

def randValue():
    return random.randint(1,3)
    
def createRobots():
    gen=[1]
    for i in range(10):
        gen.append(Robot(randValue(),randValue(),randValue(),[],[],[],-1,-1))
    return gen


def printRobots(gen):
    for i in range(len(gen)):
        if(i!=0):
            gen[i].printRobot(i)
        else:
            print("********************************")
            print("")
            print("          Generation: ",gen[i])
            print("")
            print("********************************")

def writeInFile(gen,file):
    # f.write("This is line %d\r\n" % (i+1))
    for i in range(len(gen)):
        if(i!=0):
            gen[i].writeRobot(i,file)
        else:
            file.write("********************************\r\n")
            file.write("\r\n")
            file.write("          Generation: %d\r\n" % gen[i])
            file.write("\r\n")
            file.write("********************************\r\n")

def average(lst):
    nonZero=0
    for i in range(len(lst)):
        if(lst[i]!=0):
            nonZero+=1
    return sum(lst)/nonZero

def sumLst(lst):
    return sum(lst)

def printList(lst):
    print(*lst, sep = ", ")  

def realProb(lst):
    probLst=[]
    N=sumLst(lst)
    for i in range(len(lst)):
            probLst.append(round(lst[i]/N*100,2))
    return probLst

def newProb(probLst):
    newProbLst=probLst
    for i in range(len(probLst)):
        if(newProbLst[i]!=0):
            newProbLst[i]=100/newProbLst[i]
        else:
            newProbLst[i]=0
    return newProbLst

def normalizeProb(probLst):
    normLst=probLst
    prob=sumLst(normLst)
    for i in range(len(normLst)):
        normLst[i]=round(100*normLst[i]/prob,2)
    return normLst

def randomNumber():
    return random.randint(0,100)

def partialSum(lst,max):
    aux=0
    for i in range (max):
        aux+=lst[i]
    return aux

def pathChoosen(value):
    switcher = {
        0: "North",
        1: "Northeast",
        2: "East",
        3: "Southeast",
        4: "South",
        5: "Southwest",
        6: "West",
        7: "Northwest",        
    }
    print (switcher.get(value, "Invalid value"))

def roboticTravel(robots,map):
    for i in range(len(robots)):
        if(i>0):
            robots[i].traverseTerrain(map)

def randomDifficult(ammount,probList):
    for i in range (ammount):
        probList.append(random.randint(0,100))
    
def choosePath(lst):
    value= random.randint(0,sum(lst))
    #print("List: ",lst)
    sumProb=0
    for i in range(len(lst)):
        sumProb+=lst[i]
        if(value<=sumProb):
            return i
    return -1

def discardDifficult(lst,minD,maxD,difficult):
    #print("Voy a trabajar con: ",difficult)
    for i in range(len(lst)):
        if(difficult==0):
            if(lst[i]>minD):
                lst[i]=-1
        elif(difficult==2):
            if(lst[i]<maxD):
                lst[i]=-1
        else:
            if(lst[i]>=maxD or lst[i]<=minD):
                lst[i]=-1
    return lst

def discardNearFar(lst,NoF,nearFarList):
    #print("len lista 1:",lst," len lista2: ",nearFarList)
    nof=-1
    if(NoF%2==0):
        nof=0
    else:
        nof=1
    for i in range(len(lst)):
        if(nearFarList[i]!=nof):
            lst[i]=-1
    return lst

def discardDistCost(lst,CoD,distanceList):
    cod=-1
    auxList=[]
    CoDList=[]
    if(CoD%2==0):
        for i in range(len(lst)):
            if(distanceList[i]!=-1 and distanceList[i]!=0):
                if(len(auxList)>0):
                    pass
                    #print("aux:",CoDList[0]," sfd:", distanceList[i])
                if(not auxList):
                    auxList.append(i)
                    CoDList.append(distanceList[i])
                elif(distanceList[i]<CoDList[0]):
                        auxList.clear()
                        CoDList.clear()
                        auxList=[i]
                        CoDList=[distanceList[i]]
                elif(distanceList[i]==CoDList[0]):
                    auxList.append(i)
                    CoDList.append(distanceList[i])
    else:
        for i in range(len(lst)):
            if(lst[i]!=-1 and lst[i]!=0):
                if(len(auxList)>0):
                    pass
                    #print("aux:",CoDList[0]," sfd:", lst[i])
                if(not auxList):
                    auxList.append(i)
                    CoDList.append(distanceList[i])
                elif(lst[i]<CoDList[0]):
                        auxList.clear()
                        CoDList.clear()
                        auxList=[i]
                        CoDList=[lst[i]]
                elif(lst[i]==CoDList[0]):
                    auxList.append(i)
                    CoDList.append(lst[i])
    #print(auxList)
    if(not auxList):
        return -1
    elif(len(auxList)==1):
        return auxList[0]
    else:
        randAux=random.randint(0,len(auxList)-1)
        return auxList[randAux]
    return 0

def checkList(lst):

    for i in range(len(lst)):
        if(lst[i]!=-1):
            return True
    return False

def printDetailedPositions(robots):
    i=1
    while(i<=10):
        robots[i].detailedPos(robots[0],i)
        i+=1
    print("----------------------------------------------")

def assignProbabilities(robots):

    i=1
    while(i<=10):
        randomDifficult(3,robots[i].difficultProb)
        randomDifficult(6,robots[i].nearFarProb)
        randomDifficult(12,robots[i].costDistProb)
        i+=1


def distancePoint(robots):
    row=0
    column=19
    distance=[]
    for i in range(len(robots)):
        if(i!=0):
            distance.append(abs(row-robots[i].pos[0])+abs(column-robots[i].pos[1]))
    
    distancePoints=realProb(distance)
    distancePoints=newProb(distancePoints)
    distancePoints=normalizeProb(distancePoints)
    return distancePoints

    