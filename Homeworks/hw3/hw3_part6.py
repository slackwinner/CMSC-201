# File: hw3_part6.py
# Author: Dane Magbuhos
# Date: 9/24/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program outputs a counting box based on the user`s 
#              width and height.


def main():

    # Grabs user`s width and height input
    widthInput = int(input("Enter a width: "))
    heightInput = int(input("Enter a height: "))

    # Calculates array based on user`s inputs
    totalArray = widthInput * heightInput
    counter = 1
    widthCounter = 0
    heightCounter = 0

    # Loops through and outputs integers per row based on widthInput and count up towards total array value (e.g. Width = 2; Height = 4; totalArray = 8)     
    while counter <= totalArray:
          print(counter, end=" ")
          counter += 1
          widthCounter += 1

          # Prepares next row prior to outputting another set of integers
          if widthCounter == widthInput:
             widthCounter = 0
             heightCounter += 1
             print() 

    # Ensures that amount of rows,from heightInput, are present before outputting
    # blank statement for spacing purposes in output
    if heightCounter == heightInput:
        print()            
                     
main()
