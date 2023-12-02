import os

string = open("input.txt", "r").read()
arr = string.split(os.linesep)

out = 0
for line in arr:
	redCubes = 0
	greenCubes = 0
	blueCubes = 0

	inputData = line.split("Game ")[1]
	gameID = int(inputData.split(": ")[0])
	gameData = inputData.split(": ")[1]
	for data in gameData.split("; "):
		for cubes in data.split(", "):
			cubesData = cubes.split(" ")
			match cubesData[1]:
				case "red":
					if redCubes < int(cubesData[0]):
						redCubes = int(cubesData[0])
				case "green":
					if greenCubes < int(cubesData[0]):
						greenCubes = int(cubesData[0])
				case "blue":
					if blueCubes < int(cubesData[0]):
						blueCubes = int(cubesData[0])
				case _:
					print("Error")
					break
	out += (redCubes * greenCubes * blueCubes)
print(out)
