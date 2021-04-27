
class Node:
    def __init__(self, temp, isConstant):
        self.temp = temp
        self.isConstant = isConstant
        
def min(a, b):
    if a < b:
        return a
    return b
    
def max(a, b):
    if a > b:
        return a
    return b

timeStep = 1 #seconds
nodeSize = 0.038 #meters
sideLength = 6 #nodes
targetError = 0.01 #Celcius

grid = [[0]*sideLength]*sideLength
for i in range(sideLength):
    grid[i] = [0]*sideLength
    for j in range(sideLength):
        grid[i][j] = Node(20.0, False)

grid[0][2] = Node(75.0, True) #Celcius
grid[2][1] = Node(75.0, True) #Celcius
grid[4][2] = Node(20.0, True) #Celcius
grid[4][5] = Node(20.0, True) #Celcius

for t in range(100):
    for j in range(sideLength-1, -1, -1):
        row = ""
        for i in range(sideLength):
            left = max(i - 1, 0) #index of surrounding nodes. If it's an edge, use the current node.j
            right = min(i + 1, sideLength - 1)
            bottom = max(j - 1, 0)
            top = min(j + 1, sideLength - 1)

            leftNode = grid[left][j].temp
            rightNode = grid[right][j].temp
            bottomNode = grid[i][bottom].temp
            topNode = grid[i][top].temp
        
            average = (leftNode + rightNode + bottomNode + topNode) / 4
            if not grid[i][j].isConstant:
                grid[i][j].temp = average

            print(int(grid[i][j].temp), end=' ')
        print('\n')
    print('\n')