# File: lab12.py
# Author: Dane Magbuhos
#
#
#
#




def main():

    print("Dogs are brought to adoption events based on time at the shelter.")

    minInput = int(input("Please enter the minimum stay time for the dogs: "))
    fileName = "dogData.txt"
    fileNameTwo = "dogList.txt"
    
    dogFile = open(fileName)
    listOfDogs = open(fileNameTwo, "w")
    dogList = dogFile.readlines()

    for i in range(len(dogList)):
        line = dogList[i].strip().split(",")
        name = line[0]
        breed = line[1]
        gender = line[2]
        age = line[3]
        minimum = int(line[4])
#        print(name, " ", breed, " ", gender, " ", age," ", minimum)
        if minimum > minInput:
           listOfDogs.write(str(name) + "," + str(breed) + "," + str(gender)+ ","  + str(age)+ "," + str(minimum)+"\n")

    dogFile.close()
    listOfDogs.close()

main()
