
import copy
import math
import random


# rows = int(input("Input number of rows:\n"))
# columns = int(input("Input number of columns:\n"))
# numHouses = int(input("Input number of houses:\n"))
rows = 100
columns = 100
numHouses = 2000
home = '\u25A2'
hospital = 'H'

def main():
    board = initBoard()    
    runs = 1
    # randomly insert homes and hospitals
    insertHomes(board) # squares = home
    insertHospitals(board) # H = hospitals
    while runs <= 4:
        print(f"------------------------------------------------------------\nRunning test {runs}")
        hcrrboard = copy.deepcopy(board)
        saboard = copy.deepcopy(board)

        print("Starting Hill CLimbing with Random Restart\n")
        # drawBoard(board)
        print(f"The initial manhattan distance is {manhattan(hcrrboard)}\n")
        hcrrboard = hcrr(rows,columns,board)
        # drawBoard(board[0])
        print(f"The final manhattan distance is {hcrrboard[1]}\n")

        print("Starting Simulated Annealing\n")
        # drawBoard(saboard)
        # print(f"The initial manhattan distance is {manhattan(saboard)}\n")
        solution = sa(saboard)
        # drawBoard(solution[0])
        print(f"The final manhattan distance is {solution[1]}\n")
        runs += 1

def initBoard():
    board = []
    for i in range(rows): 
        board.append([])
        for j in range(columns):
            board[i].append('o')
    return board

# randomly insert 2 hospitals in the board
def insertHospitals(board):
    count = 0

    while count < 2:
        
        r = random.randint(0,rows - 1)
        c = random.randint(0,columns - 1)
        
        if board [r][c] == 'o':
            insertLocation(r,c,board,hospital)
            count += 1

def removeHospitals(board):    
    for i in range(rows): 			
        for j in range(columns):
            if board [i][j] == hospital:
                insertLocation(i,j,board,'o')

def insertHomes(board):
    homes = 0
    while homes < numHouses:
        r = random.randint(0,rows - 1)
        c = random.randint(0,columns - 1)
        if board [r][c] == 'o':
            insertLocation(r,c,board,home)
            homes+=1

def insertLocation(r,c,b,location):
    b[r][c] = location

def drawBoard(b):
    for i in range(rows):
        for j in range(columns):
            print(f'{b[i][j]}', end=' ')
        print()
    print()

def manhattan(state):
    distances = []
    homeLoc = findIndex(rows,columns,home,state)
    hospitalLoc = findIndex(rows,columns,hospital,state)
    
    for r,c in homeLoc:
        localDist = math.inf

        for y,x in hospitalLoc:
            dist = abs(r - y) + abs(c - x)
            if dist < localDist:
                localDist = dist

        distances.append(localDist)

    return sum(distances)
     
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

    if r > 0:

        if arr[r-1][c] == home or arr[r-1][c] ==hospital:
            return None

        arr[r][c], arr[r-1][c] = arr[r-1][c], arr[r][c]

        return arr

def down(r, c, board):
    # copy the state
    arr = []
    for li in board:
        arr.append(list(li))

    if r < rows-1:

        if arr[r+1][c] == home or arr[r+1][c] == hospital:
            return None

        arr[r][c], arr[r+1][c] = arr[r+1][c], arr[r][c]

        return arr

def left(r, c, board):
    # copy the state
    arr = []
    for li in board:
        arr.append(list(li))
        
    if c > 0:

        if arr[r][c-1] == home or arr[r][c-1] == hospital:
            return None

        arr[r][c], arr[r][c-1] = arr[r][c-1], arr[r][c]

        return arr

def right(r, c, board):
    # copy the state
    arr = []
    for li in board:
        arr.append(list(li))
        
    if c < columns-1:

        if arr[r][c+1] == home or arr[r][c+1] == hospital:
            return None

        arr[r][c], arr[r][c+1] = arr[r][c+1], arr[r][c]

        return arr

# Find the possible next states and return a list of those states
def possibleStates(board):
    nextStates = []
    hospitalLoc = findIndex(rows,columns,hospital,board)
    # At each hospital location get the next possible moves
    for r,c in hospitalLoc:
        nextStates.append(up(r,c,board))
        nextStates.append(down(r,c,board))
        nextStates.append(left(r,c,board))
        nextStates.append(right(r,c,board))
    # filter out the Nones and return the list
    nextStates = [i for i in nextStates if i]
    states = []

    for li in nextStates:
        states.append((li, manhattan(li)))

    return states

# Hill CLimbing with Random Restart
def hcrr(rows,columns,board): 
    statesEvaluated = 0
    localMin = []
    currentMin = math.inf
    cmin = ([],math.inf)
    restart = 0
    count = 1
    # copy the state
    current = []
    for li in board:
        current.append(list(li))

    while(restart < 10):
        nextStates = possibleStates(current)
        statesEvaluated += len(nextStates)
        # uncomment to see the next states being computed
        # for li in nextStates:
        # 	drawBoard(li[0])

        nextStates.sort(key=lambda x:x[1])
        
        # the first state in the sorted list is the new current
        current = nextStates[0][0]

        if nextStates[0][1] < currentMin:
            currentMin = nextStates[0][1]
            cmin = nextStates[0]
        else:
            localMin.append(cmin)
            restart += 1
            # generate new location for hospitals
            removeHospitals(current)
            insertHospitals(current)

    localMin.sort(key=lambda x:x[1])

    print(f"The number of configurations evaluated: {statesEvaluated}")
    
    return localMin[0]

def sa(board):
    statesEvaluated = 0
    initTemp = 100
    finalTemp = 0.1
    alpha = .01

    curTemp = initTemp

    curState = []
    for li in board:
        curState.append(list(li))
    
    curState = (curState, manhattan(curState))
    solution = curState

    while curTemp >= finalTemp:
        nextState = random.choice(possibleStates(curState[0]))
        
        # uncomment to see the algorithm in action
        # drawBoard(nextState[0])
        # print(f"Manhattan Distance: {nextState[1]}")
        # print(f"Current T: {curTemp}")

        diffCost = curState[1] - nextState[1]
        statesEvaluated += 1

        if diffCost > 0:
            solution = nextState
        elif random.uniform(0,1) < math.exp(diffCost/curTemp):
            solution = nextState
        
        curTemp -= alpha
    
    # print(f"The number of configurations evaluated: {statesEvaluated}")
        
    return solution
    

if __name__ == "__main__":
    main()