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
player = 1
legalMoves = True

print("WELCOME TO GAME OF TIC-TAC-TOE!")
print("\nTo play select number you wish to replace with your simbol!")

player1Name = ""
player2Name = ""

player1Name = input("Player 1 name:")
player2Name = input("Player 2 name:")

while legalMoves:
    movesMade = 0
    if player == 1: 
        field = input("{}, chose number beetween 1-9:".format(player1Name))
        if int(field) > 0 and int(field) < 10:
            grid[field] = "X"
            player = 2
            movesMade +1
            printoutGrid()
        else:
            while True:
                field = input("{}, number must be beetween 1-9:".format(player1Name))
                if int(field) > 0 and int(field) < 10:
                    grid[field] = "X"
                    player = 2
                    movesMade +1
                    printoutGrid()
                    break
    break           
    
    
