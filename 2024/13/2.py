#Thanks to https://play.rust-lang.org/?version=stable&mode=release&edition=2021&gist=4b2380789dca9cf602cea9ba07d6ed3e for the math formula
import os

string = open("input.txt", "r").read()
machines = string.split(os.linesep * 2)
out = 0

for machine in machines:
	buttonA = [int(x.split("+")[1]) for x in machine.split(os.linesep)[0].split(": ")[1].split(", ")]
	buttonB = [int(x.split("+")[1]) for x in machine.split(os.linesep)[1].split(": ")[1].split(", ")]
	prize = [int(x.split("=")[1]) + 10000000000000 for x in machine.split(os.linesep)[2].split(": ")[1].split(", ")]
	a = (prize[0] * buttonB[1] - prize[1] * buttonB[0]) / (buttonA[0] * buttonB[1] - buttonA[1] * buttonB[0])
	b = (buttonA[0] * prize[1] - buttonA[1] * prize[0]) / (buttonA[0] * buttonB[1] - buttonA[1] * buttonB[0])
	result = [buttonA[0] * a + buttonB[0] * b, buttonA[1] * a + buttonB[1] * b]
	if a.is_integer() and b.is_integer():
		print("result", str(result))
		print("prize", str(prize))
		print("a", str(a))
		print("b", str(b))
		tokensA = a * 3
		tokensB = b
		out += int(tokensA + tokensB)

print("Result: " + str(out))