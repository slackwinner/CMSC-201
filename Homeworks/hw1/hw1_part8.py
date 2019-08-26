# File: hw1_part8.py
# Author: Dane Magbuhos
# Date: September 10th, 2017
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program asks the user for information
#              about how many items of food they want to
#              buy at a fixed price, calculates and outputs
#              the total cost of the meal.

#Declares fixed prices for different meal types.
appetizerPrice = 9.5
mainDishPrice = 15.8
dessertPrice = 6.55

#Grabs information about how many much food the user wants to order.
print("Appetizers cost: ",appetizerPrice)
appetizerNum = int(input("How many appetizers would you like to order? "))

print("Main dishes cost: ",mainDishPrice)
mainDishNum = int(input("How many main dishes would you like to order? "))

print("Desserts cost: ",dessertPrice)
dessertNum = int(input("How many desserts would you like to order? "))

#Calculates total amount for the user`s order.
totalAmount = (appetizerPrice * appetizerNum) + (mainDishPrice * mainDishNum)\
 + (dessertPrice * dessertNum)

#Outputs total amount.
print("Total Amount for Meal: ",totalAmount)
