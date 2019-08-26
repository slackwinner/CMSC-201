# File: hw2_part4.py
# Author: Dane Magbuhos
# Date: 09/17/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program simulates a simple calculator that`s
#              capable of performing seven basic arithmetic operations
#              using two integers.

def main():
#   Lists options for user to choose and grabs user input
    print("You can perform many operations with this program:")
    print("add, subtract, multiply, divide, int divide, mod, and exponents")
    operation = input("Which operation do you want to perform? ")
    firstNum = int(input("Enter the first number of the operation: "))
    secondNum = int(input("Enter the second number of the operation: "))

#   Executes and outputs appropriate response based on user`s input    
    if operation == "add":
       print(firstNum," + ",secondNum," = ",firstNum + secondNum)
    elif operation == "subtract":
         print(firstNum," - ",secondNum," = ",firstNum - secondNum)
    elif operation == "multiply":
         print(firstNum, " * ",secondNum," = ",firstNum * secondNum)
    elif operation == "divide":
         print(firstNum, " / ",secondNum," = ",firstNum / secondNum)
    elif operation == "int divide":
         print(firstNum, " // ", secondNum," = ",firstNum // secondNum)
    elif operation == "mod":
         print(firstNum," % ",secondNum," = ",firstNum % secondNum)
    elif operation == "exponents":
         print(firstNum," ** ",secondNum," = ",firstNum ** secondNum)
    else:
       print("Invalid Operation")

main()
