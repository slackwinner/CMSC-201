# File: hw3_part2.py
# Author: Dane Magbuhos
# Date: 09/24/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program calculates an expotential expression
#              without using exponentiation.

def main():

    firstInt = int(input("Enter the first number: "))
    secondInt = int(input("Enter the second number: "))   
    product = firstInt
    counter = 1

    # Handles the case in which second integer is 0 (i.e. firstInt^0 = 1) before execution
    if secondInt == 0:
       print(firstInt, " ** ",secondInt," = 1")
    else:
        # Loops through and performs multiplication process until counter < secondInt 
        while counter < secondInt:
              # Performs multiplication process
              exponentCalculation = product * firstInt

              # Stores product for next multiplication execution
              product = exponentCalculation 
              counter += 1
               
        # Output final exponentation product 
        print(firstInt," ** ",secondInt," = ", product)


main()
