import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep * 2)
rulesRaw = arr[0].split(os.linesep)
rules = {}
results = arr[1].split(os.linesep)
out = 0

for rule in rulesRaw:
	first = rule.split("|")[0]
	second = rule.split("|")[1]
	if not first in rules:
		rules[first] = [second]
	else:
		rules[first].append(second)

for result in results:
	error = False
	pages = result.split(",")
	for page in pages:
		if error:
			break
		pageI = pages.index(page)
		if page in rules:
			others = rules[page]
			for other in others:
				if error:
					break
				if other in pages:
					otherI = pages.index(other)
					if pageI > otherI:
						error = True
						break
	if not error:
		index = int(len(pages)/2)
		out += int(pages[index])

print("Result: " + str(out))