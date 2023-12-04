import os
import time
import re

# get the start time
st = time.time()

string = open("input.txt", "r").read()
arr = string.split(os.linesep)
arrLen = len(arr)
knownCards = {}


def check_cards(cards):
	won_cards = []
	for line in cards:
		matches = 0
		card_num = int(re.split(r"Card +", line.split(": ")[0])[1]) - 1
		if str(card_num) in knownCards.keys():
			for item in knownCards[str(card_num)]:
				won_cards.append(item)
			continue
		knownCards[str(card_num)] = []
		temp_line = re.split(r": +", line)[1]
		winning_nums = re.split(r" +\| +", temp_line)[0]
		have_nums = re.split(r" +\| +", temp_line)[1]
		for num in re.split(r"\s+", winning_nums):
			if num in re.split(r"\s+", have_nums):
				matches += 1
				if card_num+matches >= arrLen:
					break
				knownCards[str(card_num)].append(arr[card_num+matches])
				won_cards.append(arr[card_num+matches])
	return won_cards


newCards = check_cards(arr)
while not len(newCards) == 0:
	for card in newCards:
		arr.append(card)
	newCards = check_cards(newCards)

print("Result:", len(arr))
et = time.time()

elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
