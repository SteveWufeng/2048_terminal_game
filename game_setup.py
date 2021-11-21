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

def make_move(board, symbol):
    no_move = True
    while no_move:
        try:
            move = input('Enter move (row column [range of 1-5]): ')
            tokens = move.split()
            move1 = input('Enter  another move (row column [range of 1-5]): ')
            tokens = move.split()
            tokens1 = move1.split()
            row = int(tokens[0])
            col = int(tokens[1])
            row1 = int(tokens1[0])
            col1 = int(tokens1[1])
            if row > 5 or row1 > 5:
                print("out of range")
            if col > 5 or col1 > 5:
                print("out of range")
            if board[row][col] == '':
                board[row][col] = symbol
                no_move = False
            elif board[row][col] != 
            else:
                print('Invalid move. Please try again')
        except:
            print("invalid move. Please try again.")
    print_board(board)
def table():
    print("Hello World!")
    
def two_or_four(num):
    if num <= 70:
        return 2
    else:
        return 4

def spawn(random_number,board, moves):
    #table[ROWS][COLS]
    count = 0
    for x in moves:
        random_number = random.randint(1,100)
        if board[ROWS][COLS] == '':
            board[ROWS][COLS] = two_or_four(random_number)
        else:
            spawn()
        if count == x:
            print("Game over!")
            break
def get_score(score, moves):
    score = 0
    for i in range(moves):
        table()

def main():
    print("Welcome to our wonderful game!!!")
main()