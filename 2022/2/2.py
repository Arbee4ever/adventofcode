import os

string = open("2.txt", "r").read()
arr = string.split(os.linesep)

score = 0

theirs = ["A", "B", "C"]
mine =   ["X", "Y", "Z"]

for x in arr:
	split = x.split(" ")
	me = mine.index(split[1])
	them = theirs.index(split[0])
	score += me + 1
	if me - them == 2:
		score += 0
		continue
	if them - me == 2:
		score += 6
		continue
	if me < them:
		score += 0
		continue
	if me == them:
		score += 3
		continue
	if me > them:
		score += 6
		continue

print(score)

score1 = 0

for x in arr:
	split = x.split(" ")
	me = mine.index(split[1])
	them = theirs.index(split[0])
	score1 += me * 3
	if me == 0:
		e = them - 1
		if e == -1:
			e = 2
		score1 += e
	if me == 1:
		e = them
		score1 += e
	if me == 2:
		e = them + 1
		if e == 3:
			e = 0
		score1 += e
	score1 += 1

print(score1)