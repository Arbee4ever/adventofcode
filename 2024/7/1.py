import os

def multiply(a, b):
	return a * b

def add(a, b):
	return a + b

string = open("input.txt", "r").read()
arr = string.split(os.linesep)
out = 0
calculations = {}
for el in arr:
	split = el.split(": ")
	calculations[int(split[0])] = [int(x) for x in split[1].split(" ")]

'''First Attempt (idk what happened here)
result = 0
done = False
operations = [add, multiply]
for calc in calculations:
	nums = calculations[calc]
	possible = (len(nums) - 1) * 2
	for ii in range(possible):
		result = 0
		binary = [int(el) for el in list(format(ii, "b"))]
		while len(binary) < len(nums) - 1:
			binary.insert(0, 0)
		print("binary", str(binary))
		for i in range(len(nums) - 1):
			op = binary[i]
			if op == 1 and result == 0:
				result += nums[0]
			result = operations[op](result, nums[i+1])
			print("result", str(result))
			if result == calc:
				print("CORRECT", str(result))
				out += calc
				done = True
				break
			result = 0
		if done:
			break
out = 0
'''

operations = [add, multiply]
for calc in calculations:
	nums = calculations[calc]
	highest = int("1" * (len(nums) - 1), 2)
	result = 0
	for i in range(highest+1):
		binary = [int(el) for el in list(format(i, "b"))]
		while len(binary) < len(nums) - 1:
			binary.insert(0, 0)
		for x in range(len(nums)):
			if x == 0:
				result = nums[x]
			else:
				op = binary[x-1]
				result = operations[op](result, nums[x])
		if result == calc:
			out += calc
			break

print("Result: " + str(out))