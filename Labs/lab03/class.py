# File: class.py
# Author: Dane Magbuhos
# Date: 9/20/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program asks the user to input a  professor`s name 
#              and outputs an appropriate response back to the user


def main():

    professorName = input("Please enter in a professor name: ")
    if professorName == "Gibson" or professorName == "Neary":
       numOfStudents = int(input("How many students are in the class? "))
       if numOfStudents >= 80:
          print("Wow, so many options for study groups! ")
       elif numOfStudents >= 30 and numOfStudents < 80:
            print("You have so many chances to make new friends! ")
       else: 
            print("You`ll get to know all of your classmates really well ")

    else:
        print(professorName,"doesn`t teach CMSC 201! You`re in the wrong class!")

main()
