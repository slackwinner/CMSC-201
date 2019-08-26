# File: hw3_part7.py
# Author: Dane Magbuhos
# Date: 9/24/17
# Section: 20
# E-mail: mag@umbc.edu
# Description: This program draws a right triangle based on the 
#              user`s height and symbol preference.

def main ():

    # Grabs user`s height and symbol input
    height = int(input("Enter the height: "))
    symbol = input("Enter a single character for the symbol: ")

    rowCounter = 1
    widthCounter = 0

    # Loops through and outputs appropriate amount of designated symbol per row
    while rowCounter <= height:
          if widthCounter < rowCounter:
             print(symbol, end=" ")
             widthCounter += 1

          # Prepares next row prior to outputing another set of designated symbol
          elif widthCounter == rowCounter:
               rowCounter += 1
               widthCounter = 0
               print()

    # Outputs blank statement for spacing purposes in output
    print()
              
main()
