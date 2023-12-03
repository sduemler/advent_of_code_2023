input = open("1/input.txt", "r")
lines = input.readlines()

totalValue = 0
numLines = 0

for line in lines:
  lineValue = ''
  for x in range(len(line)):
    if line[x].isdigit():
      lineValue = lineValue + line[x]
      break
  for x in range(len(line)-1, -1, -1):
    if line[x].isdigit():
      lineValue = lineValue + line[x]
      break
  totalValue = totalValue + int(lineValue)

print(totalValue)