# File: hw3_part4.py
# Author: Dane Magbuhos
# Date: 9/24/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program calculates how much money will be
#              raised during a charity run.

def main():

    # Grabs pledge input from user
    amountOfPledges = int(input("How many pledges did you secure? "))

    counter = 0
    pledgeCounter = 1
    totalAmount = 0

    # Loops through until amount per pledge is added and accounted for
    while counter < amountOfPledges:
          # Outputs pledge counter number
          print("For pledge # ",pledgeCounter)
          
          # Grabs amount of money that was pledged from user
          moneyPledged = float(input("How much money was pledged? "))

          # Adds and stores current total amount based on user`s money input
          totalAmount = totalAmount + moneyPledged
          pledgeCounter += 1
          counter += 1 
    
    # Grabs amount of miles ran from user
    miles = float(input("How many miles did you run for charity? "))

    # Calculates amount earned and outputs results
    totalAmount = miles * totalAmount
    print("Based on you ",miles,"miles you earned $",totalAmount,"for the charity")

main()
