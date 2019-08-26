# File: hw5_part6.py
# Author: Dane Magbuhos
# Date: 10/9/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program takes the user`s temperature inputs and
#              calculates the average temperature.

EXIT = "STOP" # Used to allow user to stop entering temperature inputs
INCREMENT_INDEX = 1 # Used to increment index based on specifed number

########################################################
# average() calcualtes and returns the average
# Input:    numList; a list of floats
# Output:   avgNum; a float, average of list`s numbers
def average(numList):

    listLength = len(numList)
    currentTotal = 0
    index = 0

    # Traverses through list and calculates the total amount of temperatures 
    while index < listLength:
       currentTotal = currentTotal + numList[index]
       index += INCREMENT_INDEX

    # Calculates average temperature
    avgNum = currentTotal/listLength

    # Returns average temperature to main function
    return(avgNum)

def main():

    validInput = True
    tempList = []
    
    # Allows user to enter in as many inputs as desired
    while validInput ==  True:

        # Grabs temperature input (Note: Read in as a string)
        tempInput = input("Enter a temperature, 'STOP' to exit: ")

        # If tempInput is equal to "EXIT" value, calls average function and 
        # passes temp list to function and outputs average temp
        if tempInput == str(EXIT):
            averageTemp = average(tempList)
            print("Average Temperature: ",averageTemp,end="\n\n")
            validInput = False
        else:
            # Converts tempInput as a float datatype before adding to 
            # temp list
            tempInput = float(tempInput)
            tempList.append(tempInput)

main()
