from aocd import get_data
data = get_data(day=8, year=2025)

testData = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''

def dist(n, m):
	return(((n[0] - m[0]) ** 2 + (n[1] - m[1]) ** 2 + (n[2] - m[2]) ** 2) ** 0.5)

def findDist(boxes):
	distances = []
	for i in range(0, len(boxes)):
		for j in range(i+1, len(boxes)):
			distances.append(tuple([dist(boxes[i], boxes[j]), i, j]))
	distances.sort(key=lambda x: x[0])
	return(distances)

def findDupes(graph):
	dupes = True
	while dupes:
		dupes = False
		for i in range(len(graph)):
			for j in range(i+1, len(graph)):
				# print(graph)
				if len(graph[i].intersection(graph[j])) > 0:
					graph[i].update(graph[j])
					del graph[j]
					dupes = True
					break
	return(graph)

def part1(distances):
	graph = [set(distances[0][1:])]
	for i in range(1, 1000):
		found = False
		for j in range(0, len(graph)):
			if len(graph[j].intersection(distances[i])) > 0:
				graph[j].add(distances[i][1])
				graph[j].add(distances[i][2])
				found = True
				break
		if not found:
			graph.append(set(distances[i][1:]))

	graph = (findDupes(graph))
	graph.sort(key=len, reverse=True)
	print(len(graph[0])*len(graph[1])*len(graph[2])) 

input = [[int(i) for i in x.split(",")] for x in data.split('\n')]
distances = findDist(input)
# part1(distances)

graph = [set(distances[0][1:])]
for i in range(1, len(distances)):
	found = False
	for j in range(0, len(graph)):
		if len(graph[j].intersection(distances[i])) > 0:
		# if distances[i][1] in graph[j] or distances[i][2] in graph[j]:
			graph[j].add(distances[i][1])
			graph[j].add(distances[i][2])
			found = True
			break
	if not found:
		graph.append(set(distances[i][1:]))
	graph = findDupes(graph)
	if len(graph[0]) == len(input):
		y = (list(distances[i]))
		print(input[y[1]][0] * input[y[2]][0])
		break