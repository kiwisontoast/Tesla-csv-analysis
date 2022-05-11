data = open("TSLA.txt", "r").readlines()
dataset = len(data)-1
#variables
summedrise = 0
summedfall = 0

timesrose = 0
timesfell = 0

timesfallrise = 0
timesrisefall = 0
timesriserise = 0
timesfallfall = 0

previousDif = 0
for i in range(2, len(data)):
    lastline = data[i-1].split(",")
    line = data[i].split(",")

    difference = (float(line[4])-float(line[1]))/float(line[1])*100

    lastdif = previousDif
    previousDif = difference

    if (difference > 0):
        timesrose += 1
        summedrise += difference

        if i == 2:
            continue
        if lastdif > 0:
            timesriserise += 1
        else:
            timesfallrise += 1
    else:
        timesfell += 1
        summedfall -= difference

        if i == 2:
            continue
        if lastdif < 0:
            timesfallfall += 1
        else:
            timesrisefall += 1

print("Rose: "+str(timesrose)+" times")
print("Rise Chance: {:.2f}%".format(timesrose/dataset*100))
print("Average Rise: {:.2f}%".format(summedrise/timesrose))
print()
print("Fell: "+str(timesfell)+" times")
print("Fall Chance: {:.2f}%".format(timesfell/dataset*100))
print("Average Fall: {:.2f}%".format(summedfall/timesfell))
print()
print("Rose-Rose: {:.2f}%".format(timesriserise/dataset*100))
print("Rose-Fell: {:.2f}%".format(timesrisefall/dataset*100))
print("Fell-Rose: {:.2f}%".format(timesfallrise/dataset*100))
print("Fell-Fell: {:.2f}%".format(timesfallfall/dataset*100))
