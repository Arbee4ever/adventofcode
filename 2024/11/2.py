from functools import lru_cache
#Thanks to https://github.com/RD-Dev-29/advent_of_code_24/blob/main/code_files/day11.py for showing me lru_cache

string = open("input.txt", "r").read()
arr = [int(x) for x in string.split(" ")]
out = 0
cache = {}


def blink(stone):
	if stone in cache:
		return cache[stone]
	if stone == 0:
		val = [1]
	elif len(str(stone)) % 2 == 0:
		stone_len = int(len(str(stone)) / 2)
		val = [int(str(stone)[:stone_len]), int(str(stone)[stone_len:])]
	else:
		val = [stone * 2024]
	cache[stone] = val
	return val


@lru_cache(maxsize=None)
def blink_for_stone(stone, blinks):
	if blinks == 0:
		return 1

	count = 0
	new_stones = blink(stone)
	for new_stone in new_stones:
		count += blink_for_stone(new_stone, blinks - 1)

	return count


print("arr", str(arr))
for el in arr:
	out += blink_for_stone(el, 75)

print("Result: " + str(out))
