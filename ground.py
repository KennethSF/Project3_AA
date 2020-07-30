

class Ground:

    def __init__(self,file_name):
        self.ground=self.read(file_name)

    def read(self,file_name):
        size=20
        f=open(file_name,"r")
        M=self.createMatrix(size)
        for i in range(size):
            self.createLine(M,f.readline(),i)
        return M

    def createMatrix(self,size):
        M=[]
        for i in range (0,size):
            M.append([None]*size)
        return M
    
    def createLine(self,M,ground_values,row):
        for i in range (len(M)):
            M[row][i]=ground_values[i]

    def printFloor(self):
        for i in range(len(self.ground)):
            s=""
            for j in range(len(self.ground[0])):
                s+=self.ground[i][j]+" "
            print(s)
    
    def printSpaceBySpace(self):
        for i in range(len(self.ground)):
            for j in range(len(self.ground[0])):
                print("El valor es:",self.ground[i][j]," X=",i, "Y=",j)
    
    def printSpace(self,x,y):
        print("Value of this space: ",self.ground[x][y])