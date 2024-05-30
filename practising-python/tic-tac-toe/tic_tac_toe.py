def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def is_board_full(board):
    return all(space in ['X', 'O'] for space in board)

def get_valid_move(board):
    while True:
        try:
            move = int(input("Choose your move (1-9): ")) - 1
            if move in range(9) and board[move] not in ['X', 'O']:
                return move
            else:
                print("This move is not valid. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def tic_tac_toe():
    board = [str(i+1) for i in range(9)]
    current_player = "X"

    while True:
        print_board(board)
        move = get_valid_move(board)
        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("The game is a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
