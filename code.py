import random  # Import the random module for generating random moves

def print_board(board):
    # Prints the current state of the Tic-Tac-Toe board.
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Checks if the specified player has won the game.
    # Returns True if the player has won, otherwise False.
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    # Returns a list of coordinates of empty cells on the board.
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(board, player):
    # Allows the player to make a move on the board.
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Cell already taken. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ai_move(board, player):
    # Generates a random move for the AI player.
    # Returns the coordinates of the chosen empty cell.
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_game():
    # Main function to run the Tic-Tac-Toe game.
    board = [[" "]*3 for _ in range(3)]  # Initialize an empty Tic-Tac-Toe board
    players = ['X', 'O']  # Define player symbols
    current_player = random.choice(players)  # Randomly select starting player
    
    print("Welcome to Tic-Tac-Toe!")  # Print welcome message
    print_board(board)  # Display initial board
    
    while True:
        if current_player == 'X':
            player_move(board, current_player)  # Player's turn
        else:
            row, col = ai_move(board, current_player)  # AI's turn
            board[row][col] = current_player

        print_board(board)  # Print updated board
        
        if check_winner(board, current_player):  # Check for winner
            print(f"Player {current_player} wins!")  # Print winner message
            break
        
        if all(board[i][j] != " " for i in range(3) for j in range(3)):  # Check for draw
            print("It's a draw!")  # Print draw message
            break
        
        current_player = 'O' if current_player == 'X' else 'X'  # Switch players

if __name__ == "__main__":
    play_game()  # Start the game


