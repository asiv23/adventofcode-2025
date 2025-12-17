from aocd import get_data
data = get_data(day=9, year=2025)

testData = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''

def part1(redTiles):
	# floor = [['.' for i in range(max(redTiles[1])+2)] for j in range(max(redTiles[0])+2)]
	# for i in redTiles:
	# 	floor[i[1]][i[0]] = '#'
	# maxCorners = []
	
	maxArea = 0
	for i in range(len(redTiles)):
		for j in range(i, len(redTiles)):
			if findArea(redTiles[i], redTiles[j]) > maxArea:
				maxArea = findArea(redTiles[i], redTiles[j]) 
				 
	print(maxArea)

def drawSquare(grid, start, end):
	for i in range(start[1], end[1]+1):
		for j in range(start[0], end[0]+1): 
			grid[i][j] = '0'
	
	return grid

def findArea(start, end): 
	return (abs(end[0] - start[0])+1) * (abs(end[1] - start[1])+1)

redTiles = [[int(y) for y in x.split(',')] for x in testData.split('\n')]

# part1(redTiles)

# maxArea = 0
# for i in range(len(redTiles)):
# 	for j in range(i+1, len(redTiles)):
# 		if findArea(redTiles[i], redTiles[j]) > maxArea:	
# 			maxArea = findArea(redTiles[i], redTiles[j]) 
# 				# print(maxArea, i, j,)
				
# print(maxArea)