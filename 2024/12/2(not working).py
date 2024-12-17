import os

from PIL import ImageDraw, Image, ImageFont

string = open("test2.txt", "r").read()
arr = string.split(os.linesep)


def draw_grid():
	size = image.size[0]

	block_size = 100

	for y in range(0, size, block_size):
		for x in range(0, size, block_size):
			img.rectangle((x, y, x + block_size, y + block_size), outline="white", width=2)


fenceWidth = 15
fences = {
	"[0, 1]": [(-fenceWidth, -fenceWidth), (100 + fenceWidth, 0)],
	"[1, 0]": [(-fenceWidth, -fenceWidth), (0, 100 + fenceWidth)],
	"[0, -1]": [(-fenceWidth, 100), (100 + fenceWidth, 100 + fenceWidth)],
	"[-1, 0]": [(100, -fenceWidth), (100 + fenceWidth, 100 + fenceWidth)]
}


def paint(position, background, foreground, char, shape=None):
	x1 = position[0] * 100
	y1 = position[1] * 100
	x2 = x1 + 100
	y2 = y1 + 100
	if shape is None:
		shape = [(x1, y1), (x2, y2)]
		img.rectangle(shape, foreground, 50)
		font = ImageFont.truetype("../../JetBrainsMono-Medium.ttf", 50)
		img.text((x1 + 50, y1 + 50), char, background, font=font, anchor="mm")
	else:
		x1 += shape[0][0]
		y1 += shape[0][1]
		x2 += -(100 - shape[1][0])
		y2 += -(100 - shape[1][1])
		shape = [(x1, y1), (x2, y2)]
		img.rectangle(shape, background)


out = 0
visited = {}
groups = []
image = Image.new(mode="RGB", size=(len(arr) * 100, len(arr) * 100))
img = ImageDraw.Draw(image)
orientations = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def from_coords(coords):
	if coords[0] in range(len(arr[0])) and coords[1] in range(len(arr)):
		return arr[coords[1]][coords[0]]
	return ""


def to_coords(index):
	return [int(index % len(arr[0])), int(index / len(arr[0]))]


def check_cell(coords, char, dir):
	val = {"area": [], "sides": dict((str(el), []) for el in orientations)}
	print("val", str(val))
	if not from_coords(coords) == char:
		print("dir", str(dir))
		val["sides"][str(dir)].append(coords)
		if dir != [0, 0]:
			paint(coords, (255, 0, 0), (0, 255, 0), char, fences[str(dir)])
		return val
	if coords in visited[char]:
		return val
	visited[char].append(coords)
	val["area"].append(coords)
	print("val", str(val))
	for diff in orientations:
		next_cell = check_cell([coords[0] + diff[0], coords[1] + diff[1]], char, diff)
		val["area"] += next_cell["area"]
		if dir != [0, 0]:
			val["sides"][str(diff)] += next_cell["sides"][str(diff)]
	print("val", str(val))
	return val


def compare(a, b):
	return a[0] == b[0] or a[1] == b[1]


for i in range(len(string.replace("\n", ""))):
	coords = to_coords(i)
	char = from_coords(coords)
	paint(coords, (255, 0, 0), (0, 255, 0), char)

result = {}
for i in range(len(string.replace("\n", ""))):
	coords = to_coords(i)
	char = from_coords(coords)
	if not char in visited:
		visited[char] = []
	if not coords in visited[char]:
		result = check_cell(coords, char, [0, 0])
		groups.append({"char": char, "origin": coords, "area": result["area"], "sides": result["sides"]})
		visited[char].append(coords)

orientations2 = [[0, -1], [1, 0], [0, 1], [-1, 0]]
for group in groups:
	orientationI = 0
	startingOr = orientations[orientationI]
	orientation = startingOr
	sidesNum = 0
	group_sides = group["sides"]
	sides = []
	cells = group["area"]
	starting = group["origin"]
	position = starting
	char = group["char"]
	for i in range(len(group_sides)):
		while orientationI >= len(orientations):
			orientationI -= 4
		right = orientations[0]
		if orientationI + 1 < len(orientations):
			right = orientations[orientationI + 1]
		else:
			right = orientations[orientationI + 1 - 4]

		left = orientations[len(orientations) - 1]
		if orientationI - 1 >= 0:
			left = orientations[orientationI - 1]
		else:
			left = orientations[orientationI - 1 + 4]

		back = []
		if orientationI + 2 >= len(orientations):
			back = orientations[orientationI + 2 - len(orientations)]
		else:
			back = orientations[orientationI + 2]

		temp = 0
		for o in orientations2:
			if char != from_coords([position[0] + o[0], position[1] + o[1]]):
				sides.append([position[0] + o[0], position[1] + o[1]])
				temp += 1
				#print("sides", str(sides))
		if temp == 4:
			sidesNum += 4
			break

		if char == from_coords([position[0] + left[0], position[1] + left[1]]):
			orientation = left
			orientationI -= 1
			sidesNum += 1
		elif char == from_coords([position[0] + orientation[0], position[1] + orientation[1]]):
			pass
		elif char == from_coords([position[0] + right[0], position[1] + right[1]]):
			orientation = right
			orientationI += 1
			sidesNum += 1
		elif char == from_coords([position[0] + back[0], position[1] + back[1]]):
			orientation = back
			orientationI += 2
			sidesNum += 2
		position = [position[0] + orientation[0], position[1] + orientation[1]]
	out += len(group["area"]) * len(sides)

print("Result: " + str(out))
draw_grid()
image.show()
