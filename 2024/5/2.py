import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep * 2)
rulesRaw = arr[0].split(os.linesep)
rules = {}
results = arr[1].split(os.linesep)
out = 0

def is_greater(a, b):
	if a in rules:
		if str(b) in rules.get(a):
			print(rules)
			return True

for rule in rulesRaw:
	first = rule.split("|")[0]
	second = rule.split("|")[1]
	if not first in rules:
		rules[first] = [second]
	else:
		rules[first].append(second)

errors = []
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
						errors.append(pages)
						error = True
						break

newResult = []
for result in errors:
	sortedBool = False
	while not sortedBool:
		sortedBool = True
		for i in range(len(result)-1):
			el = result[i]
			other = result[i+1]
			if is_greater(other, el):
				result.insert(i, result.pop(i+1))
				sortedBool = False
	index = int(len(result)/2)
	out += int(result[index])


print("Result: " + str(out))