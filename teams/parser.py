file = open('teams/ovr.txt', "r")

abbrs = { "ARI":"Arizona Cardinals", "ATL":"Atlanta Falcons", "BAL":"Baltimore Ravens", "BUF":"Buffalo Bills", "CAR":"Carolina Panthers", "CHI":"Chicago Bears", "CIN":"Cincinnati Bengals", "CLE":"Cleveland Browns", "DAL":"Dallas Cowboys", "DEN":"Denver Broncos", "DET":"Detroit Lions", "GB":"Green Bay Packers", "HOU":"Houston Texans", "IND":"Indianapolis Colts", "JAX":"Jacksonville Jaguars", "KC":"Kansas City Chiefs", "LAC":"Los Angeles Chargers", "LAR":"Los Angeles Rams", "LV":"Las Vegas Raiders", "MIA":"Miami Dolphins", "MIN":"Minnesota Vikings", "NE":"New England Patriots", "NO":"New Orleans Saints", "NYG":"New York Giants", "NYJ":"New York Jets", "PHI":"Philadelphia Eagles", "PIT":"Pittsburgh Steelers", "SEA":"Seattle Seahawks", "SF":"San Francisco 49ers", "TB":"Tampa Bay Buccaneers", "TEN":"Tennessee Titans", "WAS":"Washington Commanders" }

lineNum=0
teams = []
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
    if(len(newWords) == 6):
        newWords[1] = newWords[1] + " " + newWords[2]
        del newWords[2]
    else:
        newWords[1] = newWords[1] + " " + newWords[2] + " " + newWords[3]
        del newWords[3]
        del newWords[2]
    for team in abbrs.items():
        if(newWords[1] == team[1]):
            newWords[1] = team[0]
    teams.append(newWords)

newFile = "SOS,Team,Line\n"
for team in teams:

    newFile += team[0] + "," + team[1] + "," + team[4]
    newFile += "\n"

file.close()
file = open('teams/data.csv', "w")
file.write(newFile)