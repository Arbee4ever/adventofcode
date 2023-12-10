import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)


def gen_dict(raw_data):
	new_network = {}
	for node in raw_data:
		name = node.split(" ")[0]
		left = node.split(" = (")[1].split(", ")[0]
		right = node.split(" = (")[1].split(", ")[1].split(")")[0]
		new_network[name] = {
			"L": left,
			"R": right
		}
	return new_network


directions = arr[0]
arr.remove(arr[0])
arr.remove(arr[0])
network = gen_dict(arr)

steps = 0
currentNode = "AAA"
while not currentNode == "ZZZ":
	for dir in directions:
		currentNode = network.get(currentNode).get(dir)
		steps += 1


print("Result:", steps)
