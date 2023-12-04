input = open("3/input.txt", "r")
lines = input.readlines()

partList = []
symbolCords = []

for line in lines:
  line = line.rstrip()
  partList.append([*line])

j = 0
for part in partList:
  k = 0
  for symbol in part:
    if not (symbol.isdigit()) and symbol != '.':
      symbolCords.append([j, k])
    k += 1
  j += 1
  
partLen = len(partList[0])
listLen = len(partList)
totalParts = 0
partNumberList = []

def helper(yCord, xCord):
  partNumber = str(partList[yCord][xCord])
  x = 1
  while xCord - x >= 0 and partList[yCord][xCord - x].isdigit():
    partNumber = partList[yCord][xCord - x] + partNumber
    x += 1
  x = 1
  while xCord + x < partLen and partList[yCord][xCord + x].isdigit():
    partNumber += partList[yCord][xCord + x]
    x += 1
  if partNumber not in partNumberList:
    partNumberList.append(partNumber)
    return int(partNumber)
  else:
    return 0

for symbol in symbolCords:
  print(symbol)
  #check top
  if symbol[0] - 1 >= 0:
    yCord = symbol[0] - 1
    xCord = symbol[1]
    if partList[yCord][xCord].isdigit():
      totalParts += helper(yCord, xCord)

  #check up right
  if symbol[0] -1 >= 0 and symbol[1] + 1 <= partLen:
    yCord = symbol[0] - 1
    xCord = symbol[1] + 1
    if partList[yCord][xCord].isdigit():
      totalParts += helper(yCord, xCord)

  #check right
  if symbol[1] + 1 <= partLen:
    yCord = symbol[0]
    xCord = symbol[1] + 1
    if partList[yCord][xCord].isdigit():
      totalParts += helper(yCord, xCord)

  #check down right
  if symbol[0] + 1 <= listLen and symbol[1] + 1 <= partLen:
    yCord = symbol[0] + 1
    xCord = symbol[1] + 1
    if partList[yCord][xCord].isdigit():
      totalParts += helper(yCord, xCord)

  #check bottom
  if symbol[0] + 1 <= listLen:
    yCord = symbol[0] + 1
    xCord = symbol[1]
    if partList[yCord][xCord].isdigit():
      totalParts += helper(yCord, xCord)

  #check down left
  if symbol[0] + 1 <= listLen and symbol[1] - 1 >= 0:
    yCord = symbol[0] + 1
    xCord = symbol[1] - 1
    if partList[yCord][xCord].isdigit():
      totalParts += helper(yCord, xCord)

  #check left
  if symbol[1] - 1 >= 0:
    yCord = symbol[0]
    xCord = symbol[1] - 1
    if partList[yCord][xCord].isdigit():
      totalParts += helper(yCord, xCord)

  #check up left
  if symbol[0] - 1 >= 0 and symbol[1] - 1 >= 0:
    yCord = symbol[0] - 1
    xCord = symbol[1] - 1
    if partList[yCord][xCord].isdigit():
      totalParts += helper(yCord, xCord)

print(totalParts)