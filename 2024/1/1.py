import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)
left = []
right = []
out = 0

for x in arr:
	if x != "":
		left.append(int(x.split(" ")[0]))
		right.append(int(x.split(" ")[1]))

left.sort()
right.sort()
for y in range(len(left)):
	if left[y] >= right[y]:
		out += left[y] - right[y]
	else:
		out += right[y] - left[y]
		
print("Result: " + str(out))