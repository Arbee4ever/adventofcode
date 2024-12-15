import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)
out = 0
visited = {}

def from_coords(coords):
	if coords[0] in range(len(arr[0])) and coords[1] in range(len(arr)):
		return arr[coords[1]][coords[0]]
	return ""

def to_coords(index):
	return [int(index % len(arr[0])), int(index / len(arr[0]))]

def check_cell(coords, char):
	val = {"area": 0, "perimeter": 0}
	if coords in visited[char]:
		return val
	if not from_coords(coords) == char:
		val["perimeter"] += 1
		return val
	print("coords", str(coords))
	visited[char].append(coords)
	val["area"] += 1
	for diff in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
			next = check_cell([coords[0] + diff[0], coords[1] + diff[1]], char)
			val["area"] += next["area"]
			val["perimeter"] += next["perimeter"]

	return val

for i in range(len(string.replace("\n", ""))):
	coords = to_coords(i)
	char = from_coords(coords)
	if not char in visited:
		visited[char] = []
	if not coords in visited[char]:
		result = check_cell(coords, char)
		print("char", str(char))
		print("result", str(result))
		out += result["area"] * result["perimeter"]
		visited[char].append(coords)


print("Result: " + str(out))