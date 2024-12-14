string = open("input.txt", "r").read()
data = []
out = 0

ii = 0
for i in range(len(string)):
	if i % 2 == 0:
		for x in range(int(string[i])):
			data.append(str(ii))
		ii += 1
	else:
		for x in range(int(string[i])):
			data.append(".")

for i in range(len(data)):
	if not i in range(len(data)):
		break
	if data[i] == ".":
		last = data.pop()
		while last == ".":
			last = data.pop()
		data[i] = last

i = 0
for char in data:
	out += int(char) * i
	i += 1

print("Result: " + str(out))
