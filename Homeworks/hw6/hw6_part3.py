# File: hw6_part3.py
# Author: Dane Magbuhos
# Date: 11/14/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program recursively counts the number
#              of ears and horns in a line of horses and 
#              unicorns.

# Represents the amount of ears and horns that the horse and unicorn has
HORSE = 2
UNICORN = 3

# Represents even remainder
EVEN = 0

# Used to indicate if current equineAmount is even 
EVEN_MOD = 2

# Represents the final value of equineAmount
FINAL_VALUE = 0

# Used to decrease a number by given value
DECREMENT = 1


###########################################################
# count() This counts the amount of ears and horns based
#         on the provided amount of horses and unicorns
# Input:  equineAmount; an integer that represents amount 
#         of horses and unicorns in a line
# Output: total; an integer that represents the sum of all
#         ears and horns

def count(equineAmount):

   # Handles the FINAL_VALUE case (i.e. stops the count recursive calls)
   if equineAmount == FINAL_VALUE:
       return FINAL_VALUE
   
   # Adds horse amount to total if current number is even
   elif equineAmount % EVEN_MOD == EVEN:
       total = HORSE + count(equineAmount - DECREMENT)
       return total

   else:
       # Adds unicorn amount to total if current number is odd
       total = UNICORN + count(equineAmount - DECREMENT)
       return total


def main():

    equineAmount = int(input("How long is the line of equines? "))

    # Calls count function
    total = count(equineAmount)

    print("In a line of", equineAmount , "equines, there are", total ,"ears and horns.", "\n\n")


main()
