# File: hw2_part1.py
# Author: Dane Magbuhos
# Date: 09/17/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program simulates a "procrastination reprimand" by asking 
#              the user how long they waited to start on the assignments for 
#              project 1. The user was given 6 days until the design is due, 
#              and 13 days until the project is due.

def main():
#   Grabs amount of days left for design and project phases from user.
    print("For project 1, you have 6 days to finish the design, and 13 days to finish the project.")
    designNum = int(input("Days left when you start the design: "))
    projectNum = int(input("Days left when you start the project: "))

#   This section evaluates the inputs and outputs an appropriate response.        
    if designNum == 0 or projectNum == 0:
       print("Why would you wait so long!? :(")
#   Checks to see if designNum equals 6 and project is in between or equal to 10 through 13 
    elif designNum == 6:
         if projectNum >= 10 and projectNum <= 13:
            print("Wow, you started really early! Great job! :)")
    else:
        print("Good luck on the project! You can do it!")

#   Output below is used to space out results during exection of program.
    print(" ")
       
main()
