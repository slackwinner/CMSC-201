# File: hw5_part3.py
# Author: Dane Magbuhos
# Date: 10/8/17
# Section: 20
# E-mail: mag4@umbc.edu
# Description: This program checks the grammar of a sentence.


EXIT = "" # Allows user to stop entering inputs
FINAL_INDEX = 1 # Used to format index

###############################################################################
# checkCapital() Checks to see if first character in first word is capitalized
# Input: sentence; a string that`s going to be checked for capital letter
# Output: None
def checkCapital(sentence):
    index = 0
    capitalLetter = sentence[index].upper()
    
    # Determines if first character of string is capitalized and outputs appropriate response
    if sentence[index] != capitalLetter:
        print("WRONG - Sentences start with a capital letter.")
    else:
        print("Correct Capitalization!")

#########################################################################
#checkPunctuation() Checks to see if sentence ends in a punctuation 
# Input: sentence; a string that`s going to be checked for a punctuation
# Output: None
def checkPunctuation(sentence):
    index = len(sentence) - FINAL_INDEX
    
    # Determines if last character of string is equal to one of the punctuations
    if sentence[index] == "?" or sentence[index] == "!" or sentence[index] == ".":
       print("Correct Punctuation!")
    else:
        print("WRONG - Sentences use punctuation.")

def main():

    validInput = True
    while validInput == True:
          # Grabs user`s sentence input
          sentence = input("Enter a sentence (enter nothing to quit): ")

          # Checks to see if sentence is not equal to EXIT
          if sentence == str(EXIT):
             validInput = False
          else:
              # Calls functions and passes input for validation 
              checkCapital(sentence)
              checkPunctuation(sentence)


main()
