
def printBoard(board):
	for row in board:
		for c in row:
			print(c, end = " ")
		print()

def getZeroPositions(board):
	posList = []
	for r in range(len(board)):
		for c in range(len(board[r])):
			if not board[r][c]:
				posList.append((r, c))
	return posList

def getSquarePossibilites(board, pos):
	startx = 6 if pos[0] > 5 else 3 if pos[0] > 2 else 0
	starty = 6 if pos[1] > 5 else 3 if pos[1] > 2 else 0
	res = []
	for r in range(3):
		for c in range(3):
			n = board[startx + r][starty + c]
			if n:
				res.append(n)
	return res

def solveBoard(board, zeroPosList):
	if not zeroPosList:
		printBoard(board)
		return
	for pos in zeroPosList:
		r, c = pos[0], pos[1]
		row = board[r]
		col = [row[c] for row in board]
		nums = range(1, 10)
		nums = list(filter(lambda x: (x not in row) and (x not in col) and (x not in getSquarePossibilites(board, pos)), nums))
		if len(nums) == 1:
			board[r][c] = nums[0]
			zeroPosList.remove(pos)
			break
	solveBoard(board, zeroPosList)

def initBoard():
	file = open("board.txt", "r")
	board = []
	for line in file:
		l = line.strip()
		row = [int(x) for x in l.split(" ")]
		board.append(row)
	return board

board = initBoard()
solveBoard(board, getZeroPositions(board))
