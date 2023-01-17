def printoutGrid():
    fields = []
    for x in grid.values():
        fields.append(x)
    print(gridString.format(*fields))

grid = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

gridString = """
| {} | {} | {}
| {} | {} | {}
| {} | {} | {}
    """
legalMoves = True
def checkIfLegal(nm):
    if nm >= 9 or nm < 0: 
        return False
    else:
        return True
def playerTurn():
    movesMade = 1
    intField = int
    player = 1
    legal = True
    while(legal):
        if player == 1: 
            field = input("{}, chose number beetween 1-9:".format(player1Name))
            while True:
                try: 
                    intField = int(field)
                    break
                except ValueError:
                    field = input("{}, You must chose beetween 1-9: ".format(player1Name))
            
            print(intField)
            allGood = True
            while(allGood):
                while(intField <= 0 and intField > 9):
                    field = input("{}, you must chose number beetween 1-9: ".format(player1Name))
                if (intField > 0 and intField <= 9):
                    print("Here")
                    if player == 1:
                        while(grid[field] == "X" or grid[field] == "O"):
                            try:
                                field = input("{}, please chose another number beetween 1-9: that one is already used:".format(player1Name))
                                grid[field]
                            except:
                                field = input("{}, please chose another number beetween 1-9: that one is already used:".format(player1Name))
                    allGood = False
                else:
                    allGood = False

            grid[field] = "X"
            player = 2
            movesMade = movesMade + 1
            legal = checkIfLegal(movesMade)
            printoutGrid()
        
        if player == 2:
            field = input("{}, chose number beetween 1-9:".format(player2Name))
            while True:
                try: 
                    intField = int(field)
                    break
                except ValueError:
                    field = input("{}, You must chose beetween 1-9: ".format(player2Name))
            
            print(intField)
            allGood = True
            while(allGood):
                while(intField <= 0 and intField > 9):
                    field = input("{}, you must chose number beetween 1-9: ".format(player2Name))
                if (intField > 0 and intField <= 9):
                    print("Here")
                    if player == 2:
                        while(grid[field] == "O" or grid[field] == "X"):
                            try:
                                field = input("{}, please chose another number beetween 1-9: that one is already used:".format(player2Name))
                                grid[field]
                            except:
                                field = input("{}, please chose another number beetween 1-9: that one is already used:".format(player2Name))
                    allGood = False
                else:
                    allGood = False

            grid[field] = "O"
            player = 1
            movesMade = movesMade + 1
            legal = checkIfLegal(movesMade)
            printoutGrid()


    


print("WELCOME TO GAME OF TIC-TAC-TOE!")
print("\nTo play select number you wish to replace with your simbol!")

player1Name = ""
player2Name = ""

player1Name = input("Player 1 name:")
player2Name = input("Player 2 name:")

playerTurn()