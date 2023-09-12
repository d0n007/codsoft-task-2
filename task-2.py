import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, maximizing_player):
    if is_winner(board, "O"):
        return 1
    if is_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_move = None
    best_eval = float("-inf")
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                eval = minimax(board, 0, False)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        user_row = int(input("Enter row (0, 1, or 2): "))
        user_col = int(input("Enter column (0, 1, or 2): "))
        
        if board[user_row][user_col] == " ":
            board[user_row][user_col] = "X"
        else:
            print("Invalid move. Try again.")
            continue
        
        print_board(board)
        
        if is_winner(board, "X"):
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break
        
        print("AI's turn:")
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = "O"
        print_board(board)
        
        if is_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
