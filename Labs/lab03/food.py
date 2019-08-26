# File: food.py
# Author: Dane Magbuhos
# Date: 9/20/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: Asks the user what they had for breakfast and outputs excellent 
#              choice when they enter a specific input.

def main():
    
    foodInput = input("Please enter what you ate for breakfast: ")
    if foodInput == "green eggs" or foodInput == "ham":
       print("Excellent choice!")
    else:
        print(foodInput," is a strange choice for breakfast")



main()
