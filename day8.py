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

# boxes = [[int(i) for i in x.split(",")] for x in data.split('\n')]
boxes = [[int(i) for i in x.split(",")] for x in testData.split('\n')]

distances = []
for i in range(0, len(boxes)):
	for j in range(i+1, len(boxes)):
		distances.append([dist(boxes[i], boxes[j]), i, j])
distances.sort(key=lambda x: x[0])
# distances = distances[0:10]
# print(distances)


graph = [distances[0][1:]]
for i in distances[1:11]:
	# print("test", graph)
	contains = False
	for j in range(0, len(graph)):
		if i[1] in graph[j] and i[2] not in graph[j]:
			graph[j].append(i[2])
			contains = True
		elif i[2] in graph[j] and [1] not in graph[j]:
			graph[j].append(i[1])
			contains = True
	if contains == False:
		graph.append(i[1:])

graph.sort(key=len, reverse=True)
[print(x) for x in graph]