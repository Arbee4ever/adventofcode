import os
import re
from functools import cmp_to_key

string = open("input.txt", "r").read()
arr = string.split(os.linesep)
possibleCards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def compare(hand1, hand2):
	hand1 = hand1.split(" ")[0]
	hand2 = hand2.split(" ")[0]
	if get_type(hand1) > get_type(hand2):
		return 1
	elif get_type(hand1) < get_type(hand2):
		return -1
	else:
		for i, char in enumerate(hand1):
			if possibleCards.index(char) > possibleCards.index(hand2[i]):
				return -1
			elif possibleCards.index(char) < possibleCards.index(hand2[i]):
				return 1


def get_type(hand):
	hand = "".join(sorted(hand))
	matches = re.findall(r"((.)\2+)", hand)
	if len(matches) == 0:
		return 1
	elif len(matches) == 1 and len(matches[0][0]) == 2:
		return 2
	elif len(matches) == 2 and len(matches[0][0]) == 2 and len(matches[1][0]) == 2:
		return 3
	elif len(matches) == 1 and len(matches[0][0]) == 3:
		return 4
	elif len(matches) == 2 and len(matches[0][0]) == 3 and len(matches[1][0]) == 2:
		return 5
	elif len(matches) == 2 and len(matches[1][0]) == 3 and len(matches[0][0]) == 2:
		return 5
	elif len(matches[0][0]) == 4:
		return 6
	elif len(matches[0][0]) == 5:
		return 7
	print(matches)


outArr = sorted(arr, key=cmp_to_key(lambda x, y: compare(x, y)))

out = 0
for index, el in enumerate(outArr):
	bid = el.split(" ")[1]
	out += int(bid) * (index + 1)
print(outArr)
print("Result:", out)
