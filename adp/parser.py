import string

file = open('data.txt', "r")
abbrs = { "ARI":"Arizona Cardinals", "ATL":"Atlanta Falcons", "BAL":"Baltimore Ravens", "BUF":"Buffalo Bills", "CAR":"Carolina Panthers", "CHI":"Chicago Bears", "CIN":"Cincinnati Bengals", "CLE":"Cleveland Browns", "DAL":"Dallas Cowboys", "DEN":"Denver Broncos", "DET":"Detroit Lions", "GB":"Green Bay Packers", "HOU":"Houston Texans", "IND":"Indianapolis Colts", "JAX":"Jacksonville Jaguars", "KC":"Kansas City Chiefs", "LAC":"Los Angeles Chargers", "LAR":"Los Angeles Rams", "LV":"Las Vegas Raiders", "MIA":"Miami Dolphins", "MIN":"Minnesota Vikings", "NE":"New England Patriots", "NO":"New Orleans Saints", "NYG":"New York Giants", "NYJ":"New York Jets", "PHI":"Philadelphia Eagles", "PIT":"Pittsburgh Steelers", "SEA":"Seattle Seahawks", "SF":"San Francisco 49ers", "TB":"Tampa Bay Buccaneers", "TEN":"Tennessee Titans", "WAS":"Washington Commanders" }

lineNum=0
players = []
count = 0
player = []
for line in file:
    line = line.replace('\t',' ')
    line = line.replace('  ',' ')
    line = line.replace('\n','')
    if(lineNum == 0):
        lineNum+=1
        continue
    
    if(count == 0):
        count=count
    elif(count == 1):
        count=count
    elif(count == 2):
        player.append(line)
    elif(count == 3 and ((line == 'Q' or line == 'O') or line == 'D')):
        count-=1
    elif(count == 3):
        player.append(line.upper())
    elif(count == 4):
        player.append(line)
    elif(count == 5):
        player.append(line)
    elif(count == 6):
        count=count
    elif(count == 7):
        count=count
    elif(count == 8):
        count=count
    elif(count == 9):
        players.append(player)
        player = []
        if not line.__contains__("."):
            count=0
        else:
            count=-1

    count+=1


newFile = "Name,Pos,Team,ADP\n"
for player in players:
    newFile += player[0] + "," + player[2] + "," + player[1] + ', ' + player[3]
    newFile += "\n"

file.close()
file = open('data.csv', "w")
# file = open('data/cbs/e_data.csv', "w")
# file = open('data/cbs/r_data.csv', "w")
file.write(newFile)