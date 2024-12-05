import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)
left = []
right = []
leftCount = {}
rightCount = {}
out = 0

for x in arr:
	if x != "":
		leftX = int(x.split("   ")[0])
		rightX = int(x.split("   ")[1])
		left.append(leftX)
		if not leftX in leftCount:
			leftCount[leftX] = 0
		leftCount[leftX] += 1
		right.append(rightX)
		if not rightX in rightCount:
			rightCount[rightX] = 0
		rightCount[rightX] += 1

left.sort()
right.sort()
for y in range(len(left)):
	if left[y] in rightCount:
		out += int(left[y] * rightCount[left[y]])
		
print("Result: " + str(out))