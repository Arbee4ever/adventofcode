import os
import sys

from PIL import Image, ImageDraw

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
pixels = []

multi = 40
img = Image.new(mode="RGB", size=(140*multi, 140*multi))
imgDraw = ImageDraw.Draw(img)
index = 0


def check_neighbors(x, y, prevDir, skippixel = False):
	global index
	if arr[y][x] + str(x) + "|" + str(y) in path:
		return
	index += 1
	if not skippixel:
		img.paste((255, int((index / 11040)*255), int((index / 11040)*255)), (x*multi, y*multi, x*multi+multi, y*multi+multi))
	path.append(arr[y][x] + str(x) + "|" + str(y))
	pixels.append([x, y])
	if 0 < y and prevDir != "S" and ("N" in directions.get(arr[y][x])) and ("S" in directions.get(arr[y - 1][x])):
		check_neighbors(x, y - 1, "N")
	elif x < len(arr[y]) - 1 and prevDir != "W" and ("E" in directions.get(arr[y][x])) and ("W" in directions.get(arr[y][x + 1])):
		check_neighbors(x + 1, y, "E")
	elif y < len(arr) - 1 and prevDir != "N" and ("S" in directions.get(arr[y][x])) and ("N" in directions.get(arr[y + 1][x])):
		check_neighbors(x, y + 1, "S")
	elif 0 < x and prevDir != "E" and ("W" in directions.get(arr[y][x])) and ("E" in directions.get(arr[y][x - 1])):
		check_neighbors(x - 1, y, "W")


for i, line in enumerate(arr):
	if "S" in line:
		img.paste((0, 255, 255), (line.index("S")*multi, i*multi, line.index("S")*multi+multi, i*multi+multi))
		check_neighbors(line.index("S"), i, "", True)
		print("Result:", len(path) / 2)
		for index, pixel in enumerate(pixels):
			imgDraw.text((pixel[0]*multi, pixel[1]*multi), str(index) + ":\n" + str(pixel[0]) + "|" + str(pixel[1]), (0, 0, 0))
		img.show()
		break
