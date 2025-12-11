def part1():
	freshCount = 0
	for i in ingredients:
		if inRange(i):
			freshCount += 1
	print(freshCount)

def inRange(i):
	for r in freshRanges:
		if r[0] < i <= r[1]:
			return True	

with open("./input_files/day5-input.txt") as file:
	data = [x.strip() for x in file.read().split('\n\n')]
	freshRanges = [[int(x.split('-')[0]), int(x.split('-')[1])] for x in data[0].splitlines()]
	ingredients = [int(x) for x in data[1].splitlines()]

freshRanges.sort(key=lambda x: x[0])
newRanges = [[freshRanges[0][0], freshRanges[0][1]]]
for i in range(1, len(freshRanges)):
	overlap = False
	for j in range(i, len(newRanges)):
		if newRanges[j][0] <= freshRanges[i][0] <= newRanges[j][1]:
			newRanges[j][1] = max(freshRanges[i][1], newRanges[j][1])
			overlap = True
	if overlap == False:
		newRanges.append(freshRanges[i])
print(newRanges)

count = 0 
for i in newRanges:
	count += i[1] - i[0] + 1
print(count)