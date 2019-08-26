# File:    proj1.py
# Author:  Dane Magbuhos
# Date:    10/19/17
# Section: 20
# E-mail:  mag4@umbc.edu
# Description: This program allows a user to "load in"
#              a database of their choosing, and to either
#              search the database or create a playlist of
#              length 10 or less based on year, artist, or genre.

# main menu options
USER_QUIT    = -1
MENU_SEARCH  = 0
MENU_CREATE  = 1

MIN_SONG_NUM = 0   # minimum number of songs in a playlist
MAX_SONG_NUM = 10  # maximum number of songs in a playlist

# these constants are used to give names to the columns of the 2D list
YEAR     = 0
ARTIST   = 1
TITLE    = 2
GENRE    = 3
DURATION = 4
TEMPO    = 5

# these constants are used to give names to the 2D playlist
PLAYLIST_YEAR = 1
PLAYLIST_ARTIST = 2
PLAYLIST_GENRE = 3

DETAIL_MIN = YEAR   # minimum value; used for getValidInput()
DETAIL_MAX = TEMPO  # maximum value

ROW_VALUE = YEAR # Used to start at first row
COLUMN_VALUE = YEAR # Used to start at first column

PLAYLIST_MIN = ARTIST # minimum value; used for getValidInput() 
PLAYLIST_MAX = GENRE  # maximum value; used for getValidInput()


############################################################################
# make2DList() constructs a 2D list from a file that contains information
#              about songs in a music library, such as year and artist
# Input:       filename;   a string of the music library's file name
# Output:      resultList; a 2D list that contains all the songs within file

def make2DList(filename):
    fileObj = open(filename)
    lines = fileObj.readlines()
    fileObj.close()

    resultList = []
    index = 0

    while index < len(lines):
        line = lines[index].strip().split(",")
        line[YEAR]     = int(line[YEAR]) 
        line[DURATION] = float(line[DURATION])
        line[TEMPO]    = float(line[TEMPO])
        resultList.append(line)
        index += 1

    return resultList

##############################################################
# displayMainMenu() prints out the main menu of the program
# Input:  None;Takes in nothing (the menu is always the same)
# Output: Returns nothing; since it is a print function

def displayMainMenu():
    print("What would you like to do next?")
    print("    0) Perform a search")
    print("    1) Create a playlist",end="\n\n")

##############################################################
# displayOptions() prints out a list of six different traits 
#                  shown for each song
# Input:  None; Takes in nothing (the menu is always the same)
# Output: Returns nothing; since it is a print function

def displayOptions():
    print("    Index Value")
    print("    0 - Year")
    print("    1 - Artist")
    print("    2 - Title")
    print("    3 - Genre")
    print("    4 - Duration")
    print("    5 - Tempo",end="\n\n")

##############################################################
# displayPLOptions() prints out three different options for
#                    creating a playlist
# Input:  None; Takes in nothing (the menu is always the same)
# Output: Returns nothing; since it is a print function

def displayPLOptions():
    print("    1 - Year")
    print("    2 - Artist")
    print("    3 - Genre")

##############################################################
# printSongs() prints the details of every song in the given 
#              2D list
# Input:  songs; 2D list of detailed songs
# Output: Returns nothing; since it is a print function

def printSongs(songs):

    row = ROW_VALUE

    # Traverses through 2D list and outputs the song info
    while row < len(songs):
        col = COLUMN_VALUE
        while col < len(songs[row]):
            print(songs[row][col],end=" ")
            col += 1

        # Prepares for the next row of song info
        print()
        row += 1

    # Outputs empty statement for spacing purposes in output
    print(" ")

#############################################################
# getValidInput() Gets a valid integer from the user that
#                 falls within a specified range
# Input:  prompt; a integer to use when asking for input
#         minimum; a integer used to specify lower extreme
#         maximum; a integer used to specify upper extreme
# Output: prompt; an integer within the range

