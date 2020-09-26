
def main():
    # rows = int(input("Input number of rows:\n"))
    # columns = int(input("Input number of columns:\n"))
    rows = 5
    columns = 10
    home = '\u25A2'
    hospital = 'H'
    board = initBoard(rows,columns)    
    insertLocation(0,4,board,hospital) # H for hospitals
    insertLocation(3,9,board,hospital)
    insertLocation(1,2,board,home) # square for homes
    insertLocation(3,1,board,home)
    insertLocation(0,8,board,home)
    insertLocation(4,6,board,home)
    drawBoard(rows, columns, board)

def initBoard(rows,columns):
    board = []
    for i in range(rows):
        board.append([])
    for i in range(rows): 
        for j in range(columns):
            board[i].append('o')
    return board

def insertLocation(x,y,b,location):
    b[x][y] = location

def drawBoard(x,y,b):
    for i in range(x):
        for j in range(y):
            print(f'{b[i][j]}', end=' ')
        print()

    print()

if __name__ == "__main__":
    main()