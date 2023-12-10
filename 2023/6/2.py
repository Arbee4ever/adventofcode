import os
import re

string = open("input.txt", "r").read()
arr = string.split(os.linesep)

time = re.sub(r" +", "", arr[0]).split(":")[1]
distance = re.sub(r" +", "", arr[1]).split(":")[1]

possibleHoldTimes = 0
time = int(time)
for i in range(1, time + 1):
	dist = i * (time - i)
	if dist > int(distance):
		possibleHoldTimes += 1
	elif possibleHoldTimes != 0:
		break
print("Result:", possibleHoldTimes)
