from aocd import get_data
data = get_data(day=4, year=2025)
    
directions = [
	[0, 1],
	[0, -1],
	[1, 0],
	[1, 1],
	[1, -1],
	[-1, 0],
	[-1, 1],
	[-1, -1],
]

accessable = 0
removable = True

grid = [line for line in data.split('\n')] 
while removable == True:
	removable = False
	for i in range(0, len(grid)):
		for j in range(0, len(grid[i])):
			adjacent = 0
			if grid[i][j] == '@':
				for d in directions:
					if 0 <= i+d[0] < len(grid) and 0 <= j+d[1] < len(grid[i]):
						adjacent = adjacent + 1 if grid[i+d[0]][j+d[1]] == '@' else adjacent
				if adjacent < 4:
					grid[i] = grid[i][:j] + 'x' + grid[i][j+1:]
					accessable = accessable + 1
					removable = True
		# print('\n')

print(accessable)