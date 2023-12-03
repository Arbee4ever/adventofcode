import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)


def get_area(u, v):
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
			return get_number(u-1, v)
	number = ""
	last = False
	while not last:
		number = number + arr[v][u]
		u += 1
		if u >= len(arr[v]) or not arr[v][u].isdigit():
			last = True
	return number


out = 0
symbols = []
for y, line in enumerate(arr):
	for x in range(len(line)):
		char = line[x]
		if not (char == "." or char.isdigit()):
			symbols.append({
				"symbol": char,
				"x": x,
				"y": y
			})

for symbol in symbols:
	if symbol["symbol"] == "*":
		numbers = []
		area = get_area(symbol["x"], symbol["y"])
		for i, sym in enumerate(area):
			if sym.isdigit():
				num = get_number((symbol["x"] - 1) + int(i % 3), (symbol["y"] - 1) + int(i / 3))
				if num not in numbers:
					print(num)
					numbers.append(num)
					if len(numbers) == 2:
						out += int(numbers[0]) * int(numbers[1])
						numbers = []
print("Result:", out)
