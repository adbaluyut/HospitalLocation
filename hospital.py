

# rows = int(input("Input number of rows:\n"))
# columns = int(input("Input number of columns:\n"))
# numHouses = int(input("Input number of houses:\n"))
rows = 5 # y on the board
columns = 10 # x on the board
numHouses = 4
home = '\u25A2'
hospital = 'H'

def main():
	board = initBoard(rows,columns)    
	# initial locations for hospitals
	insertLocation(0,4,board,hospital) # H for hospitals
	insertLocation(3,9,board,hospital)
	insertLocation(1,2,board,home) # square for homes
	insertLocation(3,1,board,home)
	insertLocation(0,8,board,home)
	insertLocation(4,6,board,home)
	drawBoard(rows, columns, board)
	hcrr(rows,columns,board,3)

def initBoard(rows,columns):
	board = []
	for i in range(rows): 
		board.append([])
		for j in range(columns):
			board[i].append('o')
	return board

def insertLocation(r,c,b,location):
	b[r][c] = location

def drawBoard(r,c,b):
	for i in range(r):
		for j in range(c):
			print(f'{b[i][j]}', end=' ')
		print()
	print()

def manhattan(state):
	homeLoc = findIndex(rows,columns,hospital,state)
	total = 0
	return total
	 
# return a list of tuples containing the coordinates of the targets
def findIndex(r, c, target, state):
	hCoord = []
	for i in range(r):
		for j in range(c):
			if target == state[i][j]:
				hCoord.append((i,j))
	return hCoord

def up(r, c, board):
		# copy the state
		arr = []
		for li in board:
			arr.append(list(li))

		print(r)
		if r > 0:
			arr[r][c], arr[r-1][c] = arr[r-1][c], arr[r][c]
			return arr

def down(r, c, board):
		# copy the state
		arr = []
		for li in board:
			arr.append(list(li))
			
		print(r)
		if r < rows-1:
			arr[r][c], arr[r+1][c] = arr[r+1][c], arr[r][c]
			return arr

def left(r, c, board):
		# copy the state
		arr = []
		for li in board:
			arr.append(list(li))
			
		print(c)
		if c > 0:
			arr[r][c], arr[r][c-1] = arr[r][c-1], arr[r][c]
			return arr

def right(r, c, board):
		# copy the state
		arr = []
		for li in board:
			arr.append(list(li))
			
		print(c)
		if c < columns-1:
			arr[r][c], arr[r][c+1] = arr[r][c+1], arr[r][c]
			return arr

def possibleStates(board):
	nextStates = []
	hospitalLoc = findIndex(rows,columns,hospital,board)
	print(hospitalLoc)
	# At each hospital location get the next possible moves
	for r,c in hospitalLoc:
		print(f"{board[r][c]} at ({r},{c})")
		nextStates.append(up(r,c,board))
		nextStates.append(down(r,c,board))
		nextStates.append(left(r,c,board))
		nextStates.append(right(r,c,board))
	# filter out the Nones and return the list
	return [i for i in nextStates if i]

# Hill CLimbing with Random Restart
def hcrr(rows,columns,board,numRestart):
	# copy the state
	current = []
	for li in board:
		current.append(list(li))
	restart = 0

	nextStates = possibleStates(board)
	for li in nextStates:
		drawBoard(rows,columns,li)

	

if __name__ == "__main__":
	main()