def getValidInput(prompt, minimum, maximum):

    inputValid = False

    # Outputs blank space for spacing purposes in output
    print(" ")

    while inputValid != True:
        # Only validates menu option
        if maximum == MENU_CREATE:
            # Grabs user`s menu choice
            prompt = int(input("Enter a menu choice (0 - 1) or '-1' to exit: "))
            # Checks to see if user entered sentienl value or one of the two menu choices
            if prompt == USER_QUIT or prompt == minimum or prompt == maximum:
               inputValid = True
            else:
                print("Invalid Menu Choice")

        # Only validates column option 
        if maximum == DETAIL_MAX:
            # Grabs user`s column choice
            prompt = int(input("Enter a column choice (0 - 5): "))
            # Checks if user`s column choice is valid
            if prompt < minimum or prompt > maximum:
                print("Invalid Column Choice")
            else: 
                inputValid = True
        
        # Only validates playlist option
        if maximum == PLAYLIST_MAX:
            # Grabs user`s playlist choice
            prompt = int(input("Choose a playlist to make: "))
            # Checks if user`s playlist option is valid
            if prompt < minimum or prompt > maximum:
                print("Invalid Playlist Option")
            else:
                inputValid = True

        # Only validates length of playlist value
        if maximum == MAX_SONG_NUM:
            # Grabs user`s preferred length of playlist
            prompt = int(input("Enter the length of your playlist (0-10): "))
            # Checks to see if length input is valid
            if prompt < minimum or prompt > maximum:
               print("Invalid Playlist Length")
            else:
                inputValid = True

    return prompt

################################################################
# colToString() converts a number to corresponding heading
# Input:  value; an integer that correlates with column heading
# Output: column; a string that contains specific info the user
#                 wants to search for

def colToString(value):
    
    sentenceTemplate = "Enter the "
    sentenceTemplateTwo = " you want to search for: "
    
    if value == YEAR:
       column = input(sentenceTemplate + "year" + sentenceTemplateTwo)
    elif value == ARTIST:
        column = input(sentenceTemplate + "artist" + sentenceTemplateTwo)
    elif value == TITLE:
        column = input(sentenceTemplate + "title" + sentenceTemplateTwo)
    elif value == GENRE:
        column = input(sentenceTemplate + "genre" + sentenceTemplateTwo)
    elif value == DURATION:
        column = input(sentenceTemplate + "duration" + sentenceTemplateTwo)
    else:
        column = input(sentenceTemplate + "tempo" + sentenceTemplateTwo)
    
    print(" ")
    
    return column

######################################################################
# songToString() converts 2D list of each song into a single string
# Input:  song; a 1D list that contains detailed parts of a song
# Output: songInfo; a string that contains combined parts of the song 

def songToString(song):

    space = " - "
    
    # Converts 1D list of song info into specified format
    songInfo = song[YEAR],space,song[GENRE],space,song[ARTIST],space,song[TITLE]

    return songInfo

###################################################################
# search() Creates a 2D list of songs that match the value 
#          being searched for in the selected column
# Input:  songs; a 2D list that contains all the songs within file
#         col; a string that contains corresponding column heading
#         value; a string that`s being searched for
# Output: searchResult; a 2D list of all the songs that matched the 
#                       search value 

def search(songs, col, value):
    
    row = ROW_VALUE
    searchResult = []

    # Traverses through 2D list
    while row < len(songs):
        column = COLUMN_VALUE
        foundValue = []

        # Handles string case within 2D list
        if str(songs[row][col]) == str(value):
            # Traverses through entire row if song info matches value
            while column < len(songs[row]):
                foundValue.append(songs[row][column])
                column += 1

            # Converts song info into finalized string
            songInfo = songToString(foundValue)

            # Stores populated string info into search result list
            searchResult.append(songInfo)

        # Handles float case within 2D list
        elif col == DURATION or col == TEMPO:
             floatSearch = float(value)
             if float(songs[row][col]) >= floatSearch:
                 # Traverses through entire row if song info is greater
                 # or equal to value
                while column < len(songs[row]):
                    foundValue.append(songs[row][column])
                    column += 1

                # Converts song info into finalized string
                songInfo = songToString(foundValue)

                # Stores populated song info into search result list
                searchResult.append(songInfo)

        row += 1
    
    return searchResult

