import re

def JustGetLetters(text):
    new = ""
    for char in text:
        if(re.match("[A-Z]", char)):
            new += char
    return new

file = open('clay.txt', "r")

newFile = []
for line in file:
    newFile.append(line)

newString = ""
for line in newFile:
    # print(line)
    matches = re.findall("[0-9]+\\.", line)[1:]
    for match in matches:
        index = line.index(match)
        line = line[:index] + '\n' + line[index:]
    newString += line

lineNum=0
players = []
lines = newString.split("\n")
for line in lines:
    # print(line)
    if(lineNum == 0):
        lineNum+=1
        continue
    line = line.replace('\t',' ')
    # line = line.replace('.',',')
    words = re.split('[,\\.] ', line)
    if(re.match("[A-Z]\\.[A-Z]",words[1])):
        words[1] = words[1]+". " + words[2]
        del words[2]

    if(words[1] == "Amon-Ra St"):
        words[1] = words[1] + ". " + words[2]
        del words[2]

    moreWords = words[2].split()

    # words[0] = words[0][:-1]
    print(words)
    print(len(moreWords))
    moreWords[2] = JustGetLetters(moreWords[2])

    del moreWords[3]
    del moreWords[1]

    words[2] = moreWords[0]
    words.append(moreWords[1])

    # DST Handling
    if(line.__contains__('DST')):
        words[1] = words[1].split(" ")[0] + ' Defense'

    players.append(words)

newFile = "Rank,Name,Pos,Team,Cost\n"
for player in players:
    print(player)
    newFile += player[0] + "," + player[1] + "," + player[3] + "," + player[2] + ",-1"
    newFile += "\n"

file.close()
file = open('cl_data.csv', "w")
file.write(newFile)