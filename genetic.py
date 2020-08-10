import utilities
import random
from robot import Robot

def crossGen(probList,robots):
    newGen=[robots[0]+1]
    i=1
    while(i<=10):
        rA=chooseRobot(probList)+1
        rB=chooseRobot(probList)+1
        robotA=robots[rA]
        robotB=robots[rB]
        newGen.append(crossRobots(robotA,robotB,rA,rB))
        i+=1
    #utilities.printRobots(newGen)
    return newGen

def chooseRobot(lst):
    value= random.randint(0,99)
    #print("List: ",lst)
    sumProb=0
    for i in range(len(lst)):
        sumProb+=lst[i]
        if(value<=sumProb):
            return i
    return -1

def crossRobots(robotA,robotB,rA,rB):
    newCamera=crossing2bits(robotA.camera,robotB.camera)
    newEngine=crossing2bits(robotA.engine,robotB.engine)
    #print("New Camera: ",newCamera,"New Engine:" ,newEngine)
    newBattery=crossingBatteries(robotA.battery,robotB.battery)
    #print("New Battery: ",newBattery)
    #print("Prob 1: ",robotA.difficultProb[0]," Prob 2: ",robotB.difficultProb[0])
    dp,nfp,cdp=crossAllProbs(robotA,robotB)
    #print("NewProb: ",newProb)
    return Robot(newBattery/80,newCamera,newEngine,dp,nfp,cdp,rA,rB)

def crossingBatteries(genA,genB):
    SgenA=normalizeBinaryProb("{0:b}".format(genA),8)
    SgenB=normalizeBinaryProb("{0:b}".format(genB),8)
    breakingPoint=random.randint(1,7)
    #print("GenA: ",genA, " GenB: ",genB)
    #print("String genA: ",SgenA," String genB: ",SgenB)
    #print("The breaking point is: ",breakingPoint)
    NewGenA=SgenA[0:breakingPoint]+SgenB[breakingPoint:len(SgenB)]
    NewGenB=SgenB[0:breakingPoint]+SgenA[breakingPoint:len(SgenB)]
    #print("New String A: ",NewGenA," New Srtring B: ",NewGenB)
    #print("Decimal: ",genA," Binario: ",NewGenA)
    #print(NewGenB)
    #print("------------------------------")
    intGenA=int(NewGenA,2)
    intGenB=int(NewGenB,2)
    if(intGenA>240):
        intGenA=240
    if(intGenB>240):
        intGenB=240
    choose=random.randint(1,2)
    if(choose==1):
        return intGenA
    else:
        return intGenB

def crossingProbabilities(genA,genB):
    SgenA=normalizeBinaryProb("{0:b}".format(genA),7)
    SgenB=normalizeBinaryProb("{0:b}".format(genB),7)
    breakingPoint=random.randint(1,6)
    #print("String genA: ",SgenA," String genB: ",SgenB)
    #print("The breaking point is: ",breakingPoint)
    NewGenA=SgenA[0:breakingPoint]+SgenB[breakingPoint:len(SgenB)]
    NewGenB=SgenB[0:breakingPoint]+SgenA[breakingPoint:len(SgenA)]
    #print("New String A: ",NewGenA," New Srtring B: ",NewGenB)
    intGenA=int(NewGenA,2)
    intGenB=int(NewGenB,2)
    if(intGenA>100):
        intGenA=100
    if(intGenB>100):
        intGenB=100
    choose=random.randint(1,2)
    if(choose==1):
        return intGenA
    else:
        return intGenB

def crossing2bits(genA,genB):
    SgenA=normalizeBinaryProb("{0:b}".format(genA),2)
    SgenB=normalizeBinaryProb("{0:b}".format(genB),2)
    #print("String genA: ",SgenA," String genB: ",SgenB)
    newGenA=int(SgenA[0]+SgenB[1],2)
    newGenB=int(SgenB[0]+SgenA[1],2)
    #print("New String A: ",newGenA," New Srtring B: ",newGenB)
    if(newGenA==0):
        return newGenB
    if(newGenB==0):
        return newGenA
    choose=random.randint(1,2)
    if(choose==1):
        return newGenA
    else:
        return newGenB

def normalizeBinaryProb(binaryString,bits):
    if(len(binaryString)==bits):
        return binaryString
    else:
        while(len(binaryString)<bits):
            binaryString="0"+binaryString
    return binaryString

def crossAllProbs(robotA,robotB):
    newDiff=[]
    newNearFar=[]
    newCostDist=[]
    for i in range(len(robotA.difficultProb)):
        newDiff.append(crossingProbabilities(robotA.difficultProb[i],robotB.difficultProb[i]))
    for i in range(len(robotA.nearFarProb)):
        newNearFar.append(crossingProbabilities(robotA.nearFarProb[i],robotB.nearFarProb[i]))
    for i in range(len(robotA.costDistProb)):
        newCostDist.append(crossingProbabilities(robotA.costDistProb[i],robotB.costDistProb[i]))
    return newDiff,newNearFar,newCostDist

def mutation(robots):
    totalMutation=random.randint(1,3)
    for i in range(totalMutation):
        randomBot=random.randint(1,10)
        mutateRobot(robots[randomBot])
    pass

def mutateRobot(robot):
    hardware=random.randint(1,3)
    MCamera=normalizeBinaryProb("{0:b}".format(robot.camera),2) #Camera
    MEngine=normalizeBinaryProb("{0:b}".format(robot.engine),2) #Engine
    MBattery=normalizeBinaryProb("{0:b}".format(robot.battery),8) #Battery
    if(hardware==1):
        robot.camera=int(changeDigit(MCamera),2)
    elif(hardware==2):
        robot.engine=int(changeDigit(MEngine),2)
    else:
        pass
        #robot.battery=int(changeDigit(MEngine),2)

    probabilities=random.randint(1,3)
    if(probabilities==1):
        DiffProb=robot.difficultProb[probabilities-1]
        MDiffProb=normalizeBinaryProb("{0:b}".format(DiffProb),7) 
        robot.difficultProb[probabilities-1]=int(changeDigit(MDiffProb),2)
    elif(probabilities==2):
        NearFarProb=robot.nearFarProb[(probabilities*2)-1]
        MNearFar=normalizeBinaryProb("{0:b}".format(NearFarProb),7) 
        robot.nearFarProb[(probabilities*2)-1]=int(changeDigit(MNearFar),2)
    else:
        CostDistProb=robot.costDistProb[(probabilities*4)-1]
        MCostDist=normalizeBinaryProb("{0:b}".format(CostDistProb),7) 
        robot.costDistProb[(probabilities*4)-1]=int(changeDigit(MCostDist),2)
    
    

def changeDigit(binaryString):
    position=random.randint(0,len(binaryString)-1)
    if(binaryString[position]==1):
        binaryString=binaryString[0:position]+"0"+binaryString[position+1:len(binaryString)]
    else:
        binaryString=binaryString[0:position]+"1"+binaryString[position+1:len(binaryString)]
    return binaryString