import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)


out = 0
for line in arr:
	i = 0
	cardWorth = 0
	tempLine = line.split(": ")[1]
	winningNums = tempLine.split(" | ")[0]
	haveNums = tempLine.split(" | ")[1]
	for num in winningNums.split(" "):
		if num == "":
			continue
		if num in haveNums.split(" "):
			if i == 0:
				cardWorth = 1
			elif i >= 1:
				cardWorth = cardWorth * 2
			i += 1
	out += cardWorth
print("Result:", out)
