import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)
left = []
right = []
out = 0

def checkReport(levels, problemCount):
	if all(abs(int(i) - int(j)) > 0 for i, j in zip(levels, levels[1:])):
		if all(abs(int(i) - int(j)) <= 3 for i, j in zip(levels, levels[1:])):
			if all(int(i) < int(j)for i, j in zip(levels, levels[1:])) or all(int(i) > int(j) for i, j in zip(levels, levels[1:])):
				return 1
	return 0

for report in arr:
	levels = report.split(" ")
	problemCount = 0
	problemCount += checkReport(levels, problemCount)
	if problemCount == 0:
		for index in range(len(levels)):
			newLevels = levels.copy()
			newLevels.pop(index)
			problemCount += checkReport(newLevels, problemCount)
	if problemCount >= 1:
		out += 1

print("Result: " + str(out))