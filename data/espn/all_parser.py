import re

def JustGetLetters(text):
    new = ""
    for char in text:
        if(re.match("[A-Z]", char)):
            new += char
    return new

file = open('data/espn/all.txt', "r")

newFile = []
for line in file:
    newFile.append(line)

newString = ""
for line in newFile:
    # print(line)
    matches = re.findall("[0-9]+\.", line)[1:]
    for match in matches:
        index = line.index(match)
        line = line[:index] + '\n' + line[index:]
    newString += line

lineNum=0
players = []
lines = newString.split("\n")
for line in lines:
    if(lineNum == 0):
        lineNum+=1
        continue
    line = line.replace('\t',' ')
    words = line.split(' ')
    if("$" in words[5]):
        words[2] = words[2] + " " + words[3][:-1]
    else:
        words[2] = words[2] + " " + words[3] + " " + words[4][:-1]
        del words[4]

    words[0] = words[0][:-1]
    words[1] = JustGetLetters(words[1])
    del words[3]
    players.append(words)

for player in players:
    if(len(player) == 7):
        del player[6]

    cost = float(player[4][1:])/2
    player[4] = cost

newFile = "Rank,Name,Pos,Team,Cost\n"
for player in players:
    newFile += player[0] + "," + player[2] + "," + player[1] + "," + player[3] + "," + str(player[4])
    newFile += "\n"

file.close()
file = open('data/espn/all.csv', "w")
file.write(newFile)