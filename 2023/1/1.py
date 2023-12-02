import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)

out = 0
for x in arr:
	for y in range(len(x)):
		if x[y].isdigit():
			out = out + (int(x[y]) * 10)
			break
	for y in range(len(x)):
		if x[(len(x) - 1) - y].isdigit():
			out = out + int(x[(len(x) - 1) - y])
			break
print("Result: " + str(out))
