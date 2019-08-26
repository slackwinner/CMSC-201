# File: proj3.py
# Author: Dane Magbuhos
# Date: 11/27/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program reads in specified maze chosen by the user
#              and attempts to find the solution path to a specifc 
#              coordinate point.

# Specifies the four walls and open/closed walls for a square
RIGHT = 0
BOTTOM = 1
LEFT = 2
TOP = 3
OPEN_W = "0"
CLOSED_W = "1"

# Used to modify indexes, counters, and boundary ranges
DECREMENT = 1
INCREMENT = 1
INDEX_INCREMENT = 2
INDEX_DECREMENT = 2
FIRST_INDEX = 0
BAD_PATH_ONE = "B"
BAD_PATH_TWO = "P"

# Items used when validating input
TYPE_ONE = "row"
TYPE_TWO = "column"
LOWER_BOUND = 0

# Used to denote maze package's indexes
ROW = 0
COLUMN = 1
TARGET_ROW = 2
TARGET_COLUMN = 3
MAZE_MAP = 4  

# Used to denote x and y coordinate indexes
X_COOR = 0
Y_COOR = 1

# Used to denote placement of coordinate points and squares 
COORDINATE_PLACEMENT = 2
SQUARE_PLACEMENT = 2

#############################################################################
# printSolution(): Prints out solution to maze
# Input:           solution, 1D list that contains coordinate point integers 
# Output:          None, Only serves as a print function 

def printSolution(solution):

   index = LOWER_BOUND
   row = X_COOR
   col = Y_COOR
   simplifiedList = []

   if solution == None:
      print("No Solution Found! \n\n")

   else:
      print("Solution Found")

      # Filters out the bad paths and only adds the correct path to 1D list
      while index < len(solution)/COORDINATE_PLACEMENT:

         # Clears out list if bad path markers are found in list
         if solution[row] == BAD_PATH_ONE and solution[col] == BAD_PATH_TWO:
            simplifiedList = []

         else:
            simplifiedList.append(solution[row])
            simplifiedList.append(solution[col])

         index += INCREMENT
         row += INDEX_INCREMENT
         col += INDEX_INCREMENT
      
      # Resets index, row ,and col for next iteration   
      index = LOWER_BOUND
      row = X_COOR
      col = Y_COOR

      # Outputs only the correct path
      while index < len(simplifiedList)/COORDINATE_PLACEMENT:
         print("(" + str(simplifiedList[row]) + ", " + str(simplifiedList[col]) + ")")
         index += INCREMENT
         row += INDEX_INCREMENT
         col += INDEX_INCREMENT
      

#######################################################################################
# pathListChecker(): Verifies if a square has been or has not been visited before
#                    by comparing the previous squares with the examined square
# Input:             currentRow; an integer that represents examined row
#                    currentCol; an integer that represents examined col
#                    pathList; a 1D list that contains coordinate points of previous 
#                    squares
# Output:            result; a boolean value that represents if a square has been or
#                    has not been in a particular square

def pathListChecker(currentRow, currentCol, pathList):

   result = False
   pairCounter = LOWER_BOUND
   lengthOfPair = len(pathList)/COORDINATE_PLACEMENT
   row = X_COOR
   col = Y_COOR
   
   # Handles the case where only two populated coordinate points are present 
   if len(pathList) == COORDINATE_PLACEMENT:
      if currentRow == pathList[row] and currentCol == pathList[col]:
         result = True
   
   # Handles the case where there's more than two populated coordinate points are present
   elif len(pathList) > COORDINATE_PLACEMENT:
      while pairCounter < lengthOfPair:
         if currentRow == pathList[row] and currentCol == pathList[col]:
            result = True
        
         pairCounter += INCREMENT
         row += INDEX_INCREMENT
         col += INDEX_INCREMENT
   
   return result

#####################################################################################################################
# getAlternativePath(): Grabs the next preceding square should getting the first nearest square attempt fail 
# Input:                direction; an integer that represents the position of a square
#                       square; a 2D list coordinate that contains each square's wall position
#                       row; an integer that conveys row dimension of maze
#                       col; an integer that conveys column dimension of maze
#                       startingRow; an integer that conveys user's picked row
#                       startingCol; an integer that conveys user's picked column
#                       tempRow; an integer that serves as a reset row value of the current row being examined
#                       tempCol; an integer that serves as a reset column value of the current column being examined 
#                       pathList; a 1D list that contains coordinate point integers of previous squares
# Output:               pathList; a 1D list that contains recently added coordinate point integers of examined square 

