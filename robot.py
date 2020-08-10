import utilities
import random

class Robot:

    def __init__(self,battery,camera,engine,dp,nfp,cdp,father,mother):
        self.battery=int(battery*80)
        self.batteryRemaining=int(battery*80)
        self.camera=int(camera)
        self.engine=int(engine)
        self.pos=[19,0]
        self.blocked=False #If blocked=true, the robot is on a blocked terrain or
                           #in on a terrain the engine can't handle
        self.previous=0
        self.difficultProb=dp
        self.nearFarProb=nfp
        self.costDistProb=cdp
        self.father=father
        self.mother=mother

    def nearOrFar(self,map,targetRow,targetColumn):
        goal=[0,19]
        actualRow=self.pos[0]
        actualColumn=self.pos[1]
        actualDistance=abs(goal[0]-actualRow)+abs(goal[1]-actualColumn)
        targetDistance=abs(goal[0]-targetRow)+abs(goal[1]-targetColumn)
        if (actualDistance>=targetDistance):
            return 0
        return 1

    def printRobot(self,pos):
        print("Robot #",pos," Battery: ", self.battery,
        " Camera: ", self.camera, " Engine: ", self.engine)
        print("My last position is Row: ",self.pos[0]," Column: ",self.pos[1])
        print("---------------------------------------------------")
    
    def writeRobot(self,pos,file):
        # f.write("This is line %d\r\n" % (i+1)),self.father,,self.mother
        file.write("Father Robot#"+str(self.father)+"     Mother Robot#"+str(self.mother)+"\n")
        file.write("Robot #"+str(pos)+" Battery: "+ str(self.battery)+
        " Camera: "+ str(self.camera)+ str(" Engine: ")+ str(self.engine)+"\n")
        file.write("My last position is Row: "+str(self.pos[0])+" Column: "+str(self.pos[1])+"\n")
        file.write("---------------------------------------------------\n")
    
    def traverseTerrain(self,map):
        #self.batteryAvailable() and
        while(self.batteryAvailable() and self.blocked==False):
            sight,distance,nearFar=self.cameraSight(map)
            #utilities.printList(normProbList)
            path=self.makeDecision(map,sight,nearFar,distance) #Gets the cardinal point to move
            #print("Patch chosen")
            #utilities.pathChoosen(path)
            steps=distance[path]
            self.move(map,path,steps)
            self.previous=path
            #self.remainingBattery()
        #print("TERMINADO")
        #self.whereAmI()
        

    def cameraSight(self,map):
            NORTH=WEST=-1 #Direction into the map
            SOUTH=EAST=1
            sight=[self.northSouthView(map,NORTH),self.collateralCardPointView(map,NORTH,EAST),
                self.eastWestView(map,EAST),self.collateralCardPointView(map,SOUTH,EAST),
                self.northSouthView(map,SOUTH),self.collateralCardPointView(map,SOUTH,WEST),
                self.eastWestView(map,WEST),self.collateralCardPointView(map,NORTH,WEST)]
            
            distance=[self.northSouthDistance(map,NORTH),self.collateralCardPointDistance(map,NORTH,EAST),
                self.eastWestDistance(map,EAST),self.collateralCardPointDistance(map,SOUTH,EAST),
                self.northSouthDistance(map,SOUTH),self.collateralCardPointDistance(map,SOUTH,WEST),
                self.eastWestDistance(map,WEST),self.collateralCardPointDistance(map,NORTH,WEST)]
            
            nearFar=[self.northSouthNearFar(map,NORTH),self.collateralCardPointNearFar(map,NORTH,EAST),
                self.eastWestNearFar(map,EAST),self.collateralCardPointNearFar(map,SOUTH,EAST),
                self.northSouthNearFar(map,SOUTH),self.collateralCardPointNearFar(map,SOUTH,WEST),
                self.eastWestNearFar(map,WEST),self.collateralCardPointNearFar(map,NORTH,WEST)]
            
            #utilities.printList(nearFar)
            
            return sight,distance,nearFar

    def sightAmmount(self,map):
        sight=self.cameraSight(map)
        print("North: ",sight[0])
        print("Northeast: ",sight[1])
        print("East: ",sight[2])
        print("Southeast: ",sight[3])
        print("South: ",sight[4])
        print("Southwest: ",sight[5])
        print("West: ",sight[6])
        print("Northwest: ",sight[7])

    def northSouthView(self,map,CardPoint): #Cardinal point
        aux=0 #Aux acumulates the cost of moving the robot
        auxRow=self.pos[0]
        column=self.pos[1]#This auxiliar gets the values of the possible position transfer
        for i in range(self.camera):
            if(auxRow==-1 or auxRow==20):
                break
            if(auxRow+CardPoint!=-1 and auxRow+CardPoint!=20):
                groundValue=int(map.ground[auxRow][column])
                aux+=groundValue #Gets the value of the ground where the robot is located
                auxRow+=CardPoint #Moves up or down
                
        return aux
    
    def eastWestView(self,map,CardPoint):
        aux=0 #Aux acumulates the cost of moving the robot
        row=self.pos[0]
        auxColumn=self.pos[1]#This auxiliar gets the values of the possible position transfer
        for i in range(self.camera):
            if(auxColumn==-1 or auxColumn==20):
                    break
            if(auxColumn+CardPoint!=-1 and auxColumn+CardPoint!=20):
                groundValue=int(map.ground[row][auxColumn])
                aux+=groundValue #Gets the value of the ground where the robot is located
                auxColumn+=CardPoint #Moves right or left
        return aux
    
    def collateralCardPointView(self,map,NorS,WorE):
        aux=0 #Aux acumulates the cost of moving the robot
        auxRow=self.pos[0]
        auxColumn=self.pos[1]#This auxiliar gets the values of the possible position transfer
        for i in range(self.camera):
            if(auxRow==-1 or auxRow==20 or auxColumn==-1 or auxColumn==20):
                break
            if(auxRow+NorS!=-1 and auxRow+NorS!=20 and auxColumn+WorE!=-1 and auxColumn+WorE!=20):
                groundValue=int(map.ground[auxRow][auxColumn])
                aux+=groundValue #Gets the value of the ground where the robot is located
                auxRow+=NorS #Moves up or down
                auxColumn+=WorE #Moves right or left
        return aux
    
    def northSouthDistance(self,map,CardPoint):
        aux=0
        auxRow=self.pos[0]
        column=self.pos[1]#This auxiliar gets the values of the possible position transfer
        for i in range(self.camera):
            if(auxRow==-1 or auxRow==20):
                break
            if(auxRow+CardPoint!=-1 and auxRow+CardPoint!=20):
                auxRow+=CardPoint
                aux+=1
        return aux

    def eastWestDistance(self,map,CardPoint):
        aux=0 #Aux acumulates the cost of moving the robot
        row=self.pos[0]
        auxColumn=self.pos[1]#This auxiliar gets the values of the possible position transfer
        for i in range(self.camera):
            if(auxColumn==-1 or auxColumn==20):
                    break
            if(auxColumn+CardPoint!=-1 and auxColumn+CardPoint!=20):
                auxColumn+=CardPoint
                aux+=1
        return aux

    def collateralCardPointDistance(self,map,NorS,WorE):
        aux=0 #Aux acumulates the cost of moving the robot
        auxRow=self.pos[0]
        auxColumn=self.pos[1]#This auxiliar gets the values of the possible position transfer
        for i in range(self.camera):
            if(auxRow==-1 or auxRow==20 or auxColumn==-1 or auxColumn==20):
                break
            if(auxRow+NorS!=-1 and auxRow+NorS!=20 and auxColumn+WorE!=-1 and auxColumn+WorE!=20):
                auxRow+=NorS
                auxColumn+=WorE
                aux+=1
        return aux
    
    def northSouthNearFar(self,map,CardPoint):
        auxRow=self.pos[0]
        column=self.pos[1]#This auxiliar gets the values of the possible position transfer
        #near_far=-1
        for i in range(self.camera):
            if(auxRow==-1 or auxRow==20):
                break
            if(auxRow+CardPoint!=-1 and auxRow+CardPoint!=20):
                auxRow+=CardPoint
        near_far=self.nearOrFar(map,auxRow,column)    
        return near_far
   
    def eastWestNearFar(self,map,CardPoint):
        row=self.pos[0]
        auxColumn=self.pos[1]#This auxiliar gets the values of the possible position transfer
        for i in range(self.camera):
            if(auxColumn==-1 or auxColumn==20):
                    break
            if(auxColumn+CardPoint!=-1 and auxColumn+CardPoint!=20):
                auxColumn+=CardPoint
        near_far=self.nearOrFar(map,row,auxColumn)
        return near_far

    def collateralCardPointNearFar(self,map,NorS,WorE):
        auxRow=self.pos[0]
        auxColumn=self.pos[1]#This auxiliar gets the values of the possible position transfer
        for i in range(self.camera):
            if(auxRow==-1 or auxRow==20 or auxColumn==-1 or auxColumn==20):
                break
            if(auxRow+NorS!=-1 and auxRow+NorS!=20 and auxColumn+WorE!=-1 and auxColumn+WorE!=20):
                auxRow+=NorS
                auxColumn+=WorE
        near_far=self.nearOrFar(map,auxRow,auxColumn)
        return near_far
    
    def choosePath(self,lst):
        value= utilities.randomNumber()
        for i in range(len(lst)):
            sumProb=round(utilities.partialSum(lst,i+1))
            if(value<=sumProb):
                return i
        return -1

    #     SOUTH=EAST=1
    #     NORTH=WEST=-1
    def move(self,map,cardinalPoint,steps):
        #             N      NE    E     SE    S     SW      W      NW    
        direction=[[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        movDir=direction[cardinalPoint]
        auxSteps=steps
        while(auxSteps>0):
            terrain=map.ground[self.pos[0]][self.pos[1]]
            if(self.canTraverseTerrain(terrain)):
                self.batteryRemaining=self.batteryCost(terrain)
                self.pos=[self.pos[0]+movDir[0],self.pos[1]+movDir[1]]
            else:
                self.blocked=True
                #print("I got stucked at Row: ",self.pos[0], " Column: ",self.pos[1])
                break
            auxSteps-=1
        #self.whereAmI()


    def remainingBattery(self):
        print(self.battery, " Points of battery remaining")

    def minMaxDifficult(self):
        minD=self.camera
        maxD=3*self.camera
        ammount=(maxD-(minD-1))//self.camera
        #print(ammount)
        if(ammount==2):
            return minD+1,maxD-1
        return minD,maxD

    def makeDecision(self,map,sight,nearFarFullList,distanceList):
        EmptyList=True
        #utilities.printList(sight)
        while(EmptyList):
            auxSightList=sight.copy()
            #------------------------------Difficult-----------------------------------
            available=False
            minD,maxD=self.minMaxDifficult()
            difList=self.difficultAvailable(auxSightList,minD,maxD)
            while(available==False):
                difficult=utilities.choosePath(self.difficultProb)
                #print(difficult)
                #if(difList[difficult]==1):
                available=True
                #print("Dificultad escogida: ",difficult)
            auxSightList=utilities.discardDifficult(auxSightList,minD,maxD,difficult)
            #utilities.printList(auxSightList)
            #--------------------------- NearFar -------------------------------------------
            nearFarPos=difficult*2
            nearFarList=[self.nearFarProb[nearFarPos],self.nearFarProb[nearFarPos+1]]
            nearFar=utilities.choosePath(nearFarList)
            nearFarChosen=nearFar+nearFarPos
            #print("Distancia escogida: ",nearFarChosen)
            auxSightList=utilities.discardNearFar(auxSightList,nearFarChosen,nearFarFullList)
            #print("Near Far:", nearFarChosen)
            #utilities.printList(auxSightList)
            #utilities.printList(sight)
            #-------------------------- Cost Distance--------------------------------
            costDistPos=nearFarChosen*2
            costDistList=[self.costDistProb[costDistPos],self.costDistProb[costDistPos+1]]
            costDist=nearFar=utilities.choosePath(costDistList)
            costDistChosen=costDistPos+costDist
            value=utilities.discardDistCost(auxSightList,costDistChosen,distanceList)
            #print("Costo o Distancia escogida: ",costDistChosen)
            #print("Winner pos: ",value)
            #print("--------------------------------------------")
            if(utilities.checkList(auxSightList)):
                EmptyList=False

        return value   

    def difficultAvailable(self,sight,minD,maxD):
        dif=[0,0,0]
        #print("Min:",minD," Max:",maxD)
        for i in range(len(sight)):
            #print(sight[i])
            if(sight[i]<=minD):
                dif[0]=1
            elif(sight[i]>=maxD):
                dif[2]=1
            else:
                dif[1]=1
        #print("Lo que voy a devolver")
        #utilities.printList(dif)
        return dif
    
    def difficultChosen(self):
        minD,maxD= self.minMaxDifficult()
        pass

    def canTraverseTerrain(self,terrain):
        if(int(terrain)<=self.engine):
            return True
        return False

    def batteryCost(self,energyNeeded):
        return self.batteryRemaining-int(energyNeeded)
    
    def goalReached(self,pos):
        if(pos==[0,19]):
            return True
        return False

    def batteryAvailable(self):
        return self.battery>0

    def whereAmI(self):
        print("Row: ",self.pos[0], " Column: ",self.pos[1])
        print("--------------------------------------")
    
    def counterPos(self,pos):
        if(pos<=3):
            return pos+4
        return pos-4

    def detailedPos(self,gen,genMember):
        print("Gen:",gen," Robot #",genMember," Last Position: Row: ",self.pos[0]," Column: ",self.pos[1])