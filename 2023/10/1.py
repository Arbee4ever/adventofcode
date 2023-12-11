import os
import sys

string = open("input.txt", "r").read()
arr = string.split(os.linesep)
sys.setrecursionlimit(99999)

directions = {
	"|": ["N", "S"],
	"-": ["E", "W"],
	"L": ["N", "E"],
	"J": ["N", "W"],
	"7": ["S", "W"],
	"F": ["S", "E"],
	".": [],
	"S": ["N", "E", "S", "W"]
}

path = []


def check_neighbors(x, y):
	if arr[y][x] + str(x) + str(y) in path:
		return
	path.append(arr[y][x] + str(x) + str(y))
	if 0 < y and ("S" in directions.get(arr[y - 1][x])) and ("N" in directions.get(arr[y][x])):
		check_neighbors(x, y - 1)
	if x < len(arr[y]) - 1 and ("W" in directions.get(arr[y][x + 1])) and ("E" in directions.get(arr[y][x])):
		check_neighbors(x + 1, y)
	if y < len(arr) - 1 and ("N" in directions.get(arr[y + 1][x])) and ("S" in directions.get(arr[y][x])):
		check_neighbors(x, y + 1)
	if 0 < x and ("E" in directions.get(arr[y][x - 1])) and ("W" in directions.get(arr[y][x])):
		check_neighbors(x - 1, y)


for i, line in enumerate(arr):
	if "S" in line:
		check_neighbors(line.index("S"), i)
		print(len(path))
		print("Result:", len(path) / 2)
		break
