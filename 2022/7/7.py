import os

string = open("72.txt", "r").read()
arr = string.split("$ ")

solution = 0

for x in arr:
    print(x)
print(solution)
