import os
import re

string = open("input.txt", "r").read()
arr = string.split(os.linesep)


dic = {
	"one": "1",
	"two": "2",
	"three": "3",
	"four": "4",
	"five": "5",
	"six": "6",
	"seven": "7",
	"eight": "8",
	"nine": "9"
}
pattern = "(?=(" + "|".join(dic.keys()) + "))"


for x in arr:
	arr[arr.index(x)] = re.sub(pattern, lambda m: dic[m.group(1)], x)

print(arr)

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
