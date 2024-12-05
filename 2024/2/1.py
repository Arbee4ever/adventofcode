import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)
left = []
right = []
out = 0

def checkReport(report):
	levels = report.split(" ")
	if not all(abs(int(i) - int(j)) <= 3 for i, j in zip(levels, levels[1:])):
		print("1: " + report)
		return 0
	elif not all(int(i) < int(j) for i, j in zip(levels, levels[1:])):
		if not all(int(i) > int(j) for i, j in zip(levels, levels[1:])):
			print("2: " + report)
			return 0
	return 1

for report in arr:
	out += checkReport(report)

print("Result: " + str(out))