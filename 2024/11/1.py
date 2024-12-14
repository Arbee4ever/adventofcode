string = open("input.txt", "r").read()
arr = [int(x) for x in string.split(" ")]
out = 0


def blink(stone):
	if stone == 0:
		return [1]
	elif len(str(stone)) % 2 == 0:
		stoneLen = int(len(str(stone)) / 2)
		return [int(str(stone)[:stoneLen]), int(str(stone)[stoneLen:])]
	else:
		return [stone * 2024]


result = [arr]
print("result", str(result[0]))
for i in range(25):
	new = []
	for el in result[i]:
		for stone in blink(el):
			new.append(stone)
	print("new", str(new))
	result.append(new)

out = len(result[len(result) - 1])

print("Result: " + str(out))
