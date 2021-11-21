import random
ROWS = 5
COLS = 5
random_number = random.randint(1,100)
def make_board():
    return [['' for _ in range(5)] for _ in range(5)]

def print_board(board):
    print(board[0][0], "|", board[0][1], board[0][2], sep = '')
    print(board[1][0], "|", board[1][1], board[1][2], sep = '')
    print(board[2][0], "|", board[2][1], board[2][2], sep = '')
    print(board[3][0], "|", board[3][1], board[3][2], sep = '')
    print(board[4][0], "|", board[4][1], board[4][2], sep = '')

def make_move(board, symbol):
    no_move = True
    while no_move:
        try:
            move = input('Enter move (row column): ')
            tokens = move.split()
            row = int(tokens[0])
            col = int(tokens[1])

            if board[row][col] == '':
                board[row][col] = symbol
                no_move = False
            else:
                print('Invalid move. Please try again')
        except:
            print("invalid move. Please try again.")
    print_board(board)
def table():
    print("Hello World!")
    
def spawn(random_number):
    table[ROWS][COLS]
    if random_number < 70:
        return 2
    else:
        return 4