import math

def part1(worksheet):
	# worksheet = [x.split() for x in worksheet]
	# for i in range(0, len(worksheet[:-1])):
	# 	for j in range(0, len(worksheet[i])):
	# 		worksheet[i][j] = int(worksheet[i][j])
	# print(worksheet)
	
	total = 0
	for i in range(0, len(worksheet[-1])):
		match worksheet[-1][i]:
			case '+':
				total += sum([j[i] for j in worksheet[:-1]])
			case '*':
				total += math.prod([j[i] for j in worksheet[:-1]])	
	print(total)

with open("./input_files/day6-input.txt") as file:
	worksheet = file.read().splitlines()
# part1(worksheet)

rotatedWorksheet = []
temp = []
for i in range(0, len(worksheet[1])):
	x = ([j[i] for j in worksheet[:-1]])
	x = ["".join(x).strip()]
	
	if x[0] != '':
		temp.append(int(x[0]))
	else:
		rotatedWorksheet.append(temp)
		temp = []
rotatedWorksheet.append(temp)
rotatedWorksheet.append(worksheet[-1].split())

total = 0
for i in range(0, len(rotatedWorksheet[:-1])):
	match rotatedWorksheet[-1][i]:
		case '+':
			total += sum(rotatedWorksheet[i])
		case '*':
			total += math.prod(rotatedWorksheet[i])
print(total)
