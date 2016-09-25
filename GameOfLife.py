# Ryan Boehm
# GameOfLife.py
# CS:1210:0AAA
# HW 08 - Conway's Game of Life
# Run a simulation of Conway's Game of Life on a 30 by 30 grid using the python turtle module.



import math
import random
import turtle



# Initialize Global Variables
t = None
grid = []
previousGrid = []
numCellsAcross = 30 # dimensions for the grid. Must be an even number to work properly with coordinates.
numGenerations = 10 # number of generations to move through in each game.
generationCount = 0 # tracks the number of generations when playing the game.

    
    
# Draw the horizontal gridlines
def drawVerticals():
    global t, numCellsAcross
    
    t.color('black')
    t.pensize(1)
    leftBottomCoord = -(numCellsAcross // 2)
    x = leftBottomCoord #accumulator for x coordinate
    t.up()
    t.goto(x, leftBottomCoord)
    t.down()
    t.left(90)
    for i in range(numCellsAcross + 1):
        t.forward(numCellsAcross)
        x += 1
        t.up()
        t.goto(x, leftBottomCoord)
        t.down()
   


# Draws the vertical gridlines
def drawHorizontals():
    global t, numCellsAcross
    
    t.color('black')
    t.pensize(1)
    leftBottomCoord = -(numCellsAcross // 2)
    y = leftBottomCoord #accumulator for y coordinate
    t.up()
    t.goto(leftBottomCoord, y)
    t.down()
    for i in range(numCellsAcross + 1):
        t.forward(numCellsAcross)
        y += 1
        t.up()
        t.goto(leftBottomCoord, y)
        t.down()
        
        

# Wrapper function to draw the board
def drawBoard():
    global t, numCellsAcross
    
    drawHorizontals()
    drawVerticals()
    


# draw square with lower left point at (x, y)
def drawSquare(x, y): 
    # subtract 15 to draw correctly in our grid.
    x = x - (numCellsAcross // 2) 
    y = y - (numCellsAcross // 2)
    
    # then let turtle draw
    t.up()
    t.goto(x,y)
    t.down()
    for i in range(4):
        t.forward(1)
        t.right(90)
     


# Intializes the 30x30 grid and returns it.
# All cells in the grid are set to the 0 integer
def initializeGrid():
    global grid, previousGrid, numCellsAcross
    
    #create the grid to represent the game
    cell = [0]
    row = cell * numCellsAcross
    for i in range(numCellsAcross):
        grid.append(row)
    previousGrid = grid[:] #copy into previous grid for first generation of game of life.



# Sets the initial state of the grid by randomly setting 100 cells to be alive.
# Takes a 30 by 30 list as an argument.
# The integer 1 stands for alive, the integer 0 stands for dead.
def seedGrid():
    global grid, numCellsAcross
    
    i = 0
    while i < 100:
        xAlive = random.randint(0, numCellsAcross - 1)
        yAlive = random.randint(0, numCellsAcross - 1)
        if grid[xAlive][yAlive] == 1:
            continue #if you randomly select a cell that is already alive, try again (ensures that we have 100 alive cells).
        else:
            tempList = grid[xAlive][:]
            tempList[yAlive] = 1
            grid[xAlive] = tempList
            i += 1
        


# Takes the current grid, evaluates which cells should live/die, returns the next grid.
def nextGrid(grid):
    
    nextGrid = grid[:] # copy current grid for next round's grid
    for i in range(numCellsAcross): #each row
        for j in range(numCellsAcross): #each column
            neighborCells = [] #store the live/dead status of surrounding squares in a temp list.
            
            # set up the surrounding cells.  
            # cell1 proceeds to cell8 from the top left going clockwise around the square at grid[i][j].
            # the conditions help account for any cells that border an edge (to ensure that we wrap around the grid appropriately).            
            
            # We are on the top row of the grid.
            if i == 0:
                if j == 0:
                    cell1 = grid[numCellsAcross - 1][numCellsAcross - 1]
                    cell2 = grid[numCellsAcross - 1][j]
                    cell3 = grid[numCellsAcross - 1][j + 1] 
                    cell4 = grid[i][j + 1]
                    cell5 = grid[i + 1][j + 1]
                    cell6 = grid[i + 1][j]                    
                    cell7 = grid[i + 1][numCellsAcross - 1]
                    cell8 = grid[i][numCellsAcross - 1]                    
                    
                if j > 0 and j < (numCellsAcross - 1):
                    cell1 = grid[numCellsAcross - 1][j - 1]
                    cell2 = grid[numCellsAcross - 1][j]
                    cell3 = grid[numCellsAcross - 1][j + 1] 
                    cell4 = grid[i][j + 1]
                    cell5 = grid[i + 1][j + 1]
                    cell6 = grid[i + 1][j]
                    cell7 = grid[i + 1][j - 1]
                    cell8 = grid[i][j - 1]                    
                    
                if j == (numCellsAcross - 1):
                    cell1 = grid[numCellsAcross - 1][j - 1]
                    cell2 = grid[numCellsAcross - 1][j]
                    cell3 = grid[numCellsAcross - 1][0]
                    cell4 = grid[i][0]
                    cell5 = grid[i + 1][0] 
                    cell6 = grid[i + 1][j]
                    cell7 = grid[i + 1][j - 1]
                    cell8 = grid[i][j - 1]                    
                    
                    
            # We are in between the top row and the bottom row.  
            if i > 0 and i < (numCellsAcross - 1):
                if j == 0:
                    cell1 = grid[i - 1][numCellsAcross - 1]
                    cell2 = grid[i - 1][j]
                    cell3 = grid[i  - 1][j + 1]
                    cell4 = grid[i][j + 1]
                    cell5 = grid[i + 1][j + 1]
                    cell6 = grid[i + 1][j]                    
                    cell7 = grid[i + 1][numCellsAcross - 1]
                    cell8 = grid[i][numCellsAcross - 1]                     
                                                                  
                if j > 0 and j < (numCellsAcross - 1): #replicates base cases above
                    cell1 = grid[i - 1][j - 1]
                    cell2 = grid[i - 1][j]
                    cell3 = grid[i  - 1][j + 1]
                    cell4 = grid[i][j + 1]
                    cell5 = grid[i + 1][j + 1]
                    cell6 = grid[i + 1][j]
                    cell7 = grid[i + 1][j - 1]
                    cell8 = grid[i][j - 1]                    
                                                   
                if j == (numCellsAcross - 1):
                    cell1 = grid[i - 1][j - 1]
                    cell2 = grid[i - 1][j]                    
                    cell3 = grid[i  - 1][0]
                    cell4 = grid[i][0]
                    cell5 = grid[i + 1][0]
                    cell6 = grid[i + 1][j]
                    cell7 = grid[i + 1][j - 1]
                    cell8 = grid[i][j - 1]                    
                
            
            # We are on the bottom row of the grid.
            if i == (numCellsAcross - 1):
                if j == 0:
                    cell1 = grid[i - 1][numCellsAcross - 1]
                    cell2 = grid[i - 1][j]
                    cell3 = grid[i  - 1][j + 1]
                    cell4 = grid[i][j + 1]                    
                    cell5 = grid[0][j + 1]
                    cell6 = grid[0][j]
                    cell7 = grid[0][numCellsAcross - 1]
                    cell8 = grid[i][numCellsAcross - 1]                     
                                                                                   
                if j > 0 and j < (numCellsAcross - 1):
                    cell1 = grid[i - 1][j - 1]
                    cell2 = grid[i - 1][j]
                    cell3 = grid[i  - 1][j + 1]
                    cell4 = grid[i][j + 1]                    
                    cell5 = grid[0][j + 1]
                    cell6 = grid[0][j]
                    cell7 = grid[0][j - 1]
                    cell8 = grid[i][j - 1]
                                                                                   
                if j == (numCellsAcross - 1):
                    cell1 = grid[i - 1][j - 1]
                    cell2 = grid[i - 1][j]                    
                    cell3 = grid[i  - 1][0]
                    cell4 = grid[i][0]
                    cell5 = grid[0][0]
                    cell6 = grid[0][j]
                    cell7 = grid[0][j - 1]
                    cell8 = grid[i][j - 1]
                    
        
            # build a list of neighboring cells
            neighborCells.append(cell1)
            neighborCells.append(cell2)
            neighborCells.append(cell3)
            neighborCells.append(cell4)
            neighborCells.append(cell5) 
            neighborCells.append(cell6)
            neighborCells.append(cell7)
            neighborCells.append(cell8)
                    
            # check the number of neighboring cells that are alive
            aliveNeighbors = neighborCells.count(1)
            
            # check whether a given cell is alive
            cellStatus = grid[i][j]
            
            # cell is alive this round
            if cellStatus == 1:
                if aliveNeighbors < 2 or aliveNeighbors > 3: # will die if there are too few or too many neighbors alive.
                    tempList = nextGrid[i][:]
                    tempList[j] = 0
                    nextGrid[i] = tempList 
            else: #if cell is dead, must have 3 neighbors to become alive
                if aliveNeighbors == 3:
                    tempList = nextGrid[i][:]
                    tempList[j] = 1
                    nextGrid[i] = tempList 
    
    return nextGrid
                    
                    
                    
# Documents the number of generations played and the total number of generations.
def writeMessage():
    global numCellsAcross, t, numGenerations, generationCount
    
    t.color('black')
    t.up()
    t.goto(0, -((numCellsAcross // 2) + 1.5))
    t.down()
    
    #set up message based on inputs 
    message = 'Number of Generations To Play = ' + str(numGenerations)
    
    t.write(message, False, 'center',('Arial',16,'bold'))
    
    

def generationLoop():
    global grid, previousGrid, numCellsAcross, generationCount, numGenerations
    
    # Loop through the cells, see which ones are alive, draw squares            
    for i in range(numCellsAcross):
        for j in range(numCellsAcross):
            
            # if previous cell was dead, and current cell is alive, draw red square
            if previousGrid[i][j] == 0 and grid[i][j] == 1:
                # Set color and fill-color and begin filling
                t.fillcolor('red')
                t.begin_fill()
                
                drawSquare(i, j)
        
                # stop filling
                t.end_fill() 
                
            # if previous cell was alive, and current cell is dead, draw white square 
            elif previousGrid[i][j] == 1 and grid[i][j] == 0:
                # Set color and fill-color and begin filling
                t.fillcolor('white')
                t.begin_fill()
                
                drawSquare(i, j)
        
                # stop filling
                t.end_fill()
               

    # Force Python to update all graphics
    turtle.update()
    
    # Set up the next grid, save a copy of the previous grid for comparison
    previousGrid = grid[:]
    grid = nextGrid(grid)
    
    # keep going if we still haven't passed the set number of generations.  
    if generationCount < numGenerations:
        generationCount += 1
        generationLoop()
    else: 
        #Otherwise, start the game over.
        generationCount = 0
        playGame() #start over
        
        
        
def playGame():
    global numCellsAcross, t, grid
    
    # remove everything in case we've already played at least once
    t.clear()
    t.up()
    t.home()
    t.down()  
    
    # set up board and representative grid.
    drawBoard()
    initializeGrid()
    seedGrid()
    
    writeMessage() # start documentation
    
    # work through designated number of generations of the game
    generationLoop()



def main():
    global numCellsAcross, t, grid  # So we are assigning values to the global vars
    
    #initialize turtle and draw the picture
    boardSideLength = (numCellsAcross // 2) + 2 #make the dimensions of the board a little bit larger than the grid.
    turtle.setworldcoordinates(-(boardSideLength), -(boardSideLength), boardSideLength, boardSideLength) # LLx, LLy, URx, URy  
    turtle.setup()
    t = turtle.Turtle()
    
    wn = t.getscreen()
    wn.title("Game of Life")
    
    t.speed(0) # fastest = 0
    t.hideturtle() # don't want to see the turtle darting all over the place   
    
    #start game of life
    playGame()
    
    turtle.done()
    
    
    
main()
