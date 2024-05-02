import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
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
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(board, player):
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
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_game():
    board = [[" "]*3 for _ in range(3)]
    players = ['X', 'O']
    current_player = random.choice(players)
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        if current_player == 'X':
            player_move(board, current_player)
        else:
            row, col = ai_move(board, current_player)
            board[row][col] = current_player

        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()

