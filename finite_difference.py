

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
                self.nodes[x][y] = Node(20, False) #20 degrees Celcius

    def print(self):
        for y in range(self.height-1, -1, -1): #backwards since it prints top to bottom
            for x in range(self.width):
                end = ' '
                if y == 3 and (x == 1 or x == 2):
                    end = '|'
                print(round(self.nodes[x][y].temp, 1), end=end)
            print('\n')

        
def min(a, b):
    if a < b:
        return a
    return b
    

def max(a, b):
    if a > b:
        return a
    return b


def abs(a):
    if a < 0:
        return -a
    return a


timeStep = 1 #seconds
nodeSize = 0.038 #meters
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
            left = max(x - 1, 0) #index of surrounding nodes. If it's an edge, use the current node.j
            right = min(x + 1, sideLength - 1)
            bottom = max(y - 1, 0)
            top = min(y + 1, sideLength - 1)

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

    print('\n')
    print("cycles: ", cycles)
    print("maxTempChange: ", round(maxTempChange, 4))
    grid = nextGrid
    grid.print()
    cycles += 1