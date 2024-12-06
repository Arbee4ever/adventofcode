import os
import re

import PIL.Image
from PIL import ImageDraw


def findAll(s, ch):
	s = s.replace("\n", "")
	return [i for i, ltr in enumerate(s) if ltr == ch]

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
image = PIL.Image.new(mode="RGB", size=(len(arr)*10, len(arr)*10))
img = ImageDraw.Draw(image)
matrix = []
for el in arr:
	matrix.append(list(el))
out = 0

out += len(re.findall(r"XMAS", string))
out += len(re.findall(r"SAMX", string))

cols = zip(*arr)
stringRot = ""
for col in cols:
	stringRot += "".join(col)
	stringRot += "\n"

out += len(re.findall(r"XMAS", stringRot))
out += len(re.findall(r"SAMX", stringRot))
print("Result0: " + str(out))

allX = findAll(string, "X")

for x in allX:
	xString = ""

	matrixX = int(x % len(arr[0]))
	matrixY = int(x / len(arr[0]))
	#\
	for i in range(-3, 4):
		print(str(matrixX + i) + "|" + str(matrixY + i))
		if 0 <= matrixX + i < len(arr[0]) and 0 <= matrixY + i < len(arr):
			char = matrix[matrixY + i][matrixX + i]
			if not char == "X":
				paint(matrixX + i, matrixY + i, (0, 255, 0), (255, 0, 0), char)
			xString += char
		else:
			continue

	out += len(re.findall(r"XMAS", xString))
	out += len(re.findall(r"SAMX", xString))
	print("Result2: " + str(out))
	xString = ""

	print("--------------------")

	#/
	for i in range(-3, 4):
		print(str(matrixX - i) + "|" + str(matrixY + i))
		if 0 <= matrixX - i < len(arr[0]) and 0 <= matrixY + i < len(arr):
			char = matrix[matrixY + i][matrixX - i]
			if not char == "X":
				paint(matrixX - i, matrixY + i, (0, 255, 0), (255, 0, 0), char)
			xString += char
		else:
			continue

	paint(matrixX, matrixY, (0, 0, 255), (255, 0, 0), "X")

	print(xString)
	out += len(re.findall(r"XMAS", xString))
	out += len(re.findall(r"SAMX", xString))
	print("Result2: " + str(out))

print("Result: " + str(out))
image.show()