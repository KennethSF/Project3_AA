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
    for i in range(1):
        gen.append(Robot(randValue(),randValue(),randValue()))
    return gen

def printRobots(gen):
    for i in range(len(gen)-1):
        gen[i+1].printRobot(i)

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

# def newProb(costLst,probLst):
#     print("New prob")
#     newProbLst=probLst
#     avrg=average(costLst)
    
#     for i in range(len(costLst)):
#         if(costLst[i]<=avrg):
#             newProbLst[i]=newProbLst[i]*2
#         else:
#             newProbLst[i]=newProbLst[i]/2
#     return newProbLst

def newProb(costLst,probLst):
    newProbLst=probLst
    for i in range(len(costLst)):
        newProbLst[i]=100/newProbLst[i]
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
        1: "North",
        2: "Northeast",
        3: "East",
        4: "Southeast",
        5: "South",
        6: "Southwest",
        7: "West",
        8: "Northwest",        
    }
    print (switcher.get(value, "Invalid value"))