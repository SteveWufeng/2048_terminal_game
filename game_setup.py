import random
ROWS = 5
COLS = 5

def make_board():
    x = [['' for _ in range(5)] for _ in range(5)]
    print(x)
    return [['' for _ in range(5)] for _ in range(5)]

def print_board(board):
    print(board[0][0], "|", board[0][1], "|", board[0][2],"|", board[0][3], "|", board[0][4], sep = '')
    print(board[1][0], "|", board[1][1], "|", board[1][2], "|", board[1][3], "|",board[1][4], sep = '')
    print(board[2][0], "|", board[2][1], "|", board[2][2], "|", board[2][3], "|",board[2][4], sep = '')
    print(board[3][0], "|", board[3][1], "|", board[3][2], "|", board[3][3], "|",board[3][4], sep = '')
    print(board[4][0], "|", board[4][1], "|", board[4][2], "|", board[4][3], "|",board[4][4], sep = '')

def two_or_four(num):
    if num <= 70:
        return 2
    else:
        return 4
def up(board):
    #for row in ROWS:
        #for col in COLS:
    for row,col in board:
        old = board[row][col]
        #print(old)
        new = board[row-1][col]
        print(new)
        alter = board[row+1][col]
    #for i in COLS:
        if new == alter:
            merge = new + alter
            new = merge
            alter = 0
        else:
            continue
    print("Old board: ", old)
    print("New Board: ", new)

def down(board):
    for row,col in board:
        old = board[row][col]
        #print(old)
        new = board[row+1][col]
        print(new)
        alter = board[row-1][col]
    #for i in COLS:
        if new == alter:
            merge = new + alter
            new = merge
            alter = 0
        else:
            continue
    print("Old board: ", old)
    print("New Board: ", new)

def left(board):
    for row,col in board:
        old = board[row][col]
        #print(old)
        new = board[row][col-1]
        print(new)
        alter = board[row][col+1]
    #for i in COLS:
        if new == alter:
            merge = new + alter
            new = merge
            alter = 0
        else:
            continue
    print("Old board: ", old)
    print("New Board: ", new)

def right(board):
    for row,col in board:
        old = board[row][col]
        #print(old)
        new = board[row][col+1]
        print(new)
    #for i in COLS:
        alter = board[row][col-1]
        if new == alter:
            merge = new + alter
            new = merge
            alter = 0
        else:
            continue
    print("Old board: ", old)
    print("New Board: ", new)
    
def spawn(board):
    #table[ROWS][COLS]
    #move = input('Enter move (row column [range of 1-5]): ')
    row = random.randint(0,5)
    col = random.randint(0,5)
    #move = row,col
    #tokens = move.split()
    #move1 = input('Enter  another move (row column [range of 1-5]): ')
    #tokens1 = move1.split()
    #row = int(tokens[0])
    print("row:", row)
    #col = int(tokens[1])
    print("col:", col)
    #row1 = int(tokens1[0])
    #col1 = int(tokens1[1])
    random_number = random.randint(1,100)
    if board[row][col] == '': #and board[row1][col1] == '':
        board[row][col] = two_or_four(random_number)
        #board[row1][col1] = two_or_four(random_number)
    if row > 5 or col > 5: #or row1 > 5 or col1 > 5:
        print("out of range")
        no_move = False
    merge(board)
    print(board)
    return spawn(random_number, board)
    
    #print_board(board)
def merge(board):
    move = input("Enter a command: ")
    if move == 'w'or move == 'W':
        up(board)
    if move == 'a'or move == 'A':
        left(board)
    if move == 's'or move == 'S':
        down(board)
    if move == 'd'or move == 'D':
        right(board)

def main():
    print("Welcome to our wonderful game!!!")
    board = make_board
    print_board(board)
    spawn(board)
main()