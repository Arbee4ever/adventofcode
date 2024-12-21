import os
from typing import Self


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

	def __mul__(self, other):
		if isinstance(other, Vector2):
			return Vector2(self.x * other.x, self.y * other.y)
		elif type(other) == int:
			return Vector2(self.x * other, self.y * other)
	def __str__(self):
		return "[" + str(self.x) + "|" + str(self.y) + "]"

class Cell:
	def __init__(self, coords: Vector2, left: Self = None, right: Self = None):
		self.c = "@"
		self.right = right
		self.left = left
		self.position = coords

	def move(self, vector: Vector2):
		return

	def movable(self, vector: Vector2):
		return False

	def __str__(self):
		return str(self)

class Robot(Cell):
	def move(self, vector: Vector2):
		movable = self.movable(vector)
		if movable:
			next_cell = house.get(self.position + vector)
			next_cell.move(vector)
			house.move(self.position, vector)
			self.position += vector
		return movable

	def set_dir(self, c):
		self.c = c

	def movable(self, vector: Vector2):
		next_cell = house.get(self.position + vector)
		movable = False
		movable_other = True
		if isinstance(next_cell, Cell):
			movable = next_cell.movable(vector)
			if str(vector) in up_down and isinstance(next_cell, Box):
				if next_cell.left is None:
					movable_other = next_cell.right.movable(vector)
				else:
					movable_other = next_cell.left.movable(vector)
		if movable_other and movable:
			return True
		else:
			return False

	def __str__(self):
		return self.c
		return "\u001B[32m" + self.c + "\u001B[0m"

class Box(Cell):
	def move(self, vector: Vector2):
		next_cell = house.get(self.position + vector)
		next_cell.move(vector)
		if str(vector) in up_down:
			if self.left is None:
				next_cell_other = house.get(self.right.position + vector)
			else:
				next_cell_other = house.get(self.left.position + vector)
			next_cell_other.move(vector)
			if self.left is None:
				house.move(self.right.position, vector)
				self.right.position += vector
			else:
				house.move(self.left.position, vector)
				self.left.position += vector
		house.move(self.position, vector)
		self.position += vector

	def movable(self, vector: Vector2):
		next_cell = house.get(self.position + vector)
		movable = []
		if isinstance(next_cell, Cell):
			movable.append(next_cell.movable(vector))
			if str(vector) in up_down:
				if self.left is None:
					next_cell_other = house.get(self.right.position + vector)
				else:
					next_cell_other = house.get(self.left.position + vector)
				movable.append(next_cell_other.movable(vector))
		if all(movable):
			return True
		else:
			return False

	def __str__(self):
		if self.left is None:
			return "["
		return "]"

class Air(Cell):
	def move(self, vector: Vector2):
		return

	def movable(self, vector: Vector2):
		return True

	def __str__(self):
		return "."

class Wall(Cell):
	def move(self, vector: Vector2):
		return

	def movable(self, vector: Vector2):
		return False

	def __str__(self):
		return "#"

class House:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.house = [["" for x in range(width)] for y in range(height)]

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
	return Vector2(int(index % len(houseRaw[0])), int(index / len(houseRaw[0])))

string = open("input.txt", "r").read()
arr = string.split(os.linesep * 2)
houseRaw = arr[0].split(os.linesep)
house = House(len(houseRaw[0])*2, len(houseRaw))
moves = "".join(arr[1].split("\n"))
out = 0

boxes = []
robot: Robot = Robot(Vector2(-1, -1))
for i, char in enumerate("".join(houseRaw)):
	pos = to_coords(i)
	pos.x *= 2
	if char == "O":
		box_left = Box(pos)
		box_right = Box(pos + Vector2(1, 0))
		boxes.append(box_left)
	elif char == "@":
		box_left = Robot(pos)
		box_right = Air(pos + Vector2(1, 0))
		robot = box_left
	elif char == "#":
		box_left = Wall(pos)
		box_right = Wall(pos + Vector2(1, 0))
	elif char == ".":
		box_left = Air(pos)
		box_right = Air(pos + Vector2(1, 0))
	box_left.right = box_right
	box_right.left = box_left
	house.put(pos, box_left)
	house.put(pos + Vector2(1, 0), box_right)

print(house)
directions = {
	"^": Vector2(0, -1),
	">": Vector2(1, 0),
	"v": Vector2(0, 1),
	"<": Vector2(-1, 0),
}
up_down = [str(Vector2(0, 1)), str(Vector2(0, -1))]
for i, move in enumerate(moves):
	#print("Move", i, move + ":")
	dir = directions[move]
	pos = Vector2(robot.position.x, robot.position.y)
	robot.move(dir)
	robot.set_dir(move)
	#print(house)

for box in boxes:
	out += box.position.y * 100 + box.position.x

print(house)
print("Result: " + str(out))