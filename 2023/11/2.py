import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)
galaxies = []
expansionVar = 999999

emptyLines = []
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
	if "#" in line:
		line_galaxies = [i for i, letter in enumerate(line) if letter == "#"]
		for g in line_galaxies:
			galaxies.append([g, i])
	else:
		emptyLines.append(i)

emptyColumns = sorted(emptyColumns)
emptyLines = sorted(emptyLines)

for galaxy in galaxies:
	xAdd = 0
	yAdd = 0
	for column in emptyColumns:
		if column < galaxy[0]:
			xAdd += expansionVar
		else:
			break
	for line in emptyLines:
		if line < galaxy[1]:
			yAdd += expansionVar
		else:
			break
	galaxy[0] += xAdd
	galaxy[1] += yAdd

out = 0
for i, galaxy in enumerate(galaxies):
	for j in range(len(galaxies)):
		if i+j+1 >= len(galaxies):
			break
		steps = abs(galaxies[i+j+1][1] - galaxy[1]) + abs(galaxies[i+j+1][0] - galaxy[0])
		out += steps

print("Result:", out)
