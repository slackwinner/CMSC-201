# File: hw2_part2.py
# Author: Dane Magbuhos
# Date: 09/20/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program rounds to the nearest whole number
#              based up the user`s preference to round up or down.

def main():
#   Grabs user`s inputed number and rounding preference
    numberInput = float(input("Input the number you are rounding: "))
    roundingPreference = input("Do you want to round up or down? ")

#   Isolates decimal value and checks if isolatedDecimal is equal to 0 before execution
    typeCastedNum = int(numberInput)
    isolatedDecimal = numberInput - typeCastedNum
    if isolatedDecimal == 0:
       print("Original Value: ",typeCastedNum," Rounded Value: ",typeCastedNum)

#   Rounds postive integer upwards if subtractedResults is < 0.5 
    elif roundingPreference == "up":
         print("Rounding up ...")
         if numberInput >= 0:
            if isolatedDecimal < 0.5:
               print("Original Value: ",numberInput," -> Rounded Value: ",typeCastedNum)
            else:
                print("Original Value: ",numberInput," -> Rounded Value: ",typeCastedNum + 1)

#   Rounds negative integer upwards if subtractedResults is > -0.5
         elif numberInput < 0:
              if isolatedDecimal > -0.5:
                 print("Original Value: ",numberInput," -> Rounded Value: ",typeCastedNum)
              else:
                  print("Original Value: ",numberInput," -> Rounded Value: ",typeCastedNum - 1)

#   Rounds both positve and negative integers downwards 
    elif roundingPreference == "down":
         print("Rounding down ...")
         typeCastedNum = int(numberInput)
         print("Original Value: ",numberInput," -> Rounded Value: ",typeCastedNum)

#   Handles invalid commands
    else:
        print("Invalid Command")
        print("Original Value: ",numberInput," Rounded Value: ",numberInput)

# Outputs blank space for spacing purposes in output                 
    print()
main() 
