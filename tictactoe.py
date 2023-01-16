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

fields = []
for x in grid.values():
    fields.append(x)
legalMoves = True

print("WELCOME TO GAME OF TIC-TAC-TOE!")
print("\nTo play select number you wish to replace with your simbol!")

print(gridString.format(*fields))

player1Name = ""
player2Name = ""

player1Name = input("Player 1 name:")
player2Name = input("Player 2 name:")

while legalMoves:
    movesMade = 0
    i = 1
    if i == 1: 
        field = input("{}, chose number beetween 1-9:".format(player1Name))
        if int(field) > 0 and int(field) < 10:
            grid[field] = "X"
            i = 2
            movesMade +1
        else:
            while True:
                field = input("{}, number must be beetween 1-9:".format(player1Name))
                if int(field) > 0 and int(field) < 10:
                    grid[field] = "X"
                    i = 2
                    movesMade +1
                    break
    print(i)
    break           
    
