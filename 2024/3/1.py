import os
import re

string = open("input.txt", "r").read()
arr = re.findall("mul\([0-9]{1,4},[0-9]{1,4}\)", string)
out = 0

print(len(arr))
for el in arr:
    split = el.split(",")
    x = int(split[0].split("(")[1])
    y = int(split[1].split(")")[0])
    out += x * y
    
 print("Result: " + str(out))