def getAlternativePath(direction, square, row, col, startingRow, startingCol, tempRow, tempCol, pathList):
   
   result = True
   examinedRow = tempRow
   examinedCol = tempCol

   while result != False:

      # Grabs coordinates for right square
      if direction == RIGHT  and square[RIGHT] == OPEN_W:
         examinedCol += INCREMENT
         checkRow = tempRow
         checkCol = examinedCol

      # Grabs coordinates from bottom square
      elif direction == BOTTOM and square[BOTTOM] == OPEN_W:
         examinedRow += INCREMENT
         checkRow = examinedRow
         checkCol = tempCol

      # Grabs coordinates from left square
      elif direction == LEFT and square[LEFT] == OPEN_W:
         examinedCol -= DECREMENT
         checkRow = tempRow
         checkCol = examinedCol
   
      # Grabs coordiantes from top square
      elif direction == TOP and square[TOP] == OPEN_W:
         examinedRow -= DECREMENT
         checkRow = examinedRow
         checkCol = tempCol

      # Resets the search if one of the coordinate points is out of bounds
      if examinedRow < LOWER_BOUND or examinedRow > row or examinedCol < LOWER_BOUND or examinedCol > col:
         examinedRow = startingRow
         examinedCol = startingCol

         # Bad path markers are placed to indicate what paths to skip when printing out a solution
         pathList.append(BAD_PATH_ONE)
         pathList.append(BAD_PATH_TWO)

      # Determines if collected coordiantes are open and have not been at that specific location
      if square[direction] == OPEN_W:
         result = pathListChecker(checkRow, checkCol, pathList)
      else:
         # Resets coordinate points to previous coordinate points and grabs next direction
          examinedRow = tempRow
          examinedCol = tempCol
          direction += INCREMENT

          # Keeps direction options from being out of bounds
          if direction > TOP: 
             direction = RIGHT
   
   # Adds coordinate points to the pathList
   tempRow = examinedRow
   tempCol = examinedCol
   pathList.append(tempRow)
   pathList.append(tempCol)
      
   return pathList
      
###########################################################################################################################
# searchMaze(): Recursively searches through maze to determine the solution path from starting point to ending point
# Input:        maze; a 2D list that contains a 1D list of square's wall attributes
#               row; an integer that conveys max row's dimensions of maze
#               col; an integer that conveys max column's dimensions of maze
#               targetRow; an integer that conveys row's ending point
#               targetCol; an integer that conveys column's ending point
#               startingRow; an integer that conveys user's picked row
#               startingCol; an integer that conveys user's picked column
#               currentRow; an integer that conveys an examined row value
#               currentCol; an integer that conveys an examined column value
#               pathList; a 1D list that contains all current coordinate points of solution
# Output:       pathList; a 1D list that contains all coordinate points of solutions              

def searchMaze(maze, row, col, targetRow, targetCol, startingRow, startingCol, currentRow, currentCol, pathList):

   # Sets coordinates from maze's 2D list
   square = maze[currentRow][currentCol]

   # Temp variables used to test certain directions before alterating currentRow and currentCol
   tempRow = currentRow
   tempCol = currentCol
   
   # Returns path list if the coordinate points is at the final coordaintes
   if currentRow == targetRow and currentCol == targetCol:
        return pathList

   # Returns nothing if coordinate points is a dead end
   elif square[RIGHT] == CLOSED_W and square[BOTTOM] == CLOSED_W and square[LEFT] == CLOSED_W and square[TOP] == CLOSED_W:
      return None

   else:
       
       # Examines the open right hand side of square
       if square[RIGHT] == OPEN_W:
          # Sets direction to next square position if alternative path is needed
          direction = BOTTOM
          tempCol += INCREMENT
          result = pathListChecker(currentRow, tempCol, pathList)

       # Examines the open bottom side of square
       elif square[BOTTOM] == OPEN_W:
          direction = LEFT
          tempRow += INCREMENT
          result = pathListChecker(tempRow, currentCol, pathList)

       # Examines the open left side of square
       elif square[LEFT] == OPEN_W:
          direction = TOP
          tempCol -= DECREMENT
          result = pathListChecker(currentRow, tempCol, pathList)
   
       # Examines the open top side of square
       elif square[TOP] == OPEN_W:
          direction = RIGHT
          tempRow -= DECREMENT
          result = pathListChecker(tempRow, currentCol, pathList)
       
       # Conveys that examined coordinate points has not been visited and adds the coordinate points to new path list
       if result == False:
          currentRow = tempRow
          currentCol = tempCol
          pathList.append(currentRow)
          pathList.append(currentCol)
          newPathList = pathList[:]
   
       # Conveys that examned coordiante point has been visited before and adds alternative coordiante points to path list
       elif result == True:
          tempRow = currentRow
          tempCol = currentCol
          # Gets alternative path
          altPath = getAlternativePath(direction, square, row, col, startingRow, startingCol, tempRow, tempCol, pathList)
          
          # Grabs recently added coordinate points from list
          currentRow = altPath[len(altPath) - INDEX_DECREMENT]
          currentCol = altPath[len(altPath) - DECREMENT]
          newPathList = altPath[:]

       return searchMaze(maze, row, col, targetRow, targetCol, startingRow, startingCol, currentRow, currentCol, newPathList)


