import os
import re


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

i = 0
found = False
while not found:
	i += 1
	space = ["." * width] * height
	for robot in robots:
		robot.position.x = (robot.position.x + robot.velocity.x) % width
		robot.position.y = (robot.position.y + robot.velocity.y) % height
		space[robot.position.y] = space[robot.position.y][:robot.position.x] + "#" + space[robot.position.y][robot.position.x + 1:]

	for row in space:
		if len(re.findall(r"#{10,500}", row)) != 0:
			print("\n".join(space))
			print("\n")
			print(i)
			print("\n")
			found = True
			break

print("Result: " + str(out))