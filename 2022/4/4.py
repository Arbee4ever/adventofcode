import os

string = open("4.txt", "r").read()
arr = string.split(os.linesep)

score = 0

for x in arr:
	split = x.split(",")
	split2 = split[0].split("-")
	split3 = split[1].split("-")
	if set(range(int(split2[0]), int(split2[1])+1)).issubset(range(int(split3[0]), int(split3[1])+1)):
		score += 1
		continue
	if set(range(int(split3[0]), int(split3[1])+1)).issubset(range(int(split2[0]), int(split2[1])+1)):
		score += 1
		continue
print(score)

score1 = 0

for x in arr:
	split = x.split(",")
	split2 = split[0].split("-")
	split3 = split[1].split("-")
	if set(range(int(split2[0]), int(split2[1])+1)).intersection(range(int(split3[0]), int(split3[1])+1)):
		score1 += 1
		continue
	if set(range(int(split3[0]), int(split3[1])+1)).intersection(range(int(split2[0]), int(split2[1])+1)):
		score1 += 1
		continue
print(score1)