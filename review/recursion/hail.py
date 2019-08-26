# File: hail.py
# Author: Dane Magbuhos
# Section: 20
# Email: mag4@umbc.edu
# Description: This program simulates the up and down movement 
#              of a hailstone in a storm

EVEN = 2
EVEN_REMAINDER = 0
ODD_REMAINDER = 1

def movement(startingHeight):

   # print("Hail is currently at: ", startingHeight)

    if startingHeight <= 0:
        print("Invalid Height of ", startingHeight)
        return 0

    elif startingHeight == 1:
        print("Height of ", startingHeight) 
        return 0

    else:
       # intCast = int(startingHeight)
        print("Current Step: ", startingHeight)

        modHeight = startingHeight % EVEN
    
        if modHeight == EVEN_REMAINDER:
            startingHeight = startingHeight // 2
            return movement(startingHeight) + 1
    
        elif modHeight == ODD_REMAINDER:
            startingHeight = startingHeight * 3 + 1
            return movement(startingHeight) + 1


def main():

     startingHeight = int(input("Please enter the starting height of the hailstone: "))

     finalHail = movement(startingHeight)

     print("It took ", finalHail, "steps to hit the ground.")




main()
