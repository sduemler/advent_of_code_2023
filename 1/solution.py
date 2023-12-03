input = open("1/input.txt", "r")
lines = input.readlines()

totalValue = 0

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

totalValue = 0
numMap = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
keyList = list(numMap.keys())
valueList = list(numMap.values())

for line in lines:
  #double for loop, for each character go five out and check if it's in the dictionary
  #then the same thing but backards, adding to the front of the tempValue

  lineValue = ''
  x = 0
  while lineValue == '' and x < len(line):
    if line[x].isdigit():
      lineValue += line[x]
      break
    else:
      tempValue = line[x]
      i = x
      while i+1 != len(line) and not len(tempValue) > 5:
        i += 1
        tempValue += line[i]
        if tempValue in valueList:
          lineValue += keyList[valueList.index(tempValue)]
          break
    x += 1

  x = len(line) - 1
  while len(lineValue) == 1 and x != -1:
    if line[x].isdigit():
      lineValue += line[x]
      break
    else:
      tempValue = line[x]
      i = x
      while i-1 != -1 and not len(tempValue) > 5:
        i -= 1
        tempValue = line[i] + tempValue
        if tempValue in valueList:
          lineValue += keyList[valueList.index(tempValue)]
          break
    x -= 1
  totalValue += int(lineValue)

print(totalValue)

