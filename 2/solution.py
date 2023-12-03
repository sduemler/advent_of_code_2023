input = open("2/input.txt", "r")
lines = input.readlines()

gameMap = {}
totalIds = 0
power = 0

for line in lines:
  line = line.rstrip()
  maxRed = 0
  maxGreen = 0
  maxBlue = 0
  firstSplit = line.split(': ')
  id = firstSplit[0].split(' ')[1]
  gameSplit = firstSplit[1].split('; ')
  for split in gameSplit:
    pullSplit = split.split(', ')
    for pull in pullSplit:
      infoSplit = pull.split(' ')
      if infoSplit[1] == 'red' and int(infoSplit[0]) > maxRed:
        maxRed = int(infoSplit[0])
      if infoSplit[1] == 'blue' and int(infoSplit[0]) > maxBlue:
        maxBlue = int(infoSplit[0])
      if infoSplit[1] == 'green' and int(infoSplit[0]) > maxGreen:
        maxGreen = int(infoSplit[0])
  gameMap[id] = [maxRed, maxBlue, maxGreen]
  power += (maxRed * maxGreen * maxBlue)
  if (maxRed < 13 and maxGreen < 14) and maxBlue < 15:
    totalIds += int(id)

print(totalIds)
print(power)
