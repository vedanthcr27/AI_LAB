def my_board(board):
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--|---|--")
    print()

def checkwin(board, player):
    if board[0] == board[1] == board[2] == player: return True
    if board[3] == board[4] == board[5] == player: return True
    if board[6] == board[7] == board[8] == player: return True

    if board[0] == board[3] == board[6] == player: return True
    if board[1] == board[4] == board[7] == player: return True
    if board[2] == board[5] == board[8] == player: return True

    if board[0] == board[4] == board[8] == player: return True
    if board[2] == board[4] == board[6] == player: return True

    return False

def tic_tac_toe():
    board = [0] * 9
    player = 1
    while True:
        my_board(board)
        move = int(input(f"Player {player} choose from 1 to 9: ")) - 1

        if board[move] != 0:
            print("The spot is taken,try again")
            continue

        board[move] = player

        if checkwin(board, player):
            my_board(board)
            print(f" Player {player} wins!")
            break
        if 0 not in board:
            my_board(board)
            print("Draw!")
            break
        player = 2 if player == 1 else 1
tic_tac_toe()
