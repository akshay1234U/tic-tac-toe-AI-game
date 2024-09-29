import math


board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

def print_board(board):
    for row in board:
        print(row)
    print()

def check_winner(board):
 
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]
    
    for row in board:
        if '' in row:
            return None
    return 'Draw'


def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O': 
        return 1
    elif winner == 'X': 
        return -1
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ''
                    best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = 'O'


def play_game():
    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Winner: {winner}")
            break

        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter col (0, 1, 2): "))
        if board[row][col] == '':
            board[row][col] = 'X'
        else:
            print("Cell already taken, try again.")
            continue

       
        ai_move()


play_game()
