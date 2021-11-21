import random
ROWS = 5
COLS = 5
def make_board():
    return [['' for _ in range(5)] for _ in range(5)]

def print_board(board):
    print(board[0][0], "|", board[0][1], board[0][2], sep = '')
    print(board[1][0], "|", board[1][1], board[1][2], sep = '')
    print(board[2][0], "|", board[2][1], board[2][2], sep = '')
    print(board[3][0], "|", board[3][1], board[3][2], sep = '')
    print(board[4][0], "|", board[4][1], board[4][2], sep = '')

def two_or_four(num):
    if num <= 70:
        return 2
    else:
        return 4
def up(board):
    for row in ROWS:
        for col in COLS:
            old = board[row][col]
            new = board[row-1][col]
    print("Old board: ", old)
    print("New Board: ", new)

def down(board):
    for row in ROWS:
        for col in COLS:
            old = board[row][col]
            new = board[row+1][col]
    print("Old board: ", old)
    print("New Board: ", new)
def left(board):
    for row in ROWS:
        for col in COLS:
            old = board[row][col]
            new = board[row-1][col-1]
    print("Old board: ", old)
    print("New Board: ", new)

def right(board):
    for row in ROWS:
        for col in COLS:
            old = board[row][col]
            new = board[row+1][col+1]
    print("Old board: ", old)
    print("New Board: ", new)
    
def spawn(board, row, col):
    #table[ROWS][COLS]
    move = input('Enter move (row column [range of 1-5]): ')
    tokens = move.split()
    move1 = input('Enter  another move (row column [range of 1-5]): ')
    tokens = move.split()
    tokens1 = move1.split()
    row = int(tokens[0])
    col = int(tokens[1])
    row1 = int(tokens1[0])
    col1 = int(tokens1[1])
    random_number = random.randint(1,100)
    if board[row][col] == '' and board[row1][col1] == '':
            board[row][col] = two_or_four(random_number)
            board[row1][col1] = two_or_four(random_number)
    if row > 5 or row1 > 5 or col > 5 or col1 > 5:
        print("out of range")
        no_move = False
    if board[row][col] != '' or board[row1][col1] != '':
        addition = board[row][col] + board[row1][col1]
        board[row1][col1] = int(addition)
    else:
        return spawn(random_number, board)
    print_board(board)


def main():
    print("Welcome to our wonderful game!!!")
main()