# File: hw4_part4.py
# Author: Dane Magbuhos
# Date: 10/1/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program asks the user for the number of tests they`ve taken
#              and then asks for their grade for each test.

EXTRA_CREDIT_ALLOWED = "yes" # Allows user to input grade higher than HIGH_GRADE_BOUND
LOW_GRADE_BOUND = 0 # Set to lowest grade bound 
HIGH_GRADE_BOUND = 100 # Sets to highest grade bound

def main():
    
    # Grabs amount of test taken from user
    amountOfTests = int(input("Enter number of tests taken: "))

    # Outputs blank statement for spacing purposes in output
    print(" ")

    highGrade = 0
    testCounter = 1

    # Loops through and asks user what grade they got for each test
    while testCounter <= amountOfTests:
        print("For Test # ",testCounter," was extra credit allowed?")
        extraCredit = input("Please enter 'yes' or 'no': ")
        gradeInput = int(input("Enter your grade for the test: "))

        # If extra credit is not allowed, grade input has to be in between 0 - 100
        if extraCredit != EXTRA_CREDIT_ALLOWED:
            while gradeInput < LOW_GRADE_BOUND or gradeInput > HIGH_GRADE_BOUND:
                print("Test grade must be between 0 and 100")
                gradeInput = int(input("Enter your grade for the test: "))

        # If extra credit is allowed, grade input must be greater than 0
        elif extraCredit == EXTRA_CREDIT_ALLOWED:
            while gradeInput < LOW_GRADE_BOUND:
                print("Test grade cannot be negative")
                gradeInput = int(input("Enter your grade for the test: "))

        # Keeps track of the highest grade based on user`s grade input
        if gradeInput > highGrade:
           highGrade = gradeInput

        testCounter += 1

        # Outputs blank statement for spacing purposes in output
        print(" ")

    # Outputs high grade based on user`s input
    print("The highest grade received was: ",highGrade)
           
main()
