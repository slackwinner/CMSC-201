# File: hw2_part3.py
# Author: Dane Magbuhos
# Date: 09/17/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program simulates a simple deli ordering counter that
#              asks the user what they like on their sandwich, as a side,
#              and to drink. After ordering, the program informs them of 
#              what they ordered and outputs invalid choices in, if there
#              are any, at the end.

def main():
#   Grabs input from user and outputs blank statement for spacing purposes
#   during execution
    print("Welcome to CMSC 201 Deli")
    print("Sandwich Choices:'ham','cheese', or'veggie'")
    print("Side Choices: 'cookies', 'chips', or 'pickle'")
    print("Drink Choices: 'water', 'lemonade', or 'soda'")
    print(" ")
    sandwichChoice = input("Please choose your sandwich type: ")
    sideChoice = input("Please choose your side: ")
    drinkChoice = input("Please choose your drink: ")
    print(" ")

#   Evaluates input from choice and outputs appropriate response
    if sandwichChoice == "ham" or sandwichChoice == "cheese" or sandwichChoice == "veggie":
       print("You chose a ",sandwichChoice," sandwich.")
    else:
       print("A ",sandwichChoice," is not a proper choice for a sandwich.")

    if sideChoice == "cookies" or sideChoice == "chips" or sideChoice == "pickle":
       print("You chose ",sideChoice," for your side.")
    else:
       print("A ",sideChoice," is not a proper choice for a side.")

    if drinkChoice == "water" or drinkChoice == "lemonade" or drinkChoice == "soda":
       print("You chose ",drinkChoice," for your drink.")
    else:
       print("A ",drinkChoice,"is not a proper choice for a drink.")

#   Outputs blank statement for spacing purposes during execution
    print("Enjoy your meal!")
    print(" ")

main() 
