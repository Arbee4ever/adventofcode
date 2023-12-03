import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)


def check_area(u, v):
	area = ""
	for xy in range(9):
		a = (u - 1) + xy % 3
		b = (v - 1) + int(xy / 3)
		if (a < 0) | (b < 0):
			continue
		if (a > len(arr) - 1) | (b > len(arr[0]) - 1):
			continue
		area = area + arr[b][a]
	return area


def get_number(u, v):
	if not u - 1 == -1:
		if arr[v][u - 1].isdigit():
			return False
	number = ""
	last = False
	i = 0
	while not last:
		number = number + arr[v][u]
		u += 1
		if u >= len(arr[v]) or not arr[v][u].isdigit():
			last = True
		i += 1
	return number


out = 0
partNums = []
for y, line in enumerate(arr):
	for x in range(len(line)):
		char = line[x]
		if char.isdigit():
			num = get_number(x, y)
			if num is not False:
				partNums.append({
					"number": num,
					"x": x,
					"y": y
				})
for partNum in partNums:
	isValid = False
	for index in range(len(partNum["number"])):
		if isValid:
			isValid = False
			break
		area1 = check_area(partNum["x"] + index, partNum["y"])
		for symbol in area1:
			if not (symbol == "." or symbol.isdigit()):
				isValid = True
				out += int(partNum["number"])
				break
print("Result:", out)
