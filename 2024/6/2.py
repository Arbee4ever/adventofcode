import os

import PIL.Image
from PIL import ImageDraw
from numpy import copy

def paint(x, y, background, foreground, char):
	x1 = x*10
	y1 = y*10
	x2 = x1 + 10
	y2 = y1 + 10
	shape = [(x1, y1), (x2, y2)]
	img.rectangle(shape, background, 50)
	img.text((x1, y1), char, foreground)


string = open("input.txt", "r").read()
arr = string.split(os.linesep)
out = 0
image = PIL.Image.new(mode="RGB", size=(len(arr[0])*10, len(arr)*10))
img = ImageDraw.Draw(image)
orientations = {
	"^": {
		"multiplier": -1,
		"axis": 1
	},
	">": {
		"multiplier": 1,
		"axis": 0
	},
	"v": {
		"multiplier": 1,
		"axis": 1
	},
	"<": {
		"multiplier": -1,
		"axis": 0
	}
}


def from_coords(coords, map):
	if coords[0] in range(len(map[0])) and coords[1] in range(len(map)):
		return str(map[coords[1]][coords[0]])
	return ""


def to_coords(index, map):
	return [int(index % len(map[0])), int(index / len(map[0]))]


newObstacles = []

def walk(map):
	global pos
	pos = to_coords(string.replace("\n", "").index("^"), map)
	global walking
	walking = True
	global visited
	visited = {}
	while walking:
		char = from_coords(pos, map)
		if char == "":
			return False
		axis = orientations[char]["axis"]
		multiplier = orientations[char]["multiplier"]
		newPos = copy(pos)
		path = ""
		for i in range(0, len(map)):
			newPos[int(axis)] += (1 * multiplier)
			newChar = from_coords(newPos, map)
			if str(newPos[0]) + "," + str(newPos[1]) in visited and visited[str(newPos[0]) + "," + str(newPos[1])] == orientations[char]:
				newObstacles.append(str(newPos[0]) + "," + str(newPos[1]))
				walking = False
				paint(newPos[0], newPos[1], (255, 0, 0), (0, 255, 0), "O")
				return True
			if newChar == "#":
				newPos[int(axis)] += -1 * multiplier
				temp = list(orientations)
				tempI = temp.index(char) + 1
				if tempI >= len(temp):
					tempI = tempI - len(temp)
				map[pos[1]] = map[pos[1]][:pos[0]] + "X" + map[pos[1]][pos[0] + 1:]
				map[newPos[1]] = map[newPos[1]][:newPos[0]] + temp[tempI] + map[newPos[1]][newPos[0] + 1:]
				pos = copy(newPos)
				break
			elif newChar == ".":
				path += newChar
				map[newPos[1]] = map[newPos[1]][:newPos[0]] + "X" + map[newPos[1]][newPos[0] + 1:]
				if not str(newPos[0]) + "," + str(newPos[1]) in visited:
					visited[str(newPos[0]) + "," + str(newPos[1])] = orientations[char]
					paint(newPos[0], newPos[1], (0, 255, 0), (255, 0, 0), "X")

			elif newChar == "":
				return False


walk(copy(arr))

count = 0
for x in visited:
	count += 1
	print(count, "x", str(x))
	newArr = copy(arr)
	coords = []
	coords.append(int(x.split(",")[0]))
	coords.append(int(x.split(",")[1]))
	newArr[coords[1]] = newArr[coords[1]][:coords[0]] + "#" + newArr[coords[1]][coords[0] + 1:]
	if walk(newArr):
		out += 1

print("newObstacles", str(newObstacles))
print("Result: " + str(out))
image.show()