##################################################################################
# inputValidator(): Ensures that row and column inputs are within range of maze
# Input:            higherBound; an integer that represents max boundary of maze
#                   validType; a string that indicates an appropriate output to
#                   give to the user
# Output:           userInput; an integer that represents user's desired choice 
       
def inputValidator(higherBound, validType):

 result = False

 if validType == TYPE_ONE:
     userInput = int(input("Please enter the starting row: "))

 elif validType == TYPE_TWO:
     userInput = int(input("Please enter the starting column: "))
 
 while result != True:
     if userInput < LOWER_BOUND or userInput > higherBound:
         userInput = int(input("Invalid, enter a number between " + str(LOWER_BOUND) + " and " + str(higherBound) + " (inclusive): "))
     else:
         result = True

 return userInput


##############################################################################
# readMaze(): Takes in file name, reads in it's contents, and constructs maze
# Input:      fileName; a string that contains text file's name
# Output:     mazeContents; a 1D list of the read in items from text file

def readMaze(fileName):

 # Opens up chosen maze map
 mazeFile = open(fileName)

 # Reads in the contents of maze map
 contents = mazeFile.readlines()

 # Closes the maze map file
 mazeFile.close()

 # Gets rid of extra spaces in read input
 coordinateList = []
 index = FIRST_INDEX

 while index < COORDINATE_PLACEMENT:
     coordinates = contents[index].strip().split()
     coordinateList.append(coordinates)
     index += INCREMENT
 
 # Intializes the dimensions of maze and finish line coordinates
 maxRow = int(coordinateList[X_COOR][X_COOR])
 maxCol = int(coordinateList[X_COOR][Y_COOR]) 

 finalRow = int(coordinateList[Y_COOR][X_COOR])
 finalCol = int(coordinateList[Y_COOR][Y_COOR])
 
 squareList = []
 index = SQUARE_PLACEMENT

 # Stores the squares inside a separate 1D list
 while index < (len(contents)):
     square = contents[index].strip().split()
     squareList.append(square)
     index += INCREMENT

 # Creates and populates 2D maze with squares from 1D list
 maze = []
 tempIndex = FIRST_INDEX

 while len(maze) < maxRow:
     row = []
     while len(row) < maxCol:
         row.append(squareList[tempIndex])
         tempIndex += INCREMENT
     maze.append(row)

 # Stores coordinate points and maze into 1D list
 mazeContents = []
 mazeContents.append(maxRow)
 mazeContents.append(maxCol)
 mazeContents.append(finalRow)
 mazeContents.append(finalCol)
 mazeContents.append(maze)
   
 return mazeContents
  
def main():

 print("Welcome to the Maze Solver!")
 fileName = input("Please enter the filename of the maze: ")

 # Calls readMaze function
 mazePackage = readMaze(fileName)

 # Grabs contents from mazePackage 
 row = mazePackage[ROW] - DECREMENT
 column = mazePackage[COLUMN] - DECREMENT
 targetRow = mazePackage[TARGET_ROW]
 targetCol = mazePackage[TARGET_COLUMN]
 maze = mazePackage[MAZE_MAP]

 # Calls inputValidator function
 startingRow = inputValidator(row, TYPE_ONE)
 startingCol = inputValidator(column, TYPE_TWO)

 # These variables are used to keep track of current coordinate movement
 currentRow = startingRow 
 currentCol = startingCol 
 pathList = []

 pathList.append(currentRow)
 pathList.append(currentCol)

 # Calls searchMaze function
 solution = searchMaze(maze, row, column, targetRow, targetCol,startingRow, startingCol, currentRow, currentCol, pathList)
 
 # Calls printSolution function
 printSolution(solution)

main()
