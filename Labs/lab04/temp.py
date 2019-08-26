# File: temp.py
# Author: Dane Magbuhos
# Date: 9/27/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program finds the miniumum and maximum in a list of temperatures

def main():

    numInput = int(input("How many temperatures would you like to enter: "))
    count = 0 
    maxTemp = 0

    while(numInput <= 0):
          print("You must enter a number greater than zero: ")
          numInput = int(input("How many temperatures would you like to enter: "))
    

    tempInput = float(input("Enter a temperature: "))
    minTemp = tempInput

    while count < numInput - 1:
          tempInput = float(input("Enter a temperature: "))
          if tempInput > maxTemp:
             maxTemp = tempInput
          elif tempInput < minTemp:
               minTemp = tempInput
          count += 1
    print("Minimum Temperature: ",minTemp)
    print("Maximum Temperature: ",maxTemp)    



main()
