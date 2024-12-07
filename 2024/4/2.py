import os

import PIL.Image
from PIL import ImageDraw

xmas = ["MMASS", "MSAMS", "SSAMM", "SMASM"]


def findAll(s, ch):
	s = s.replace("\n", "")
	return [i for i, ltr in enumerate(s) if ltr == ch]


def paint(position, background, foreground, char):
	x1 = position["x"] * 10
	y1 = position["y"] * 10
	x2 = x1 + 10
	y2 = y1 + 10
	shape = [(x1, y1), (x2, y2)]
	img.rectangle(shape, background, 50)
	img.text((x1, y1), char, foreground)


string = open("input.txt", "r").read()
arr = string.split(os.linesep)
image = PIL.Image.new(mode="RGB", size=(len(arr) * 10, len(arr) * 10))
img = ImageDraw.Draw(image)
matrix = []
for el in arr:
	matrix.append(list(el))
out = 0

allA = findAll(string, "A")

for a in allA:
	aString = ""

	matrixX = int(a % len(arr[0]))
	matrixY = int(a / len(arr[0]))

	print(str(matrixX) + "|" + str(matrixY))
	for i in [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)]:
		print(i)
		coords = {"x": matrixX + i[0], "y": matrixY + i[1]}
		print(coords)
		if 0 <= coords["x"] < len(arr[0]) and 0 <= coords["y"] < len(arr):
			char = matrix[coords["y"]][coords["x"]]
			paint(coords, (0, 255, 0), (255, 0, 0), char)
			aString += char
		else:
			continue

	print("aString", str(aString))
	if aString in xmas:
		out += 1
		paint({"x": matrixX, "y": matrixY}, (0, 0, 255), (255, 0, 0), "A")

print("Result: " + str(out))
image.show()
