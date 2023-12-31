import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)

out = 0
for line in arr:
	redMax = 12
	greenMax = 13
	blueMax = 14

	inputData = line.split("Game ")[1]
	gameID = int(inputData.split(": ")[0])
	gameData = inputData.split(": ")[1]
	valid = True
	for data in gameData.split("; "):
		for cubes in data.split(", "):
			cubesData = cubes.split(" ")
			match cubesData[1]:
				case "red":
					if int(cubesData[0]) > redMax:
						valid = False
						break
				case "green":
					if int(cubesData[0]) > greenMax:
						valid = False
						break
				case "blue":
					if int(cubesData[0]) > blueMax:
						valid = False
						break
				case _:
					print("Error")
					break
	if valid:
		out += gameID
print(out)
