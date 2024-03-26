import re

# FIX JR TO JR. AND ST TO ST.

# file = open('data/cbs/cummings.txt', "r")
# file = open('data/cbs/eisenberg.txt', "r")
file = open('data/cbs/richard.txt', "r")

lineNum=0
players = []
for line in file:
    if(lineNum == 0):
        lineNum+=1
        continue
    line = line.replace('\t',' ')
    line = line.replace('  ',' ')
    words = line.split(' ')
    newWords = []
    for word in words:
        if(not re.match("[A-z0-9]", word[-1:])):
            word = word[:-1]
        newWords.append(word)

    if("$" in newWords[5]):
        newWords[1] = newWords[1] + " " + newWords[2]
        del newWords[2]
    else:
        newWords[1] = newWords[1] + " " + newWords[2] + " " + newWords[3]
        del newWords[3]
        del newWords[2]
    players.append(newWords)

# print(players)

newFile = "Rank,Name,Pos,Team,Cost\n"
for player in players:
    newFile += player[0] + "," + player[1] + "," + player[3] + "," + player[2] + "," + player[4][1:]
    newFile += "\n"

file.close()
# file = open('data/cbs/c_data.csv', "w")
# file = open('data/cbs/e_data.csv', "w")
file = open('data/cbs/r_data.csv', "w")
file.write(newFile)