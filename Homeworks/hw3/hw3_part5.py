# File: hw3_part5.py
# Author: Dane Magbuhos
# Date: 9/24/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program prints numbers from 1 through 77 and outputs
#              one of three special cases for certain numbers.

def main():

    counter = 1
   
    # Loops through and outputs numbers from 1 - 77
    while counter <= 77:

          # If current integer is divisible by 4 and 5, outputs a specific string
          if counter % 4 == 0 and counter % 5 == 0:
             print("The year 2020 is coming soon!")

          # If current integer is only divisible by 5, outputs a specific string
          elif counter % 5 == 0:
               print("Where do you see yourself in five years?")

          # If current integer is only divisible by 4, outputs a specific string
          elif counter % 4 == 0:
               print("Four leaf clovers are lucky!")
          else:
              # Outputs current integer value
              print(counter)
          counter += 1
     

main() 
