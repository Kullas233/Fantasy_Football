import re

def JustGetLetters(text):
    new = ""
    for char in text:
        if(re.match("[A-Z]", char)):
            new += char
    return new

file = open('data/fp/all.txt', "r")

newFile = []
for line in file:
    newFile.append(line)



newString = []
for x in range(len(newFile)):
    if("(" in newFile[x]):
        newString.append(newFile[x-1][:-1] + newFile[x])

lineNum=0
players = []
for line in newString:
    line = line.replace('\t',' ')
    line = line.replace('  ',' ')
    index = line.index('(')
    line = line[:index] + ' ' + line[index:]

    words = words = line.split(' ')
    # if(len(words) == 8 and words[7] == '\n'):
    #     del words[7]
    #     del words[6]
    # elif(len(words) == 7 and words[6] == '\n'):
    #     del words[6]
    #     del words[5]

    if("(" in words[3]):
        words[1] = words[1] + " " + words[2]
        del words[2]
    else:
        words[1] = words[1] + " " + words[2] + " " + words[3]
        del words[3]
        del words[2]

    words[2] = words[2][1:-1]

    words[3] = JustGetLetters(words[3])

    players.append(words)

newFile = "Rank,Name,Pos,Team,Cost\n"
for player in players:
    newFile += player[0] + "," + player[1] + "," + player[3] + "," + player[2] + ",-1"
    newFile += "\n"

file.close()
file = open('data/fp/data.csv', "w")
file.write(newFile)