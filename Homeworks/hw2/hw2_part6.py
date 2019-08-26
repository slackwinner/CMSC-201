# File: hw2_part6.py
# Author: Dane Magbuhos
# Date: 09/17/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program asks the user to enter the day of the month
#              and outputs the corresponding day of the week.

def main():
#   Grabs input from user
    dayInput =int(input("Please enter the day of the month: "))
    numOfDaysPerWeek = 7

#   Checks to see if dayInput is out of range before performing calculation
    if dayInput < 1 or dayInput > 30:
       print("The date ",dayInput," is an invalid day.")

#   The remainder is calculated and used to find corresponding day   
    elif dayInput >= 1 and dayInput <= 30:
         dayMod = dayInput % numOfDaysPerWeek
         if dayMod == 0:
            print("Today is Thursday!")
         elif dayMod == 1:
              print("Today is Friday!")
         elif dayMod == 2:
              print("Today is Saturday!")
         elif dayMod == 3:
              print("Today is Sunday!")
         elif dayMod == 4:
              print("Today is Monday")
         elif dayMod == 5:
              print("Today is Tuesday!")
         elif dayMod == 6:
              print("Today is Wednesday!")    

#   Outputs blank statement for spacing purposes in output
    print()
main()
