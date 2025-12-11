import re
from aocd import get_data
data = get_data(day=7, year=2025)

def part1():
	splitCount = 0
	grid[1] = grid[1][:grid[0].index('S')] + '|' + grid[1][grid[0].index('S')+1:]
	for i in range(2, len(grid)):
		
		for match in re.finditer("\|", grid[i-1]):
			index = match.start()
			if grid[i][index] == '^':
				grid[i] = grid[i][:index-1] + '|^|' + grid[i][index+2:]
				splitCount += 1
			else:
				grid[i] = grid[i][:index] + '|' + grid[i][index+1:]		
	print(splitCount)

grid = data.split('\n')
part1()