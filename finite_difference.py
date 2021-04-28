

class Node:
    def __init__(self, temp, isConstant):
        self.temp = temp
        self.isConstant = isConstant


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = [[0]*height]*width
        for x in range(width):
            self.nodes[x] = [0]*height
            for y in range(height):
                self.nodes[x][y] = Node(22.0 , False) #20 degrees Celcius


    def print(self):
        for y in range(self.height-1, -1, -1): #backwards since it prints top to bottom
            for x in range(self.width):
                end = ' '
                if y == 3 and (x == 1 or x == 2):
                    end = '|'
                print(round(self.nodes[x][y].temp, 1), end=end)
            print('\n')


diffusivity = .000115
fourier = 0.201
nodeSize = 0.038 #meters
timeStep = fourier * nodeSize**2 / diffusivity #seconds
sideLength = 6 #nodes
targetError = 0.01 #Celcius

grid = Grid(sideLength, sideLength)

grid.nodes[0][2] = Node(75.0, True) #Celcius
grid.nodes[2][1] = Node(75.0, True) #Celcius
grid.nodes[4][2] = Node(20.0, True) #Celcius
grid.nodes[4][5] = Node(20.0, True) #Celcius

maxTempChange = 100
cycles = 1
while maxTempChange > targetError:
    maxTempChange = 0
    nextGrid = Grid(sideLength, sideLength)
    for y in range(sideLength-1, -1, -1):
        for x in range(sideLength):
            left = x - 1
            right = x + 1
            bottom = y - 1
            top = y + 1
            if x == 0:
                left = right
            elif x == sideLength - 1:
                right = left
            if y == 0:
                bottom = top
            elif y == sideLength - 1:
                top = bottom

            leftNode = grid.nodes[left][y].temp
            rightNode = grid.nodes[right][y].temp
            bottomNode = grid.nodes[x][bottom].temp
            topNode = grid.nodes[x][top].temp
        
            average = (leftNode + rightNode + bottomNode + topNode) / 4
            if grid.nodes[x][y].isConstant:
                nextGrid.nodes[x][y].temp = grid.nodes[x][y].temp
            else:
                nextGrid.nodes[x][y].temp = average
                maxTempChange = max(abs(nextGrid.nodes[x][y].temp - grid.nodes[x][y].temp), maxTempChange)
            nextGrid.nodes[x][y].isConstant = grid.nodes[x][y].isConstant
            if x == 0 and y == sideLength - 1:
                print(average)

    #print('\n')
    #print("cycles:", cycles)
    #print("time step:", round(timeStep, 3), "seconds")
    #print("time:", round(cycles * timeStep), "seconds")
    #print("maxTempChange:", round(maxTempChange, 4), "degrees Celcius")
    #print()
    grid = nextGrid
    #grid.print()
    cycles += 1