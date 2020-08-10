import unittest
import ground
import utilities
import genetic
from ground import Ground
from scenario import Scenario
from robot import Robot

class TestingMethods(unittest.TestCase):
    
    def setUp(self):
        self.floor=Ground("ground.txt")
        self.robots=utilities.createRobots()
        self.dummyRobotBoy=Robot(1,1,1,[],[],[],-1,-1)
        self.dummyRobotGirl=Robot(3,2,3,[],[],[],-1,-1)
        self.scenario=Scenario("ground.txt")
        #self.floor.printFloor()

    #def test_space(self):
    #    self.floor.printSpaceBySpace()
        
    # def test_matrixSize(self):
    #     print("Rows:" ,len(self.floor.ground), " Columns: ",len(self.floor.ground[0]))

    # def test_printMatrix(self):
    #     self.floor.printFloor()

    # def test_createRobots(self):
    #     utilities.printRobots(self.robots)

    # def test_north(self):
    #     self.dummyRobot.pos[0]=1
    #     NORTH=-1
    #     acum,auxRow=self.dummyRobot.northSouthView(self.floor,NORTH)
    #     print("Camera:",self.dummyRobot.camera, " Acum: ",acum, " X: ",auxRow, " Y: ",self.dummyRobot.pos[1])

    # def test_south(self):
    #     SOUTH=1
    #     self.dummyRobot.pos[0]=18
    #     acum,auxRow=self.dummyRobot.northSouthView(self.floor,SOUTH)
    #     print("Camera:",self.dummyRobot.camera, " Acum: ",acum, " X: ",auxRow, " Y: ",self.dummyRobot.pos[1])
    
    # def test_east(self):
    #     EAST=1
    #     self.dummyRobot.pos[1]=18
    #     acum,auxColumn=self.dummyRobot.eastWestView(self.floor,EAST)
    #     print("Camera:",self.dummyRobot.camera, " Acum: ",acum, " X: ",self.dummyRobot.pos[0], " Y: ",auxColumn)
    
    # def test_west(self):
    #     WEST=-1
    #     self.dummyRobot.pos[1]=1
    #     acum,auxColumn=self.dummyRobot.eastWestView(self.floor,WEST)
    #     print("Camera:",self.dummyRobot.camera, " Acum: ",acum, " X: ",self.dummyRobot.pos[0], " Y: ",auxColumn)

    # def test_nortwest(self):
    #     NORTH=WEST=-1
    #     self.dummyRobot.pos[1]=1
    #     self.dummyRobot.pos[1]=1
    #     acum,auxRow,auxColumn=self.dummyRobot.CollateralCardPointView(self.floor,NORTH,WEST)
    #     print("Camera:",self.dummyRobot.camera, " Acum: ",acum, " X: ",auxRow, " Y: ",auxColumn)
    
    # def test_northeast(self):
    #     NORTH=-1
    #     EAST=1
    #     acum,auxRow,auxColumn=self.dummyRobot.CollateralCardPointView(self.floor,NORTH,EAST)
    #     print("Camera:",self.dummyRobot.camera, " Acum: ",acum, " X: ",auxRow, " Y: ",auxColumn)
    
    # def test_southwest(self):
    #     SOUTH=1
    #     WEST=-1
    #     self.dummyRobot.pos[1]=19
    #     acum,auxRow,auxColumn=self.dummyRobot.CollateralCardPointView(self.floor,SOUTH,WEST)
    #     print("Camera:",self.dummyRobot.camera, " Acum: ",acum, " X: ",auxRow, " Y: ",auxColumn)

    # def test_southeast(self):
    #     SOUTH=EAST=1
    #     self.dummyRobot.pos[0]=0
    #     acum,auxRow,auxColumn=self.dummyRobot.CollateralCardPointView(self.floor,SOUTH,EAST)
    #     print("Camera:",self.dummyRobot.camera, " Acum: ",acum, " X: ",auxRow, " Y: ",auxColumn)

    # def test_collateralLimit(self):
    #     SOUTH=EAST=1
    #     self.dummyRobot.pos=[18,18]
    #     acum,auxRow,auxColumn=self.dummyRobot.CollateralCardPointView(self.floor,SOUTH,EAST)
    #     print("Camera:",self.dummyRobot.camera, " Acum: ",acum, " X: ",auxRow, " Y: ",auxColumn)
    
    # def test_sight(self):
    #     #[8,9]
    #     self.dummyRobot.pos=[8,9]
    #     self.dummyRobot.sightAmmount(self.floor)

    # def test_sightData(self):
    #     self.dummyRobot.pos=[8,9]
    #     total=utilities.totalPoints(self.dummyRobot.cameraSight(self.floor))
    #     avrg=utilities.average(self.dummyRobot.cameraSight(self.floor))
    #     utilities.printList(self.dummyRobot.cameraSight(self.floor))
    #     print("Total: ",total," Average: ",avrg)

    # def test_normProb(self):
    #     self.dummyRobot.pos=[8,9]
    #     realProbLst=utilities.realProb(self.dummyRobot.cameraSight(self.floor))
    #     utilities.printList(realProbLst)
    #     print("Summed probabilities: ",round(sum(realProbLst),2))

    # def test_newProb(self):
    #     self.dummyRobot.pos=[8,9]
    #     realProbLst=utilities.realProb(self.dummyRobot.cameraSight(self.floor))
    #     newProbLst=utilities.newProb(self.dummyRobot.cameraSight(self.floor),realProbLst)
    #     utilities.printList(newProbLst)
    #     print("Summed probabilities: ",round(sum(newProbLst),2))

    # def test_normProb(self):
    #     self.dummyRobot.pos=[8,9]
    #     realProbLst=utilities.realProb(self.dummyRobot.cameraSight(self.floor))
    #     newProbLst=utilities.newProb(self.dummyRobot.cameraSight(self.floor),realProbLst)
    #     normProbList=utilities.normalizeProb(newProbLst)
    #     utilities.printList(normProbList)
    #     print("Summed probabilities: ",round(sum(normProbList),2))

    # def test_random(self):
    #     print (utilities.randomNumber())


    # def test_choosePath(self):
    #     #self.dummyRobot.pos=[8,9]
    #     realProbLst=utilities.realProb(self.dummyRobot.cameraSight(self.floor))
    #     newProbLst=utilities.newProb(self.dummyRobot.cameraSight(self.floor),realProbLst)
    #     normProbList=utilities.normalizeProb(newProbLst)
    #     utilities.printList(normProbList)
    #     path=self.dummyRobot.choosePath(normProbList) #Gets the cardinal point to move
    #     utilities.pathChoosen(path)

    # def test_movement(self):
    #     self.dummyRobot.pos=[8,6]
    #     realProbLst=utilities.realProb(self.dummyRobot.cameraSight(self.floor))
    #     newProbLst=utilities.newProb(self.dummyRobot.cameraSight(self.floor),realProbLst)
    #     normProbList=utilities.normalizeProb(newProbLst)
    #     utilities.printList(normProbList)
    #     path=self.dummyRobot.choosePath(normProbList) #Gets the cardinal point to move
    #     utilities.pathChoosen(path)
    #     self.dummyRobot.move(self.floor,path)
    #     print("My actual position is Row: ",self.dummyRobot.pos[0], 
    #     " Column: ",self.dummyRobot.pos[1])
    
    # def test_roboticTravel(self):
    #     print("En el travel")
    #     utilities.roboticTravel(self.robots,self.floor)

    # def test_minMaxDifficult(self):
    #     easy1,easy2=self.dummyRobot.minMaxDifficult(1)
    #     medium1,medium2=self.dummyRobot.minMaxDifficult(2)
    #     hard1,hard2=self.dummyRobot.minMaxDifficult(3)

    #     print("Easy min: ",easy1," Easy max: ",easy2)
    #     print("Medium min: ",medium1," Medium max: ",medium2)
    #     print("Hard min: ",hard1," Hard max: ",hard2)

    # def test_sight(self):
    #     sight,distance= self.dummyRobot.cameraSight(self.floor)
    #     utilities.printList(sight)
    
    # def test_probs(self):
    #     #self.dummyRobot.pos=[15,17]
    #     utilities.randomDifficult(3,self.dummyRobot.difficultProb)
    #     utilities.randomDifficult(6,self.dummyRobot.nearFarProb)
    #     utilities.randomDifficult(12,self.dummyRobot.costDistProb)
    #     # utilities.printList(self.dummyRobot.difficultProb)
    #     # utilities.printList(self.dummyRobot.nearFarProb)
    #     # utilities.printList(self.dummyRobot.costDistProb)
    #     sight,distance,nearFarList= self.dummyRobot.cameraSight(self.floor)
    #     self.dummyRobot.makeDecision(self.floor,sight,nearFarList,distance)
    
    # def test_difficultAvailable(self):
    #     self.dummyRobot.pos=[15,17]
    #     sight,distance= self.dummyRobot.cameraSight(self.floor)
    #     diff=self.dummyRobot.difficultAvailable(sight)
    #     utilities.printList(diff)

    # def test_traverseTerrain(self):
    #     #self.dummyRobot.pos=[19,1]
    #     utilities.randomDifficult(3,self.dummyRobot.difficultProb)
    #     utilities.randomDifficult(6,self.dummyRobot.nearFarProb)
    #     utilities.randomDifficult(12,self.dummyRobot.costDistProb)
    #     self.dummyRobot.traverseTerrain(self.floor)

    # def test_crossingProb(self):
    #     genetic.crossingProb(255,0)        

    

    # def test_crossRobot(self):
    #     utilities.randomDifficult(3,self.dummyRobotBoy.difficultProb)
    #     utilities.randomDifficult(6,self.dummyRobotBoy.nearFarProb)
    #     utilities.randomDifficult(12,self.dummyRobotBoy.costDistProb)
    #     utilities.randomDifficult(3,self.dummyRobotGirl.difficultProb)
    #     utilities.randomDifficult(6,self.dummyRobotGirl.nearFarProb)
    #     utilities.randomDifficult(12,self.dummyRobotGirl.costDistProb)
    #     distancePoints=utilities.distancePoint(self.robots)
    #     distancePoints=utilities.realProb(distancePoints)
    #     distancePoints=utilities.newProb(distancePoints)
    #     distancePoints=utilities.normalizeProb(distancePoints)

    #     utilities.createProbabilities(self.robots)
    #     genetic.crossGen(distancePoints,self.robots)
    #     #genetic.crossRobots(self.dummyRobotBoy,self.dummyRobotGirl)
    
    def test_roboticTravel(self):
        f= open("generations.txt","w+")
        utilities.assignProbabilities(self.robots)
        x=10
        for i in range(x):
            utilities.roboticTravel(self.robots,self.floor)
            #utilities.printDetailedPositions(self.robots)
            distancePoints=utilities.distancePoint(self.robots)
            #utilities.printRobots(self.robots)
            utilities.writeInFile(self.robots,f)
            if(i==x-1):
                utilities.printRobots(self.robots)
            self.robots=genetic.crossGen(distancePoints,self.robots)
            genetic.mutation(self.robots)
        f.close()
        #utilities.printRobots(self.robots)
        # newGen2=genetic.crossGen(distancePoints,newGen)
        # utilities.roboticTravel(newGen2,self.floor)
        # utilities.printRobots(newGen2)
        # utilities.printDetailedPositions(newGen2)
        # distancePoints=utilities.distancePoint(newGen2)
        #distancePoints=utilities.distancePoint(self.robots)
        #distancePoints=utilities.realProb(distancePoints)
        #distancePoints=utilities.newProb(distancePoints)
        #distancePoints=utilities.normalizeProb(distancePoints)
        #utilities.printList(distancePoints)
        #print(sum(distancePoints))


    # def test_generations(self):
    #     #Ya hay mapa
    #     #Ya esta la primera gen
    #     utilities.printRobots(self.robots)
    #     utilities.createProbabilities(self.robots)
    #     # #for i in range(2):
    #     utilities.roboticTravel(self.robots,self.floor)
    #     distancePoints=utilities.distancePoint(self.robots)
    #     newGen=genetic.crossGen(distancePoints,self.robots)
    #     # self.robots.clear()
    #     # self.robots=newGen
    #     # utilities.roboticTravel(self.robots,self.floor)


if __name__ == '__main__':
    unittest.main()