import os

string = open("input.txt", "r").read()
machines = string.split(os.linesep * 2)
out = 0

for machine in machines:
	buttonA = [int(x.split("+")[1]) for x in machine.split(os.linesep)[0].split(": ")[1].split(", ")]
	buttonB = [int(x.split("+")[1]) for x in machine.split(os.linesep)[1].split(": ")[1].split(", ")]
	prize = [int(x.split("=")[1]) for x in machine.split(os.linesep)[2].split(": ")[1].split(", ")]
	result = [0, 0]
	while result != prize:
		for i in range(101):
			result[0] = buttonA[0] * i
			result[1] = buttonA[1] * i
			if result[0] > prize[0] or result[1] > prize[1]:
				break
			if result == prize:
				tokensA = i * 3
				out += tokensA
				break
			for ii in range(1, 101):
				result[0] += buttonB[0]
				result[1] += buttonB[1]
				if result == prize:
					print("i", str(i))
					print("ii", str(ii))
					print("result", str(result))
					tokensA = i * 3
					tokensB = ii
					out += tokensA + tokensB
					break
		break

print("Result: " + str(out))