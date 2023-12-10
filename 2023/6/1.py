import os
import re

string = open("input.txt", "r").read()
arr = string.split(os.linesep)

times = re.split(r": +", arr[0])[1]
times = re.split(r" +", times)
distances = re.split(r": +", arr[1])[1]
distances = re.split(r" +", distances)
print(distances)

out = 1
for index, time in enumerate(times):
	possibleHoldTimes = 0
	time = int(time)
	for i in range(1, time + 1):
		dist = i * (time - i)
		if dist > int(distances[index]):
			possibleHoldTimes += 1
	out = out * possibleHoldTimes
print("Result:", out)
