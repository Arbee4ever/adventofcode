import os
import re

import PIL.Image
from PIL import ImageDraw, ImageFont


def draw_grid():
	columns = len(arr)
	size = columns * multiplier

	block_size = multiplier

	for y in range(0, size, block_size):
		for x in range(0, size, block_size):
			img.rectangle((x, y, x + block_size, y + block_size), outline="white", width=2)


def paint(position, background, foreground, char, char2="", char3=""):
	x1 = position[0] * multiplier
	y1 = position[1] * multiplier
	x2 = x1 + multiplier
	y2 = y1 + multiplier
	shape = [(x1 + 2, y1 + 2), (x2 - 2, y2 - 2)]
	img.rectangle(shape, background, width=0)
	font = ImageFont.truetype("JetBrainsMono-Medium.ttf", multiplier)
	img.text((x1 + multiplier / 2, y1 + multiplier / 2), char, foreground, font, "mm")
	font = ImageFont.truetype("JetBrainsMono-Medium.ttf", multiplier / 2)
	img.text((x1, y1), char2, foreground, font, "lt")
	img.text((x2, y2), char3, foreground, font, "rb")


multiplier = 100
string = open("input.txt", "r").read()
arr = string.split(os.linesep)
out = 0
image = PIL.Image.new(mode="RGB", size=(len(arr) * multiplier, len(arr) * multiplier))
img = ImageDraw.Draw(image)
draw_grid()


def findAll(map):
	temp_antennas = {}
	s = "".join(map)
	for x in re.finditer(r'[^.|\n]', s):
		key = s[x.start()]
		if key in temp_antennas.keys():
			temp_antennas[key].append(to_coords(x.start(), map))
		else:
			temp_antennas[key] = [to_coords(x.start(), map)]
	return temp_antennas


def sub(a, b):
	temp = [0, 0]
	temp[0] = a[0] - b[0]
	temp[1] = a[1] - b[1]
	return temp


def add(a, b):
	temp = [0, 0]
	temp[0] = a[0] + b[0]
	temp[1] = a[1] + b[1]
	return temp


def is_inside(a):
	return 0 <= a[0] < len(arr[0]) and 0 <= a[1] < len(arr)


def from_coords(coords, map):
	if coords[0] in range(len(map[0])) and coords[1] in range(len(map)):
		return str(map[coords[1]][coords[0]])
	return ""


def to_coords(index, map):
	return [int(index % len(map[0])), int(index / len(map[0]))]


def check(antinode, freq):
	if is_inside(antinode) and not antinode in antinodes:
		antinodes.append(antinode)
		paint(antinode, (255, 0, 0), (0, 255, 0), "#", str(antinodes.count(antinode)), freq)


antennas = findAll(arr)
antinodes = []
for freq in antennas:
	for i in range(len(antennas[freq])):
		antenna = antennas[freq][i]
		paint(antenna, (0, 255, 0), (255, 0, 0), freq, str(len(antennas[freq])))
		for index in range(1, len(antennas[freq]) - i):
			antennaTwo = antennas[freq][i + index]
			check(antenna, freq)
			check(antennaTwo, freq)
			diff = sub(antennaTwo, antenna)
			antinode = sub(antenna, diff)
			while True:
				check(antinode, freq)
				antinode = sub(antinode, diff)
				# print("antinode", str(antinode))
				if not is_inside(antinode):
					break

			antinode = add(antennaTwo, diff)
			while True:
				check(antinode, freq)
				antinode = add(antinode, diff)
				if not is_inside(antinode):
					break

out = len(antinodes)
print("\n".join(arr))
image.show()
print("Result: " + str(out))
