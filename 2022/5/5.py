import os

string = open("5.txt", "r").read()
arr = string.split(2*os.linesep)
arr1 = arr[0].split(os.linesep)
arr2 = arr[1].split(os.linesep)
arr1.pop()
arr1.reverse()

dct = {}

for i in range(0, 1+int(len(arr1[0])/4)):
    dct["%s" % i] = []
for x in arr1:
    for i in range(0, 1+int(len(arr1[0])/4)):
        if x[1+i*4] != " ":
            dct["%s" % i].append(x[1+i*4])

for y in arr2:
    a = y.split(" ")
    del a[0::2]
    for i in range(0, int(a[0])):
        el = dct["%s" % str(int(a[1])-1)]
        e = el[-1]
        dct["%s" % str(int(a[2])-1)].append(e)
        del el[-1]

out = ""

for x in dct:
    out += dct[x][-1]
print(out)

dct1 = {}

for i in range(0, 1+int(len(arr1[0])/4)):
    dct1["%s" % i] = []
for x in arr1:
    for i in range(0, 1+int(len(arr1[0])/4)):
        if x[1+i*4] != " ":
            dct1["%s" % i].append(x[1+i*4])

for y in arr2:
    a = y.split(" ")
    del a[0::2]
    for i in range(-int(a[0]), 0):
        el = dct1["%s" % str(int(a[1])-1)]
        e = el[i]
        dct1["%s" % str(int(a[2])-1)].append(e)
        del el[i]

out1 = ""

for x in dct1:
    out1 += dct1[x][-1]
print(out1)
