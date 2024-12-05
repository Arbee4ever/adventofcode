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
		leftCount[leftX] += 1
		right.append(rightX)
		rightCount[rightX] += 1

left.sort()
right.sort()
for y in range(len(left)):
	if left[y].
		
print("Result: " + str(out))