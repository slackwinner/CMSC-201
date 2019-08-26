# File: hw1_part4.py
# Author: Dane Magbuhos
# Date: September 10th, 2017
# Section: 20
# Email: mag4@umbc.edu
# Description: This program asks the user for information about
#              a car they`re buying, and calculates and outputs
#              the total cost of the car.

#Grabs input from user.
carCost = float(input("How much does the car cost? "))
warrantyCost = float(input("How much does the warranty cost? "))
fees = float(input("How much are the fees? "))
taxes = float(input("How much are the taxes? "))

#Calculates total costs of the car.
totalCost = carCost + warrantyCost + fees + taxes

#Outputs results based on total cost.
print("Total Cost of the Car: ",totalCost)
