import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)

out = 0
for x in arr: