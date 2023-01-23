import random # to give the ai random positioning

# create lists to store values into leaving them empty spaces to be filled later
firstColumn = [" ", " ", " "]
secondColumn = [" ", " ", " "]
thirdColumn = [" ", " ", " "]
fullSet = [firstColumn, secondColumn, thirdColumn] # list of lists to get 3x3 grid

# count turns and spaces left on the grid/set
roundCount = 0
fullCount = 0

introCheck = False # check if intro has played
finishedWinner = False # check for a winner when the game has ended
fullBoard = False # check if the board is full to end the game in a draw

# board made to look nice for player calling back to the lists
def board(first, second, third):
    print("  1|2|3")
    print(f"1 {first[0]}|{second[0]}|{third[0]}")
    print("  -----")
    print(f"2 {first[1]}|{second[1]}|{third[1]}")
    print("  -----")
    print(f"3 {first[2]}|{second[2]}|{third[2]}")

# available move the player can do with attempts to patch out some bugs that could appear
def userMove():
    playerMove = input("Please enter the coordinates of your next move (x,y): ")
    while len(playerMove) < 3:
        playerMove = input("Please enter a x AND y coordinate for your next move (x,y): ")
    playerMoveSplit = playerMove.split(",")
    playerMoveX = int(playerMoveSplit[0]) - 1
    playerMoveY = int(playerMoveSplit[1]) - 1
    while 0 > playerMoveX or playerMoveX > 2 or 0 > playerMoveY or playerMoveY > 2:
        playerMove = input("Please enter a VALID coordinate between 1 to 3 x and 1 to 3 y (x,y): ")
        playerMoveSplit = playerMove.split(",")
        playerMoveX = int(playerMoveSplit[0]) - 1
        playerMoveY = int(playerMoveSplit[1]) - 1
    while fullSet[playerMoveX][playerMoveY] != " ":
        playerMove = input(f"Unfortunately, the ({playerMove}) move you have entered is already used, please enter a new move? ")
        playerMoveSplit = playerMove.split(",")
        playerMoveX = int(playerMoveSplit[0]) - 1
        playerMoveY = int(playerMoveSplit[1]) - 1
    return playerMoveX, playerMoveY

# random movement of ai
def aiMove():
    aiX = random.randrange(3)
    aiY = random.randrange(3)
    while fullSet[aiX][aiY] != " ":
        aiX = random.randrange(3)
        aiY = random.randrange(3)
    return aiX, aiY

# cycles through each possible victory scenario, if any of them occur the game says we have a winner and which character
# it was
def victoryEngine():
    winner = False
    winnerType = ""
    # x
    for column in range(3):
        if fullSet[column][0] == "x":
            if fullSet[column][1] == "x":
                if fullSet[column][2] == "x":
                    winner = True
                    winnerType = "x"
    for row in range(3):
        if fullSet[0][row] == "x":
            if fullSet[1][row] == "x":
                if fullSet[2][row] == "x":
                    winner = True
                    winnerType = "x"
    if fullSet[0][0] == "x":
        if fullSet[1][1] == "x":
            if fullSet[2][2] == "x":
                winner = True
                winnerType = "x"
    if fullSet[2][0] == "x":
        if fullSet[1][1] == "x":
            if fullSet[0][2] == "x":
                winner = True
                winnerType = "x"
    # o
    for column in range(3):
        if fullSet[column][0] == "o":
            if fullSet[column][1] == "o":
                if fullSet[column][2] == "o":
                    winner = True
                    winnerType = "o"
    for row in range(3):
        if fullSet[0][row] == "o":
            if fullSet[1][row] == "o":
                if fullSet[2][row] == "o":
                    winner = True
                    winnerType = "o"
    if fullSet[0][0] == "o":
        if fullSet[1][1] == "o":
            if fullSet[2][2] == "o":
                winner = True
                winnerType = "o"
    if fullSet[2][0] == "o":
        if fullSet[1][1] == "o":
            if fullSet[0][2] == "o":
                winner = True
                winnerType = "o"
    return winner, winnerType

# simple intro to play when starting
def intro():
    print("Welcome to Tic-Tac-Toe!")
    userInputType = input("Would you like to be 'x' or 'o'? ")

    while userInputType != "x" and userInputType != "o":
        userInputType = input("Sorry only input must be 'x' or 'o'? ")
    return True, userInputType

# to keep the loop running
while 1:

    # intro check to see if it has run, assigning the variables from its return
    if introCheck is False:
        workableIntro = intro()
        introCheck = workableIntro[0]
        userInputType = workableIntro[1]

    board(firstColumn, secondColumn, thirdColumn) # displays the board

    roundCount += 1 # counts the turn

    fullCount = 0 # sets the counter to check if the board is empty to zero to start counting the board
    for column in range(3):
        for row in range(3): # cycles through columns and rows
            if fullSet[column][row] == " ":
                fullCount += 1 # empty spaces are added
            elif column == 2 and row == 2 and fullCount == 0: # if it reaches the end of all the columns and rows without an empty space it checks the board as full
                fullBoard = True

    # ensuring the board isn't full, allows the user to input a coord into the set
    if fullBoard is False:
        if userInputType == "x":
            workableUserMove = userMove()
            fullSet[workableUserMove[0]][workableUserMove[1]] = "x"
        elif userInputType == "o":
            workableUserMove = userMove()
            fullSet[workableUserMove[0]][workableUserMove[1]] = "o"

    # rechecks if the board is full
    fullCount = 0
    for column in range(3):
        for row in range(3):
            if fullSet[column][row] == " ":
                fullCount += 1
            elif column == 2 and row == 2 and fullCount == 0:
                fullBoard = True

    # ensuring the board isn't full, allows the ai to input a coord into the set
    if fullBoard is False:
        if userInputType == "x":
            workableAiMove = aiMove()
            fullSet[workableAiMove[0]][workableAiMove[1]] = "o"
        elif userInputType == "o":
            workableAiMove = aiMove()
            fullSet[workableAiMove[0]][workableAiMove[1]] = "x"

    # rechecks if the board is full
    fullCount = 0
    for column in range(3):
        for row in range(3):
            if fullSet[column][row] == " ":
                fullCount += 1
            elif column == 2 and row == 2 and fullCount == 0:
                fullBoard = True

    # checks if victory conditions have been met and assigns them
    finishedWinner, finishedWinnerType = victoryEngine()

    # if a winner is present prints out messages based on if it is user or ai and asks to play again, resetting all
    # the checks and variables to allow the game to run again
    if finishedWinner:
        if userInputType == finishedWinnerType:
            board(firstColumn, secondColumn, thirdColumn)
            print(f"Congratulations! You won the game in just {roundCount} moves. This round is now over!")
        elif userInputType != finishedWinnerType:
            print(f"Unfortunately, you lost the game! The computer won in {roundCount} moves. This round is now over!")
        endGameInput = input("Would you like to go for another round or just end this game? (y/n) ")
        while endGameInput != "y" and endGameInput != "n":
            endGameInput = input("Please input y or n ")
        if endGameInput == "y":
            roundCount = 0
            fullCount = 0
            firstColumn = [" ", " ", " "]
            secondColumn = [" ", " ", " "]
            thirdColumn = [" ", " ", " "]
            fullSet = [firstColumn, secondColumn, thirdColumn]
            finishedWinner = False
            finishedWinnerType = ""
            fullBoard = False
            introCheck = False
        elif endGameInput == "n":
            break

    # similar to a winner being present however this is for if the board was full, and it was a draw instead
    if fullBoard:
        board(firstColumn, secondColumn, thirdColumn)
        print("The board was filled without a winner, it's a draw")
        endGameInput = input("Would you like to go for another round or just end this game? (y/n) ")
        while endGameInput != "y" and endGameInput != "n":
            endGameInput = input("Please input y or n ")
        if endGameInput == "y":
            roundCount = 0
            fullCount = 0
            firstColumn = [" ", " ", " "]
            secondColumn = [" ", " ", " "]
            thirdColumn = [" ", " ", " "]
            fullSet = [firstColumn, secondColumn, thirdColumn]
            finishedWinner = False
            finishedWinnerType = ""
            fullBoard = False
            introCheck = False
        elif endGameInput == "n":
            break
