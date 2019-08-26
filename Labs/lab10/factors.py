# File: factors.py
# Author: Dane Magbuhos
# Date: 11/08/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program grabs all the factors of a specified number

LOWER_BOUND = 0

def validFactorInput(num):
#    print("Inside input: ")
    result = True

    if num <= LOWER_BOUND:
        result = False
    
    return result

def factor(num):

    factorList = []
    for i in range(1, num + 1):
        if num % i == 0 :
           factorList.append(i)

    for j in range(len(factorList)):
        print(factorList[j], " is a factor of ", num)


def main():

    valid = False

    factorInput = int(input("Enter a (positive) number to find the factors of: "))

    while valid != True:

        validInput = validFactorInput(factorInput)

        if validInput == False:
            factorInput = int(input("Sorry, enter a number greater than zero: "))
        else:
            # Exits out of while loop
            valid = True

    factor(factorInput)





main()
