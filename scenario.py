from ground import Ground
from robot import Robot
import utilities

class Scenario:

    def __init__(self,file_name):
        self.map= Ground("ground.txt")
        self.robots= utilities.createRobots()
        #utilities.printRobots(robots)


    def moveRobots(self):
        pass

    

    