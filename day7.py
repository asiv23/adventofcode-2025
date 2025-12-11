import re

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

with open("./input_files/day7-input.txt") as file:
	grid = file.read().splitlines()

# [print(x) for x in grid] 