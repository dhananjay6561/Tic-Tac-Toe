def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, sign):
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == sign:
            return True
    return False

def check_draw(board):
    for cell in board:
        if cell not in ['X', 'O']:
            return False
    return True

def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'
    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")
        if not move.isdigit() or int(move) < 1 or int(move) > 9 or board[int(move) - 1] in ['X', 'O']:
            print("Invalid move. Try again.")
            continue
        board[int(move) - 1] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        else:
            current_player = 'O' if current_player == 'X' else 'X'

tic_tac_toe()