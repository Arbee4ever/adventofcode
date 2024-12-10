import os

from numpy import copy

string = open("input.txt", "r").read()
arr = string.split(os.linesep)
out = 0
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

def from_coords(coords):
	if coords[0] in range(len(arr[0])) and coords[1] in range(len(arr)):
		return str(arr[coords[1]][coords[0]])
	return ""

def to_coords(index):
	return [int(index % len(arr[0])), int(index / len(arr[0]))]

pos = to_coords(string.replace("\n", "").index("^"))
inside = True
while inside:
	char = from_coords(pos)
	if char == "":
		inside = False
		break
	axis = orientations[char]["axis"]
	multiplier = orientations[char]["multiplier"]
	newPos = copy(pos)
	path = ""
	for i in range(0, len(arr)):
		newPos[int(axis)] += (1 * multiplier)
		newChar = from_coords(newPos)
		if newChar == "#":
			newPos[int(axis)] += -1 * multiplier
			temp = list(orientations)
			tempI = temp.index(char) + 1
			if tempI >= len(temp):
				tempI = tempI - len(temp)
			arr[pos[1]] = arr[pos[1]][:pos[0]] + "X" + arr[pos[1]][pos[0] + 1:]
			arr[newPos[1]] = arr[newPos[1]][:newPos[0]] + temp[tempI] + arr[newPos[1]][newPos[0] + 1:]
			pos = copy(newPos)
			break
		elif newChar == ".":
			path += newChar
			arr[newPos[1]] = arr[newPos[1]][:newPos[0]] + "X" + arr[newPos[1]][newPos[0] + 1:]
		elif newChar == "":
			inside = False
			break
	out += path.count(".")

out += 1
print("Result: " + str(out))