def dist(n, m):
	return(((n[0] - m[0]) ** 2 + (n[1] - m[1]) ** 2 + (n[2] - m[2]) ** 2) ** 0.5)

with open("./input_files/day8-input.txt") as file:
	boxes = [[int(i) for i in x.split(",")] for x in file.read().splitlines()]

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