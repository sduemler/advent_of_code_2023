input = open("6/input.txt", "r")
lines = input.readlines()

times = []
distances = []
recordMultiply = 1

for line in lines:
    line = line.rstrip()
    raceSplit = line.split(':')
    if raceSplit[0] == 'Time':
        times = ' '.join(raceSplit[1].split(" ")).split()
    if raceSplit[0] == 'Distance':
        distances = ' '.join(raceSplit[1].split(' ')).split()    

for x in range(len(times)):
    raceTimes = 0
    for y in range(int(times[x])):
        raceTime = y * (int(times[x]) - y)
        if raceTime > int(distances[x]):
            raceTimes += 1
    recordMultiply = recordMultiply * raceTimes

print(recordMultiply)
            