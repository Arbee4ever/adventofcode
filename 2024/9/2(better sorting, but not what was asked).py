string = open("test.txt", "r").read()
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
print("system", str(system))

done = False
while not done:
	for i, el in enumerate(system):
		print("system", str(system))
		for num, test in enumerate(system):
			if 0 <= num+1 < len(system):
				if "." in test and "." in system[num+1]:
					system.pop(num)
					system[num] += test
		if i == len(system) - 1:
			done = True
			break
		if "." in el:
			spaceLen = len(el)
			for x in range(len(system)):
				index = len(system) - x - 1
				if index < i:
					i += 1
					continue
				file = system[index]
				if "." in file:
					continue
				fileLen = len(file)
				diff = spaceLen - fileLen
				if diff >= 0:
					file = system.pop(index)
					if len(file) > 0:
						system.insert(index, ["."] * len(file))
					system.pop(i)
					system.insert(i, file)
					if diff != 0:
						system.insert(i + 1, ["."] * diff)
					break

print("system", str(system))
for i, file in enumerate(system):
	system.pop(i)
	system.insert(i, "".join(file))
system = "".join(system)
print("system", str(system))


for i, char in enumerate(system):
	if char == ".": continue
	out += i * int(char)

print("Result: " + str(out))
