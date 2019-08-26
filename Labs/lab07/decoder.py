# File:    decoder.py
# Started: by Dr. Gibson
# Author:  Dane Magbuhos
# Date:    10/16/17
# Section: 20
# E-mail:  mag4@umbc.edu
# Description:
#   This file contains python code that uses a function to 
#   pull out the uppercase letters from a list of strings
#   to decode a secret message.


######################################################################
# decode() decodes a message by extracting all of the 
#          capital letters to reveal the hidden meaning
# Input:   msgList; a list of strings
# Output:  secret;  a string containing the hidden message
def decode(msgList):
    secret = ""
    char = "?"
    secretMessage = []
    wordIndex = 0
    index = 0
    
    # Traverses through msgList list
    while index < len(msgList):
       word =  msgList[index]
       # Traverses through a word within msgList
       while wordIndex < len(word):
           # Checks to see if character in word is equal to upper case version and not char
           # before adding to secret message list
           if word[wordIndex] == word[wordIndex].upper() and word[wordIndex] != char:
               secretMessage.append(word[wordIndex]) 
           wordIndex += 1

       # Resets wordIndex to 0 after iteration of word
       if wordIndex == len(word):
           wordIndex = 0
       index += 1
    
    # Combines characters together and returns secret 
    secret = "".join(secretMessage)
    return secret

def main():
    # message lists
    msg1 = ["thiS", "lifE", "Cannot", "Really", "bE", "True"]
    msg2 = ["wonDering", "hOw", "Good", "scoreS", "cAn", "regulaRly", \
                "bE", "manaGed?", "yOu", "shOuld", "stuDy"]
    msg3 = ["studyinG", "Once", "thrOugh", "miDnight", "wiLl", \
                "caUse", "inComplete", "Knowledge", "Of", "iNformation", \
                "noT", "Helping", "thE", "earnEd", \
                "eXam", "grAde", "iMprove"]

    # calling the decode function for each
    ans1 = decode(msg1)
    ans2 = decode(msg2)
    ans3 = decode(msg3)

    # printing out the secret messages
    print("Message 1's secret was:")
    print(ans1)
    print()

    print("Message 2's secret was:")
    print(ans2)
    print()

    print("Message 3's secret was:")
    print(ans3)
    print()



main()

