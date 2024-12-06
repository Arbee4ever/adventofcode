import re

string = open("input.txt", "r").read()
arr = re.findall(r"mul\([0-9]{1,4},[0-9]{1,4}\)|do\(\)|don't\(\)", string, re.MULTILINE)
out = 0

dont = False

for el in arr:
    if el == "don't()":
        dont = True
        continue
    elif el == "do()":
        dont = False
        continue
    if dont == False:
        split = el.split(",")
        x = int(split[0].split("(")[1])
        y = int(split[1].split(")")[0])
        out += x * y

print("Result: " + str(out))
