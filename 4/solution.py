input = open("4/input.txt", "r")
lines = input.readlines()

totalValue = 0
cardValues = {}

for line in lines:
  card = 1
  line = line.rstrip()
  cardValue = 0
  cardSplit = line.split(': ')
  winningNums = (cardSplit[1].split(' | ')[0]).split()
  yourNums = (cardSplit[1].split(' | ')[1]).split()
  for num in yourNums:
    if num in winningNums:
      if cardValue == 0:
        cardValue = 1
      else:
        cardValue = cardValue * 2
  cardValues[card] = cardValue
  card += 1
  totalValue += cardValue

print(totalValue)