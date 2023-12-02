from collections import Counter

string = open("6.txt", "r").read()

solution = 0

for i in range(4, len(string)):
    if solution != 0:
        break
    e = Counter(string[i-4:i])
    for char, count in e.items():
        if (count > 1):
            break
        if string[i-4:i].index(char) == 3:
            solution = i
            break
print(solution)

solution1 = 0

for i in range(14, len(string)):
    if solution1 != 0:
        break
    e = Counter(string[i-14:i])
    for char, count in e.items():
        if (count > 1):
            break
        if string[i-14:i].index(char) == 13:
            solution1 = i
            break
print(solution1)
