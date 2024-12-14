import os


def multiply(a, b):
	return a * b


def add(a, b):
	return a + b


def concatenate(a, b):
	return int(str(a) + str(b))


def all_op(amount):
	arr = list(operations)
	n = len(arr)
	indices = [0] * amount

	result = []
	while True:
		combination = [arr[i] for i in indices]
		result.append(combination)

		i = amount - 1
		while i >= 0:
			indices[i] += 1
			if indices[i] < n:
				break
			indices[i] = 0
			i -= 1

		if i < 0:
			break

	return result


string = open("input.txt", "r").read()
arr = string.split(os.linesep)
out = 0
calculations = {}
stack = []
for el in arr:
	split = el.split(": ")
	calculations[int(split[0])] = [int(x) for x in split[1].split(" ")]

operations = {"+": add, "*": multiply, "||": concatenate}


def calculate(test_stack):
	stack_copy = test_stack.copy()
	index = 0
	while index < len(stack_copy):
		item = stack_copy[index]
		if item in operations:
			first = stack_copy.pop(0)
			second = stack_copy.pop(0)
			stack_copy.pop(0)
			stack_copy.insert(0, operations[item](first, second))
			index -= 2
		index += 1
	return stack_copy


for calc in calculations:
	result = 0
	allOps = all_op(len(calculations[calc]) - 1)
	for ops in allOps:
		stack = []
		result = 0
		i = 0
		for number in calculations[calc]:
			stack.append(number)
			length = len(stack)
			if not length == 0 and length % 2 == 0:
				stack.append(ops[i])
				i += 1
		outcome = calculate(stack)
		result = outcome[0]
		if result == calc:
			print(list(calculations).index(calc) + 1, calc, "[" + ",".join(map(str, stack)) + "]")
			out += result
			break
	if result == calc:
		continue

print("Result: " + str(out))
