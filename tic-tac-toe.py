# Simple 2-player Tic-Tac-Toe game in Python (console version)

def print_board(board):
    # Display the current state of the board
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    # If there are no empty spaces, it's a draw
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}, choose your move (row and column):")

        try:
            row = int(input("Row (0, 1, 2): "))
            col = int(input("Column (0, 1, 2): "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid move. Try again.")
            continue

        if board[row][col] != " ":
            print("Cell already taken. Try another.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()