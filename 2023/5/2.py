import os
import re

string = open("test.txt", "r").read()
arr = string.split(os.linesep * 2)

def parse_map(raw_map):
	raw_map = raw_map.split(":" + os.linesep)[1].split(os.linesep)
	new_map = []
	for el in raw_map:
		new_map.append({
			"source": int(el.split()[1]),
			"destination": int(el.split()[0]),
			"size": int(el.split()[2])
		})
	return new_map


seeds = arr[0].split(": ")[1]
seeds = re.findall(r"\d+ \d+", seeds)
print(seeds)

out = 0
for seed in seeds:
	for mapI in range(len(arr) - 1):
		mapType = parse_map(arr[mapI + 1])
		for map in mapType:
			if map.get("source") <= int(seed) <= map.get("source") + map.get("size") - 1:
				add = int(seed) - map.get("source")
				seed = map.get("destination") + add
				break
	if out == 0 or seed < out:
		out = seed
print(out)
