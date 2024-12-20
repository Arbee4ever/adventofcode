import os
import re

class Vector2:
	def __init__(self, x: int, y: int):
		self.x = int(x)
		self.y = int(y)

	def __add__(self, other):
		if isinstance(other, Vector2):
			return Vector2(self.x + other.x, self.y + other.y)
		elif type(other) == int:
			return Vector2(self.x + other, self.y + other)

	def __sub__(self, other):
		if isinstance(other, Vector2):
			return Vector2(self.x - other.x, self.y - other.y)
		elif type(other) == int:
			return Vector2(self.x - other, self.y - other)

	def __str__(self):
		return "[" + str(self.x) + "|" + str(self.y) + "]"

class Robot:
	def __init__(self, pos: Vector2):
		self.position = pos

	def move(self, vector: Vector2):
		next_cell = house.get(self.position + vector)
		if type(next_cell) is Cell:
			movable = next_cell.move(vector)
		else:
			movable = True
		if movable:
			house.move(self.position, vector)
			self.position += vector
		return movable

	def __str__(self):
		return "@"

class Box:
	def __init__(self, pos: Vector2):
		self.position = pos

	def move(self, vector: Vector2):
		next_cell = house.get(self.position + vector)
		if type(next_cell) is Cell:
			movable = next_cell.move(vector)
		else:
			movable = True
		if movable:
			house.move(self.position, vector)
			self.position += vector
		return movable

	def __str__(self):
		return "O"

class Wall:
	def __init__(self, pos: Vector2):
		self.position = pos

	def move(self, vector: Vector2):
		return False

	def __str__(self):
		return "#"

class Cell:
	def __init__(self, coords: Vector2):
		self.position = coords
		self.content = None

	def move(self, vector: Vector2):
		return self.content.move(vector)

	def put(self, content: Robot | Box):
		self.content = content

	def __str__(self):
		return str(self.content)

class House:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.house = [["." for x in range(height)] for y in range(width)]

	def put(self, pos, content: Cell):
		self.house[pos.y][pos.x] = content
		return house

	def get(self, pos) -> str|Cell:
		if pos.x in range(self.width) and pos.y in range(self.height):
			return self.house[pos.y][pos.x]

	def move(self, position, vector):
		el = self.get(position)
		other = self.get(position + vector)
		self.put(position, other)
		self.put(position + vector, el)

	def __str__(self):
		string = ""
		for row in self.house:
			for cell in row:
				string += str(cell)
			string += "\n"
		return string

def to_coords(index: int):
	return Vector2(int(index % house.width), int(index / house.height))

string = open("input.txt", "r").read()
arr = string.split(os.linesep * 2)
houseRaw = arr[0].split(os.linesep)
house = House(len(houseRaw), len(houseRaw[0]))
moves = "".join(arr[1].split("\n"))
out = 0

boxes = []
robot: Robot = Robot(Vector2(-1, -1))
matches = re.finditer(r"[#@O]", "".join(houseRaw))
for match in matches:
	char = match.group()
	pos = to_coords(match.start())
	cell = Cell(pos)
	if char == "O":
		box = Box(pos)
		boxes.append(box)
	elif char == "@":
		box = Robot(pos)
		robot = box
	elif char == "#":
		box = Wall(pos)
	cell.put(box)
	house.put(pos, cell)

print(house)
directions = {
	"^": Vector2(0, -1),
	">": Vector2(1, 0),
	"v": Vector2(0, 1),
	"<": Vector2(-1, 0),
}
for i, move in enumerate(moves):
	dir = directions[move]
	pos = Vector2(robot.position.x, robot.position.y)
	robot.move(dir)
	print("Move", i, move + ":")
	print(house)

for box in boxes:
	out += box.position.y * 100 + box.position.x

print("Result: " + str(out))