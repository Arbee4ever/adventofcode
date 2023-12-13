import os
import sys

from PIL import Image, ImageDraw

string = open("input.txt", "r").read()
arr = string.split(os.linesep)
sys.setrecursionlimit(99999)

directions = {
	"|": [["N", "S"], [10, 0, 30, 40]],
	"-": [["E", "W"], [0, 10, 40, 30]],
	"L": [["N", "E"], [10, 0, 40, 30]],
	"J": [["N", "W"], [0, 0, 30, 30]],
	"7": [["S", "W"], [0, 10, 30, 40]],
	"F": [["S", "E"], [10, 10, 40, 40]],
	".": [[], [10, 10, 30, 30]],
	"S": [["N", "E", "S", "W"], [0, 0, 0, 0]]
}

path = []
enclosed = []
not_enclosed = []

multi = 40
img = Image.new(mode="RGB", size=(len(arr[0]) * multi, len(arr) * multi))
imgDraw = ImageDraw.Draw(img)
index = 0


def check_neighbors(x, y, prevDir):
	global index
	if [arr[y][x], x, y] in path:
		return
	index += 1
	path.append([arr[y][x], x, y])
	if 0 < y and prevDir != "S" and ("N" in directions.get(arr[y][x])[0]) and ("S" in directions.get(arr[y - 1][x])[0]):
		check_neighbors(x, y - 1, "N")
	elif x < len(arr[y]) - 1 and prevDir != "W" and ("E" in directions.get(arr[y][x])[0]) and ("W" in directions.get(arr[y][x + 1])[0]):
		check_neighbors(x + 1, y, "E")
	elif y < len(arr) - 1 and prevDir != "N" and ("S" in directions.get(arr[y][x])[0]) and ("N" in directions.get(arr[y + 1][x])[0]):
		check_neighbors(x, y + 1, "S")
	elif 0 < x and prevDir != "E" and ("W" in directions.get(arr[y][x])[0]) and ("E" in directions.get(arr[y][x - 1])[0]):
		check_neighbors(x - 1, y, "W")


def check():
	for y in range(len(arr)):
		check_enclosed(0, y)


def check_enclosed(x, y):
	if [arr[y][x], x, y] in enclosed or [arr[y][x], x, y] in not_enclosed:
		return
	pos_x = x
	crossed = 0
	current_pipe = ""
	while pos_x < len(arr[y]):
		if [arr[y][pos_x], pos_x, y] in path:
			current_pipe += arr[y][pos_x]
			if (current_pipe == "|") or (current_pipe.startswith("L") and current_pipe.endswith("7")) or (current_pipe.startswith("F") and current_pipe.endswith("J")):
				current_pipe = ""
				crossed += 1
			elif (current_pipe.startswith("L") and current_pipe.endswith("J")) or (current_pipe.startswith("F") and current_pipe.endswith("7")):
				current_pipe = ""
		elif crossed % 2 == 0:
			not_enclosed.append([arr[y][pos_x], pos_x, y])
		else:
			enclosed.append([arr[y][pos_x], pos_x, y])
		pos_x += 1


for i, line in enumerate(arr):
	if "S" in line:
		arr[i] = arr[i].replace("S", "L")
		img.paste((0, 255, 255), (line.index("S") * multi, i * multi, line.index("S") * multi + multi, i * multi + multi))
		check_neighbors(line.index("S"), i, "")
		check()
		print("Result:", len(enclosed))
		for index, pixel in enumerate(path):
			current_pix = directions.get(arr[pixel[2]][pixel[1]])
			img.paste((255, int((index / 13772) * 255), int((index / 13772) * 255)), (
				pixel[1] * multi + int(current_pix[1][0]),
				pixel[2] * multi + int(current_pix[1][1]),
				pixel[1] * multi + int(current_pix[1][2]),
				pixel[2] * multi + int(current_pix[1][3])))
			imgDraw.text((pixel[1] * multi, pixel[2] * multi), str(index) + ":\n" + str(pixel[1]) + "|" + str(pixel[2]), (0, 0, 0))
		for pixel in enclosed:
			img.paste((0, 0, 255), (pixel[1] * multi, pixel[2] * multi, pixel[1] * multi + 40, pixel[2] * multi + 40))
			imgDraw.text((pixel[1] * multi, pixel[2] * multi), str(index) + ":\n" + str(pixel[1]) + "|" + str(pixel[2]), (0, 0, 0))
		for pixel in not_enclosed:
			img.paste((0, 255, 0), (pixel[1] * multi, pixel[2] * multi, pixel[1] * multi + 20, pixel[2] * multi + 20))
		img.show()
		break
