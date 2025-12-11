sumInvalid = 0

import re

def isValid(n):
	n = str(n)
	mid = len(n)//2
	if n[0:mid] != n[mid:]:
		return False
	return True

with open("./input_files/day2-input.txt") as file:
	idRanges = file.readline()
	idRanges = idRanges.split(',')
	
	for i in idRanges:
		i = i.split('-')
		for j in range(int(i[0]), int(i[1])+1):
			if re.fullmatch(r"(.+)\1+", str(j)):
				sumInvalid = sumInvalid + j

print("sum: ", sumInvalid)