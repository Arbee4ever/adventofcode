string = open("input.txt", "r").read()
data = [int(x) for x in string]
system = []
out = 0

i = 0
for id, el in enumerate(data):
	if id % 2 == 0:
		if el > 0:
			system.append([str(i)] * el)
		i += 1
	else:
		if el > 0:
			system.append(["."] * el)

for i in range(len(system)):
	file = system[len(system) - i - 1]
	print(i, file)
	if "." in file:
		continue
	fileLen = len(file)
	for index, space in enumerate(system):
		if index >= len(system) - i - 1:
			break
		if "." in space and len(space) >= fileLen:
			system.pop(index)
			system.pop(len(system) - i - 1)
			system.insert(len(system) - i, ["."] * len(file))
			system.insert(index, file)
			if 0 <= index + 1 < len(system) and len(space) != fileLen:
				system.insert(index+1, ["."] * (len(space) - fileLen))
			break

i = 0
for file in system:
	for char in file:
		if "." in char:
			i += 1
			continue
		else:
			out += i* int(char)
			i += 1
			continue

print("Result: " + str(out))