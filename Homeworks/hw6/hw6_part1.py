# File: hw6_part1.py
# Author: Dane Magbuhos
# Date: 11/14/17
# E-mail: mag4@umbc.edu
# Description: The program calculates the summation of a number
#              that stops at the second number that the user
#              provides using recursion.

# Used to indicate the next number after secondNum
NEXT_VALUE = 1

# Used to indicate the last number of the summation process
LAST_VALUE = 0 

####################################################################
# summation() Calculates the sum recursively from the starting number 
#             to the ending number
# Input:      firstNum; an integer that represents starting number
#             secondNum; an integer that represents the ending number
# Output:     total; an integer that conveys the total amount added 
#             within the range of the starting and ending values

def summation(firstNum, secondNum):

    # Stops the summation process if firstNum is equal to the number after secondNum
    if firstNum == secondNum - NEXT_VALUE:
        return LAST_VALUE

    else:
        # Calls the summation function recursively
        total = firstNum + summation(firstNum - NEXT_VALUE, secondNum)
        return total

def main():

    firstNum = int(input("Please input the number you want to sum from: "))
    secondNum = int(input("Please input the number you want to sum down to: "))

    # Sends the user inputs to summation function
    total = summation(firstNum, secondNum)

    # Outputs the summation amount
    print("The summation from", firstNum , " to ", secondNum, " is ", total,"\n\n")







main()
