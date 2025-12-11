from aocd import get_data
data = get_data(day=3, year=2025)

def findMaxComb(n):
	jolt = 0
	i = 0
	y = len(n[i:])-12
	
	while i < len(n) and len(str(jolt)) < 12:
		x = max(n[i:i+y])
		jolt = jolt * 10 + int(x)
		
		if n.index(x, i) != i:
			y = y - (n.index(x, i) - i)
			i = n.index(x, i) + 1
		else:
			i = i + 1
	return jolt
		
batteries = data.split('\n')
# with open("./input_files/day3-input.txt") as batteries:
sum = 0
for bank in batteries:
    sum = sum + (findMaxComb(bank))
	
print(sum)