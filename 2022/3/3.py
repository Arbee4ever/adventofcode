import os
import string as e

string = open("3.txt", "r").read()
arr = string.split(os.linesep)

score = 0

for x in arr:
	split = [x[:len(x)//2], x[len(x)//2:]]
	a = list(set(split[0]) & set(split[1]))
	y = a[0]
	score += e.ascii_letters.index(y) + 1

print(score)

arrlen = len(arr)

score2 = 0

for x in range(0, int(arrlen/3)):
	a = list(set(arr[x*3]) & set(arr[x*3+1]) & set(arr[x*3+2]))
	y = a[0]
	score2 += e.ascii_letters.index(y) + 1

print(score2)