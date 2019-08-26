# File: hw5_part4.py
# Author: Dane Magbuhos
# Date: 10/8/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program determines the user`s number input
#              using the function properties of the number.


EVEN_CHECKER = 2 # Used to figure out if number is even
BOUNDARY = 0 # Used to determine where number lies on the number line
DIVISIBLE = 0 # Determines if first number is divisible by second number

#########################################################
# checkOddOrEven() prints if given number is odd or even
# Input: userNum; an integer chosen by the user
# Output: None
def checkOddOrEven(userNum):  
    
    # If expression equals to DIVISIBLE, outputs number is even
    # and vice versa
    if userNum % EVEN_CHECKER == DIVISIBLE:
        print(userNum," is even")
    elif userNum % EVEN_CHECKER != DIVISIBLE:
        print(userNum," is odd")

################################################
#checkPositive() prints if given number
#                is positive, negative, or zero
# Input: userNum; an integer chosen by the user
# Output: None
def checkPositive(userNum):
    
    # Checks to see where number lies in which boundary and
    # outputs appropriate response
    if userNum < BOUNDARY:
        print(userNum," is negative")
    elif userNum == BOUNDARY:
        print(userNum," is zero")
    elif userNum > BOUNDARY:
        print(userNum," is positive")

######################################################
#checkDivisible() prints if given number is divisible
#                 by a second number
# Input: userNum; an integer chosen by user
# Output: None 
def checkDivisible(userNum):
    # Grabs secondInt input from user
    secondInt = int(input("Enter number to divide by: "))

    # If expression equals to DIVISIBLE, outputs 
    # "is divisible by" response and vice versa
    if userNum % secondInt == DIVISIBLE:
       print(userNum, "is divisible by ",secondInt, end="\n\n")
    elif userNum % secondInt != DIVISIBLE:
         print(userNum, "is not divisible by",secondInt, end="\n\n")

def main():

    # Grabs integer from user
    numberInput = int(input("Enter a number you would like to check: "))

    #Calls functions and passes user input for examination 
    checkOddOrEven(numberInput)
    checkPositive(numberInput)
    checkDivisible(numberInput)

main()
