# File: hw1_part6.py
# Author: Dane Magbuhos
# Date: September 10th, 2017
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program asks the user for information
#              about a bill they`ve received, and calculates
#              and outputs how much they should pay in total.

#Grabs user`s input.
totalBill = float(input("How much was the bill? "))
tax = float(input("How much is the tax in your area? "))
tip = float(input("What percentage do you want to tip? "))

#This section calculates the tax and tip from the total bill.
#Then calculates the total cost.
calculatedTax = totalBill * tax/100
calculatedTip = totalBill * tip/100
calculatedCost = totalBill + calculatedTax + calculatedTip

#Outputs total cost of meal.
print("Total cost of the meal:$",calculatedCost)
