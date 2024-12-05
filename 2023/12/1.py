import os
import re

string = open("test.txt", "r").read()
arr = string.split(os.linesep)


def is_valid(springsList, groupsList):
	if "?" in springsList:
		return False
	elements = re.findall(r"((#)\2*)", springsList)
	for i, el in enumerate(elements):
		if not len(el[0]) == groupsList[i]:
			return False
	return True


print(is_valid(".##.##.#..", [2, 2, 1]))

for line in arr:
	springs = line.split(" ")[0]
	groups = line.split(" ")[1].split(",")
