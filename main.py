import random

def play():
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    move = random.choice(["Player", "Computer"])
    print(f"Let's play! The {move} starts. Player's move will be marked with 'P', computer's move will be marked with 'C'")
    
    while check_matrix(matrix) == "None":
        make_a_move(move, matrix)
        print_matrix(matrix)
        if move == "Player":
            move = "Computer"
        else:
            move = "Player"

    winner = check_matrix(matrix)

    if winner == "P":
        print("You won!")
    if winner == "C":
        print("The computer wins.")
    if winner == "Tie":
        print("There has been a tie.")

def print_matrix(matrix):
    for row in range(3):
        for column in range(3):
            if column != 2:
                print(f"{matrix[row][column]} | ", end = " ")
            else:
                print(f"{matrix[row][column]} ", end = " ")
        print("\n")

def check_matrix(matrix):
    same = 0

    # Checks rows
    for row in range(3):
        symbol = matrix[row][0]
        for column in range(3):
            if matrix[row][column] == symbol and matrix[row][column] != 0:
                 same = same + 1
            else:
                 same = 0
                 break
            
            if same == 3:
                 return symbol
            
    # Checks columns
    for column in range(3):
         symbol = matrix[0][column]
         for row in range(3):
              if matrix[row][column] == symbol and matrix[row][column] != 0:
                   same = same + 1
              else:
                   same = 0
                   break
              
              if same == 3:
                   return symbol
              
    # Check diagonals
    symbol = matrix[0][0]
    if matrix[0][0] == symbol and matrix[1][1] == symbol and matrix[2][2] == symbol and symbol != 0:
         return symbol
    
    symbol = matrix[0][2]
    if matrix[0][2] == symbol and matrix [1][1] == symbol and matrix[2][0] == symbol and symbol != 0:
         return symbol
    
    # Checks if there are any available moves
    for row in range(3):
         for column in range(3):
              if matrix[row][column] == 0:
                   return "None"
              
    return "Tie"
              
def make_a_move(move, matrix):
    if move == "Player":
        player_picks(matrix)
    if move == "Computer":
        computer_picks(matrix)

def player_picks(matrix):
    #while True:
        row = pick_row()
        column = pick_column()

        if matrix[row - 1][column - 1] == 0:
            matrix[row - 1][column - 1] = "P"
            print(f"You chose row {row}, column {column}.")
        else:
            print("You chose a spot that is already picked! Pick again.")
            player_picks(matrix)

def pick_row():
    #while True:
        row = input("Your turn! Please enter selected row: ")
        if row.isnumeric():
            row = int(row)
            if 1 <= row <= 3:
                return row
            else:
                print("Please enter a valid row (1-3)") 
                pick_row()
        else:
            print("Please enter a valid number")
            pick_row()

def pick_column():
    #while True:
        column = input("Your turn! Please enter selected column: ")
        if column.isnumeric():
            column = int(column)
            if 1 <= column <= 3:
                return column
            else:
                print("Please enter a valid column (1-3)") 
                pick_row()
        else:
            print("Please enter a valid number")
            pick_column()

# Ai tries to pick spots that are near its already picked spots, tries to block the opponent if it has connected 2 spots, tries to connect the computer's 3rd spot if 2 are already connected
def computer_picks(matrix):
    first = finish_or_block(matrix, "C")
    second = finish_or_block(matrix, "P")

    if first == None and second == None:
        row = random.choice([1, 2, 3])
        column = random.choice([1, 2, 3])

        if matrix[row - 1][column - 1] == 0:
            matrix[row - 1][column - 1] = "C"
            print(f"Computer's turn. It picked row {row}, column {column}.")
        else:
            computer_picks(matrix)

def finish_or_block(matrix, symbol):
    # Checks rows
    for row in range(3):
         same = 0
         for column in range(3):
              if matrix[row][column] == symbol:
                   same = same + 1

         if same == 2:
              for column in range(3):
                   if matrix[row][column] == 0:
                        matrix[row][column] = "C"
                        print(f"Computer's turn. It picked row {row + 1}, column {column + 1}.")
                        return True
         
    # Check columns
    for column in range(3):
         same = 0
         for row in range(3):
              if matrix[row][column] == symbol:
                   same = same + 1

         if same == 2:
              for row in range(3):
                   if matrix[row][column] == 0:
                        matrix[row][column] = "C"
                        print(f"Computer's turn. It picked row {row + 1}, column {column + 1}.")
                        return True

    # Check diagonals
    if matrix[0][0] == symbol and matrix[1][1] == symbol or matrix[0][0] == symbol and matrix[2][2] == symbol or matrix[1][1] == symbol and matrix[2][2] == symbol:
         if matrix[0][0] == 0:
              matrix[0][0] = "C"
              print("Computer's turn. It picked row 1, column 1.")
         if matrix[1][1] == 0:
              matrix[1][1] = "C"
              print("Computer's turn. It picked row 2, column 2.")
         if matrix[2][2] == 0:
              matrix[2][2] = "C"
              print("Computer's turn. It picked row 3, column 3.")
         return True

    if matrix[0][2] == symbol and matrix[1][1] == symbol or matrix[0][2] == symbol and matrix[2][0] == symbol or matrix[1][1] == symbol and matrix[2][0] == symbol:
         if matrix[0][2] == 0:
              matrix[0][2] = "C"
              print("Computer's turn. It picked row 1, column 3.")
         if matrix[1][1] == 0:
              matrix[1][1] = "C"
              print("Computer's turn. It picked row 2, column 2.")
         if matrix[2][0] == 0:
              matrix[2][0] = "C"
              print("Computer's turn. It picked row 3, column 1.")
         return True

play()