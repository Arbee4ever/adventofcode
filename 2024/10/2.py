import os
import re

string = open("input.txt", "r").read()
arr = string.split(os.linesep)
out = 0

def from_coords(coords):
	if coords[0] in range(len(arr[0])) and coords[1] in range(len(arr)):
		return int(arr[coords[1]][coords[0]])
	return ""

def to_coords(index):
	return [int(index % len(arr[0])), int(index / len(arr[0]))]

def check_from(coords, head, path):
	score = 0
	path.append(coords)
	current = from_coords(coords)
	print("score", str(score))
	print("coords", str(coords))
	print("current", current)
	if current == 9:
		score = 1
		return score
	if from_coords([coords[0], coords[1]+1]) == current+1:
		score += check_from([coords[0], coords[1]+1], head, path)
	if from_coords([coords[0]+1, coords[1]]) == current+1:
		score += check_from([coords[0]+1, coords[1]], head, path)
	if from_coords([coords[0], coords[1]-1]) == current+1:
		score += check_from([coords[0], coords[1]-1], head, path)
	if from_coords([coords[0]-1, coords[1]]) == current+1:
		score += check_from([coords[0]-1, coords[1]], head, path)
	return score

heads = re.finditer(r"0", string.replace("\n", ""))
for i, head in enumerate(heads):
	score = 0
	path = []
	score = check_from(to_coords(head.start()), i, path)
	out += score
	print("score", str(score))

print("Result: " + str(out))