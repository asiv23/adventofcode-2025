import re
from aocd import get_data
data = get_data(day=2, year=2025)

sumInvalid = 0

def isValid(n):
	n = str(n)
	mid = len(n)//2
	if n[0:mid] != n[mid:]:
		return False
	return True

idRanges = data.split(',')
# [print(x) for x in idRanges]
for i in idRanges:
	i = i.split('-')
	for j in range(int(i[0]), int(i[1])+1):
		if re.fullmatch(r"(.+)\1+", str(j)):
			sumInvalid = sumInvalid + j

print("sum: ", sumInvalid)