############################################################################
# createPlaylist() creates a 2D list of all songs based on the user`s
#                  preferred playlist type
# Input:  songs; a 2D list of all the songs from file
#         choice; an integer that represents user`s playlist type preference
#         value; an integer that represents the length of the playlist
# Output: playlist; a 2D list of the user`s preferred type of playlist 
def createPlaylist(songs, choice, length):

    playlist = []

    # Grabs value based on the choice the user picked and converts choice
    # into appropriate index prior to finding specified songs
    if choice == PLAYLIST_YEAR:
        value = input("Enter a year to make a playlist of: ")
        category = YEAR
    elif choice == PLAYLIST_ARTIST:
        value = input("Enter an artist to make a playlist of: ")
        category = ARTIST
    else:
        value = input("Enter a genre to make a playlist of: ")
        category = GENRE

    # Calls search function to find specified songs
    playlistResult = search(songs, category, value)

    # Truncates song amount to user`s preferred length
    playlist = playlistResult[ : length]

    return playlist

def main():
                 
    prompt = DETAIL_MIN
    
    print("This is the Music Organizer 3000!",end="\n\n")

    # Grabs user`s file input and reads in specified file into 2D list
    fileInput = input("Enter the file name you would like to load:  ")
    songs = make2DList(fileInput)
    
    # Calls displayMainMenu function to output main menu to user
    displayMainMenu()

    # Calls getValidInput in order to receieve a valid menu option
    userChoice = getValidInput(prompt, MENU_SEARCH, MENU_CREATE)

    # Allows infinite usage of provided options until user enters USER_QUIT value
    while userChoice != USER_QUIT:
        # Handles search option
        if userChoice == MENU_SEARCH:
            # Displays column search options 
            displayOptions()

            # Gathers column and search value from user before performing search
            column = getValidInput(prompt, DETAIL_MIN, DETAIL_MAX)
            value = colToString(column)

            # Gathers up results based on user`s criteria
            searchResult = search(songs, column, value)
            
            # Checks to see if 2D list is populated before outputting appropriate response
            if len(searchResult) == DETAIL_MIN:
                print("Your search returned no results",end="\n\n")
            else:
                print("Found the following: ")
                printSongs(searchResult)

            # Displays organizer`s main options 
            displayMainMenu()
            userChoice = getValidInput(prompt, MENU_SEARCH, MENU_CREATE)
                     
        # Handles playlist option
        elif userChoice == MENU_CREATE:
            # Displays playlist options
            displayPLOptions()
            
            # Gathers up user`s choice and length of playlist before creating playlist 
            playlistChoice = getValidInput(prompt, PLAYLIST_MIN, PLAYLIST_MAX)
            playlistLength = getValidInput(prompt, MIN_SONG_NUM, MAX_SONG_NUM)

            # Creates playslist based on user`s criteria
            playlist = createPlaylist(songs, playlistChoice, playlistLength)

            # Checks to see if 2D list is populated before outputting appropriate response
            if len(playlist) == DETAIL_MIN:
              print("Problem: The given value was not found",end="\n\n")
              print("Unable to create a playlist based on that criteria",end="\n\n")

            else:
                # Outputs blank statement for spacing purposes in output
                print(" ")
                print("Created this playlist: ")
                printSongs(playlist)

            # Display`s organizer`s main options
            displayMainMenu()
            userChoice = getValidInput(prompt, MENU_SEARCH, MENU_CREATE)

    # Only outputs until after user enters USER_QUIT value
    print("Thanks for using the Music Organizer 3000!")

main()

