
# File: hw2_part5.py
# Author: Dane Magbuhos
# Date: 09/17/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program plays a simple game, where it asks the player
#              about their dog, and attempts to guess the dog`s breed answer
#              based on their answers.

def main():
#   This section outputs appropriate response based on user`s input
    print("Please enter 'yes' or 'no' to these questions")
    answerOne = input("Does your dog have a curly tail? ")

#   If answerOne is yes, the breed search is narrowed to Eurasier and Basenji
    if answerOne == "yes":
       answerTwo = input("Can your dog bark? ")
       if answerTwo == "yes":
          print("Your dog is a Eurasier!")
       else:
          print("Your dog is a Basenji!")

#   If answerOne is no, the breed search is narrowed to Pharaoh Hound, Retriever, and Sheepdog
    elif answerOne == "no":
         answerThree = input("Do the dog`s ears stick up? ")
         if answerThree == "yes":
            print("Your dog is a Pharaoh Hound!")

#   If answerThree is no, the breed search is narrowed to Retriever and Sheepdog
         elif answerThree == "no":
              answerFour = input("Does the dog come in multiple colors? ")
              if answerFour == "yes":
                 print("Your dog is a Chesapeake Bay Retriever!")
              else:
                 print("Your dog is a Maremma Sheepdog!")

#   Outputs blank string for spacing purposes during execution of program   
    print(" ")

main()
