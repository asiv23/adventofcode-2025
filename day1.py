click = 50
zeros = 0
with open("./input_files/day1-input.txt") as rotations:
	for i in rotations:
		x = (float(i[1:]))
		if x // 100 != 0.0:
			zeros = zeros + int(x // 100)
			x = x - 100 * (x // 100)
		if i[0] == 'L':
			x = x * - 1
			if click == 0:
				click = 100
		
		click = click + int(x)
		# print(i, click, x, zeros)

		if click > 99:
			click = click - 100
			zeros = zeros + 1
		elif click < 0:
			click = 100 + click 
			zeros = zeros + 1
		elif click == 0:
			zeros = zeros + 1

		# print(i, click, x, zeros)

print(zeros)