import re

def JustGetLetters(text):
    new = ""
    for char in text:
        if(re.match("[A-Z]", char)):
            new += char
    return new

file = open('data/espn/yates.txt', "r")

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
    if(line == ""):
        continue
    line = line.replace('\t',' ')
    words = line.split(' ')

    if("(" in words[4]):
        words[1] = words[1] + " " + words[2][:-1]
        del words[2]
    else:
        words[1] = words[1] + " " + words[2] + " " + words[3][:-1]
        del words[3]
        del words[2]

    

    words[0] = words[0][:-1]
    words[2] = words[2].upper()
    words[3] = JustGetLetters(words[3])
    # del words[3]
    players.append(words)

newFile = "Rank,Name,Pos,Team,Cost\n"
for player in players:
    newFile += player[0] + "," + player[1] + "," + player[3] + "," + player[2] + ",-1"
    newFile += "\n"

file.close()
file = open('data/espn/y_data.csv', "w")
file.write(newFile)