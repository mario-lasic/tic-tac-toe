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

print("WELCOME TO GAME OF TIC-TAC-TOE!")
print("\nTo play select number you wish to replace with your simbol!")

print(gridString.format(*fields))