file = open('Fantasy_Football_26/data/athletic/ovr.txt', "r")

lineNum=0
players = []
for line in file:
    if(lineNum == 0):
        lineNum+=1
        continue
    line = line.replace('\t',' ')
    words = line.split(' ')
    newWords = []
    for word in words:
        if(word[-1:] == "\n"):
            word = word[:-1]
        newWords.append(word)

    # FA Handling
    if(newWords[3] == 'FA'):
        newWords[5] = newWords[4]
        newWords[4] = '(0)'
    elif(newWords[4] == 'FA'):
        newWords[6] = newWords[5]
        newWords[5] = '(0)'

    if("(" in newWords[4]):
        del newWords[4]
        newWords[1] = newWords[1] + " " + newWords[2]
        del newWords[2]
    else:
        del newWords[5]
        newWords[1] = newWords[1] + " " + newWords[2] + " " + newWords[3]
        del newWords[3]
        del newWords[2]
    players.append(newWords)

newFile = "Rank,Name,Pos,Team,Cost\n"
for player in players:

    #Hollywood Handling
    if(player[1] == "Hollywood Brown"):
        player[1] = "Marquise Brown"

    #Team Name Handling
    if(player[2] == 'JAC'):
        player[2] = 'JAX'

    newFile += player[0] + "," + player[1] + "," + player[3] + "," + player[2] + ",-1"
    newFile += "\n"

file.close()
file = open('Fantasy_Football_26/data/athletic/data.csv', "w")
file.write(newFile)