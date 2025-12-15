import re
from aocd import get_data
data = get_data(day=7, year=2025)

dataTest = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''

def part1(grid): #silly goofy method
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
	
grid = [x for x in data.split('\n')]
part1(grid)
grid = [[y for y in x] for x in grid]

start = grid[0].index('S')
beams = [0] * len(grid[0])
beams[start] = 1
for i in range(len(grid)):
	for j in range(1, len(grid[i])):
		if grid[i][j] == '^' and grid[i-1][j] == '|':
			beams[j+1] += beams[j]
			beams[j-1] += beams[j]
			beams[j] = 0 

print(sum(beams))