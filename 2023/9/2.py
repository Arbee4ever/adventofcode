import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)


def get_next(sequence):
	new_tree = [sequence.split()]
	new_tree[0] = [int(x) for x in new_tree[0]]
	index = len(new_tree)
	new_seq = get_new_sequence(new_tree[index - 1])
	new_tree.append(new_seq)
	while not all(v == 0 for v in new_seq):
		new_seq = get_new_sequence(new_seq)
		new_tree.append(new_seq)
	return new_tree


def get_new_sequence(prev_seq):
	new_arr = []
	for i, el in enumerate(prev_seq):
		if 0 < i < len(prev_seq):
			new_arr.append(el - prev_seq[i - 1])
	return new_arr


out = 0
for line in arr:
	tree = get_next(line)
	tree.reverse()
	for i, el in enumerate(tree):
		if i == 0:
			el.insert(0, 0)
		elif i+1 == len(tree):
			out += el[0]
			break
		else:
			tree[i+1].insert(0, tree[i+1][0] - el[0])
		tree[i] = el

print("Result:", out)
