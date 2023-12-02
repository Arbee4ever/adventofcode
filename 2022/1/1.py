import os

string = open("1.txt", "r").read()
arr = string.split(2*os.linesep)

out = []
for x in arr:
    split = x.split(os.linesep)
    print(split)
    a = 0
    for y in split:
        if y == "":
            continue
        a = a + int(y)
    out.append(a)

out.sort()
print(out)
