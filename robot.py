import utilities

class Robot:

    def __init__(self,battery,camera,engine):
        self.battery=battery*110
        self.camera=camera
        self.engine=engine
        self.pos=[19,0]

    def printRobot(self,pos):
        if(pos==0):
            print("Generation: ",pos+1)
        else:
            print("Robot #",pos+1," Battery: ", self.battery,
            " Camera: ", self.camera, " Engine: ", self.engine)
    
    def cameraSight(self,map):
            NORTH=WEST=-1 #Direction into the map
            SOUTH=EAST=1
            sight=[self.northSouthView(map,NORTH),self.collateralCardPointView(map,NORTH,EAST),
                self.eastWestView(map,EAST),self.collateralCardPointView(map,SOUTH,EAST),
                self.northSouthView(map,SOUTH),self.collateralCardPointView(map,SOUTH,WEST),
                self.eastWestView(map,WEST),self.collateralCardPointView(map,NORTH,WEST)]
            avrg=utilities.average(sight)
            return sight

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
    
    def choosePath(self,lst):
        value= utilities.randomNumber()
        print (value)
        for i in range(len(lst)):
            sumProb=utilities.partialSum(lst,i+1)
            print("Partial sum: ",sumProb)
            if(value<=sumProb):
                return i
        return -1