import re

# file = open('cummings.txt', "r")
# file = open('eisenberg.txt', "r")
file = open('Fantasy_Football_26/data/cbs/richard.txt', "r")
lineNum=0
players = []
for line in file:
    if(lineNum == 0):
        lineNum+=1
        continue
    line = line.replace('\t',' ')
    line = line.replace('  ',' ')
    words = line.split(' ')

    if(len(words) == 6):
        words[2] = words[2] + " " + words[3]
        words[3] = words[4]
        words[4] = words[5]

    newWords = []
    for word in words:
        if(not re.match("[A-z0-9]", word[-1:])):
            word = word[:-1]
        newWords.append(word)

    newWords.append(newWords[4])
    newWords[4] = newWords[3]
    newWords[3] = newWords[2][-2:]
    newWords[2] = newWords[2][:-2]

    if("$" in newWords[4]):
        newWords[1] = newWords[1] + " " + newWords[2]
        del newWords[2]
    else:
        newWords[1] = newWords[1] + " " + newWords[2] + " " + newWords[3]
        del newWords[3]
        del newWords[2]
    # print(newWords)
    players.append(newWords)

# print(players)

newFile = "Rank,Name,Pos,Team,Cost\n"
for player in players:
    # print(player)
    newFile += player[0] + "," + player[1] + "," + player[2] + ",Dumb," + player[3][1:]
    newFile += "\n"

file.close()
# file = open('c_data.csv', "w")
# file = open('e_data.csv', "w")
file = open('Fantasy_Football_26/data/cbs/r_data.csv', "w")
file.write(newFile)