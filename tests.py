import unittest
import ground
import utilities
from ground import Ground
from scenario import Scenario
from robot import Robot

class TestingMethods(unittest.TestCase):
    
    def setUp(self):
        self.floor=Ground("ground.txt")
        self.robots=utilities.createRobots()
        self.dummyRobot=Robot(3,3,3)
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


    def test_choosePath(self):
        #self.dummyRobot.pos=[8,9]
        realProbLst=utilities.realProb(self.dummyRobot.cameraSight(self.floor))
        newProbLst=utilities.newProb(self.dummyRobot.cameraSight(self.floor),realProbLst)
        normProbList=utilities.normalizeProb(newProbLst)
        utilities.printList(normProbList)
        path=self.dummyRobot.choosePath(normProbList)
        utilities.pathChoosen(path)


if __name__ == '__main__':
    unittest.main()