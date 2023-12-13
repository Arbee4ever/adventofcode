import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)
newArr = []
galaxies = []

emptyLines = 0


emptyColumns = []
for i, char in enumerate(arr[0]):
	only_space = 0
	if char == ".":
		for num in range(len(arr)):
			if arr[num][i] == ".":
				only_space += 1
			else:
				break
	if only_space == len(arr):
		emptyColumns.append(i)
for i, line in enumerate(arr):
	for index, el in enumerate(emptyColumns):
		line = line[:el+index] + "." + line[el+index:]
	newArr.insert(i + emptyLines, line)
	if "#" not in line:
		newArr.insert(i + emptyLines, ''.join([char * len(line) for char in "."]))
		emptyLines += 1

for i, line in enumerate(newArr):
	if "#" in line:
		line_galaxies = [i for i, letter in enumerate(line) if letter == "#"]
		for g in line_galaxies:
			galaxies.append([g, i])


out = 0
for i, galaxy in enumerate(galaxies):
	for j in range(len(galaxies)):
		if i+j+1 >= len(galaxies):
			break
		steps = abs(galaxies[i+j+1][1] - galaxy[1]) + abs(galaxies[i+j+1][0] - galaxy[0])
		out += steps

print("Result:", out)
