import os

class Vector2:
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)

	def __str__(self):
		return "[" + str(self.x) + "|" + str(self.y) + "]"

class Robot:
	def __init__(self, pos, vel):
		self.position = Vector2(pos[0], pos[1])
		self.velocity = Vector2(vel[0], vel[1])

def from_coords(coords):
	if coords[0] in range(len(arr[0])) and coords[1] in range(len(arr)):
		return str(arr[coords[1]][coords[0]])
	return ""

def to_coords(index):
	return [int(index % len(arr[0])), int(index / len(arr[0]))]

inputs = [["test.txt", 11, 7], ["input.txt", 101, 103]]
data = inputs[1]
string = open(data[0], "r").read()
arr = string.split(os.linesep)
out = 1
robots = []
for el in arr:
	position = el.split(" ")[0].split("=")[1]
	velocity = el.split(" ")[1].split("=")[1]
	robots.append(Robot(position.split(","), velocity.split(",")))

width = data[1]
height = data[2]
factors = [[0, 0], [0, 0]]

for robot in robots:
	robot.position.x = (robot.position.x + robot.velocity.x * 100) % width
	robot.position.y = (robot.position.y + robot.velocity.y * 100) % height
	if robot.position.x == (width-1)/2 or robot.position.y == (height-1)/2:
		continue
	quadrantX = int(robot.position.x/(width/2))
	quadrantY = int(robot.position.y/(height/2))
	factors[quadrantX][quadrantY] += 1
	print(quadrantX)
	print(quadrantY)
	print(str(robot.position))

print(factors)
for el in factors:
	for factor in el:
		out *= factor

print("Result: " + str(out))